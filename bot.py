import requests
import re

# 1. KANAL: İctimai TV (Dinamik arayıcı)
def itv_link_bul():
    url = "https://live.itv.az/player.php"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Referer": "https://live.itv.az/"
    }
    try:
        response = requests.get(url, headers=headers, timeout=15)
        linkler = re.findall(r'(https?://[^\s"\']+\.m3u8[^\s"\']*)', response.text)
        if linkler:
            for link in linkler:
                if "itv" in link.lower() and "player.php" not in link:
                    return link
            return linkler[0]
    except Exception as e:
        print("İTV linki çekilemedi, yedek atanıyor:", e)
    return "https://live.itv.az/itv.m3u8"

# 2. KANAL: CBC Sport (Dinamik arayıcı)
def cbc_sport_link_bul():
    url = "https://cbcsport.az/live/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Referer": "https://cbcsport.az/"
    }
    try:
        response = requests.get(url, headers=headers, timeout=15)
        linkler = re.findall(r'(https?://[^\s"\']+\.m3u8[^\s"\']*)', response.text)
        if linkler:
            for link in linkler:
                if "cbcsports" in link.lower() or "mncdn" in link.lower():
                    return link
            return linkler[0]
    except Exception as e:
        print("CBC Sport canlı linki çekilemedi, yedek atanıyor:", e)
    return "https://cbcsports-live.lg.mncdn.com/cbcsports_live/cbcsports/chunklist.m3u8"

# Dinamik kanalların linklerini çekiyoruz
itv_link = itv_link_bul()
cbc_link = cbc_sport_link_bul()

# SABİT RESMİ CDN LİNKLERİ (Korumaya ve şifreye takılmayanlar)
aztv_link = "https://str.yodacdn.net/azertv/index.m3u8"
medeniyyet_link = "https://str2.yodacdn.net/medeniyyettele/index.m3u8"

# 5. KANAL: Idman TV (Şifresiz resmi ana CDN linki)
idman_link = "https://str2.yodacdn.net/idmantele/index.m3u8"

print(f"Güncel İTV Linki: {itv_link}")
print(f"Güncel CBC Sport Linki: {cbc_link}")
print(f"Sabit AzTV Linki: {aztv_link}")
print(f"Sabit Medeniyyet Linki: {medeniyyet_link}")
print(f"Sabit İdman TV Linki: {idman_link}")

# M3U Formatı - Satır satır güvenli birleştirme (İdman TV eklendi)
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
    f"{idman_link}"
]

m3u_yapisi = "\n".join(m3u_satirlari)

# listem.m3u dosyasına kaydediyoruz
with open("listem.m3u", "w", encoding="utf-8") as f:
    f.write(m3u_yapisi)

print("Listem.m3u dosyası 5 şahane kanalla başarıyla güncellendi!")
