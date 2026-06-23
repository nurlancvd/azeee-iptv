import requests
import re

# Tüm isteklere gerçek tarayıcı süsü vermek için ortak başlıklar
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5"
}

# 1. KANAL: İctimai TV
def itv_link_bul():
    url = "https://live.itv.az/player.php"
    try:
        response = requests.get(url, headers=headers, timeout=10)
        linkler = re.findall(r'(https?://[^\s"\']+\.m3u8[^\s"\']*)', response.text)
        if linkler:
            for link in linkler:
                if "itv" in link.lower() and "player.php" not in link:
                    return link
            return linkler[0]
    except Exception as e:
        print("İTV çekilemedi, yedek atanıyor:", e)
    return "https://live.itv.az/itv.m3u8"

# 2. KANAL: CBC Sport
def cbc_sport_link_bul():
    url = "https://cbcsport.az/live/"
    try:
        response = requests.get(url, headers=headers, timeout=10)
        linkler = re.findall(r'(https?://[^\s"\']+\.m3u8[^\s"\']*)', response.text)
        if linkler:
            return linkler[0]
    except Exception as e:
        print("CBC Sport çekilemedi, yedek atanıyor:", e)
    return "https://cbcsports-live.lg.mncdn.com/cbcsports_live/cbcsports/chunklist.m3u8"

# YODACDN (AzTV, Medeniyyet, İdman) Ortak Token Çözücü
def yoda_token_bul():
    url = "https://aztv.az/az/live"
    try:
        response = requests.get(url, headers=headers, timeout=7)
        token_match = re.search(r'token=([A-Za-z0-9%_\-\.\+]+)', response.text)
        if token_match:
            print("Siteden yeni token başarıyla çekildi!")
            return token_match.group(1)
    except Exception as e:
        print("AzTV sitesi botu engelledi, yedek token devreye giriyor.")
    return None

# Linkleri ve Token'ı topluyoruz
itv_link = itv_link_bul()
cbc_link = cbc_sport_link_bul()
guncel_token = yoda_token_bul()

# Eğer site botu engellediyse yedek token devreye girer
if not guncel_token:
    guncel_token = "eyJpcCI6IjE1OC4xODEuNDUuNjciLCJ1YSI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2EgR2Vja28pIENocm9tZS8xNDkuMC4wLjAgU2FmYXJpLzUzNy4zNiIsImV4cCI6MTc4MjI0MzM2MSwianRpIjoiZGRiYTIyZDA5NTI0ZGRjZCJ9.2+7AgtxqqYc7QqKtDL9bO30SLXSmEZ7GjFp3KSK4gPg%3D"

# Kanalları token ile inşa ediyoruz
aztv_link = f"https://str.yodacdn.net/azertv/tracks-v3a1/mono.ts.m3u8?token={guncel_token}"
medeniyyet_link = f"https://str2.yodacdn.net/medeniyyettele/tracks-v3a1/mono.ts.m3u8?token={guncel_token}"
idman_link = f"https://str2.yodacdn.net/idmantele/tracks-v3a1/mono.ts.m3u8?token={guncel_token}"

# 6. KANAL: Xezer TV (Sabit link)
xezer_link = "https://xezerxeber.az/stream/stream.m3u8"

# 7. KANAL: Azad Azerbaycan TV (Token istemeyen, sabit resmi CDN linki)
atv_link = "https://lives.atv.az:5443/ATV_TV_STREAM/streams/atvcanli.m3u8"

# M3U Format Yapısı (ATV eklendi)
m3u_satirlari = [
    "#EXTM3U",
    f'#EXTINF:-1 tvg-id="ITV" tvg-logo="https://i.ibb.co/dsfZQ0Cq/itv.png" group-title="Azerbaijan",İctimai TV',
    f"{itv_link}",
    f'#EXTINF:-1 tvg-id="CBCSport" tvg-logo="https://i.ibb.co/pBpdbm2j/cbcs.png" group-title="Azerbaijan",CBC Sport',
    f"{cbc_link}",
    f'#EXTINF:-1 tvg-id="AzTV" tvg-logo="https://i.ibb.co/dwNh0pyg/aztv.jpg" group-title="Azerbaijan",AzTV',
    f"{aztv_link}",
    f'#EXTINF:-1 tvg-id="MedeniyyetTV" tvg-logo="https://i.ibb.co/B5BtPZLd/medeniyyet.jpg" group-title="Azerbaijan",Medeniyyet TV',
    f"{medeniyyet_link}",
    f'#EXTINF:-1 tvg-id="IdmanTV" tvg-logo="https://i.ibb.co/pBNzbCWD/idmanv.jpg" group-title="Azerbaijan",İdman TV',
    f"{idman_link}",
    f'#EXTINF:-1 tvg-id="XezerTV" tvg-logo="https://i.ibb.co/q3BGCK8n/xezer.png" group-title="Azerbaijan",Xezer TV',
    f"{xezer_link}",
    f'#EXTINF:-1 tvg-id="AzadAzerbaycanTV" tvg-logo="https://i.ibb.co/rDHp5Fk/azad.png" group-title="Azerbaijan",Azad Azerbaycan TV',
    f"{atv_link}"
]

m3u_yapisi = "\n".join(m3u_satirlari)

# listem.m3u dosyasına kaydetme
with open("listem.m3u", "w", encoding="utf-8") as f:
    f.write(m3u_yapisi)

print("Listem.m3u dosyası 7 şahane kanalla başarıyla güncellendi!")
