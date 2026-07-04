import requests
import re

# Tüm isteklere gerçek tarayıcı süsü vermek için ortak başlıklar
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5"
}

# --- DİNAMİK TOKEN ÇÖZÜCÜ FONKSİYONLAR ---

# 1. GRUP: CBC Sport (Dinamik Çözücü)
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

# 2. GRUP: YODACDN Ortak Token Çözücü (yoda.az altyapılı tüm kanallar için)
def yoda_token_bul():
    url = "https://aztv.az/az/live"
    try:
        response = requests.get(url, headers=headers, timeout=7)
        token_match = re.search(r'token=([A-Za-z0-9%_\-\.\+]+)', response.text)
        if token_match:
            print("Siteden yeni ortak yoda token başarıyla çekildi!")
            return token_match.group(1)
    except Exception as e:
        print("AzTV sitesi botu engelledi, yedek token devreye giriyor.")
    return None

# 3. GRUP: Xezer TV Dinamik Çözücü (Mevcut Liste İçin)
def xezer_link_bul():
    url = "http://149.255.152.218/channels.aspx?channel=xazer.m3u8"
    try:
        response = requests.get(url, headers=headers, timeout=10)
        token_match = re.search(r'token=([a-f0-9]+)', response.text)
        e_match = re.search(r'e=([0-9]+)', response.text)
        token = token_match.group(1) if token_match else "a4e6bcd7297a4cd917ce916ef9665bdb"
        e_val = e_match.group(1) if e_match else "1782410890"
        return f"http://149.255.152.199/xazer.m3u8?bandwidth=2096&e={e_val}&playlistlength=5&shift=0&sid=coder_53&token={token}&user=37076"
    except Exception as e:
        print("Xezer TV token çekilemedi:", e)
    return "http://149.255.152.199/xazer.m3u8?bandwidth=2096&e=1782410890&playlistlength=5&shift=0&sid=coder_53&token=a4e6bcd7297a4cd917ce916ef9665bdb&user=37076"

# 4. GRUP: Space TV Dinamik Çözücü (Mevcut Liste İçin)
def space_link_bul():
    url = "http://149.255.152.218/channels.aspx?channel=space.m3u8"
    try:
        response = requests.get(url, headers=headers, timeout=10)
        token_match = re.search(r'token=([a-f0-9]+)', response.text)
        e_match = re.search(r'e=([0-9]+)', response.text)
        token = token_match.group(1) if token_match else "0ed5c63f2d6189a7198b3c7e0b330f40"
        e_val = e_match.group(1) if e_match else "1782389870"
        return f"http://149.255.152.199/space.m3u8?bandwidth=6096&e={e_val}&playlistlength=5&shift=0&sid=coder_75&token={token}&user=37076"
    except Exception as e:
        print("Space TV token çekilemedi:", e)
    return "http://149.255.152.199/space.m3u8?bandwidth=6096&e=1782389870&playlistlength=5&shift=0&sid=coder_75&token=0ed5c63f2d6189a7198b3c7e0b330f40&user=37076"

# 5. GRUP: ARB HD Dinamik Çözücü (Mevcut Liste İçin)
def arb_link_bul():
    url = "http://149.255.152.218/channels.aspx?channel=arbhd.m3u8"
    try:
        response = requests.get(url, headers=headers, timeout=10)
        token_match = re.search(r'token=([a-f0-9]+)', response.text)
        e_match = re.search(r'e=([0-9]+)', response.text)
        token = token_match.group(1) if token_match else "1f22fc47e451e32d285081f4423f5132"
        e_val = e_match.group(1) if e_match else "1782390335"
        return f"http://149.255.152.199/arbhd.m3u8?bandwidth=6096&e={e_val}&playlistlength=5&shift=0&sid=coder_62&token={token}&user=37076"
    except Exception as e:
        print("ARB HD token çekilemedi:", e)
    return "http://149.255.152.199/arbhd.m3u8?bandwidth=6096&e=1782390335&playlistlength=5&shift=0&sid=coder_62&token=1f22fc47e451e32d285081f4423f5132&user=37076"

# 6. GRUP: Dunya TV Dinamik Çözücü (Mevcut Liste İçin)
def dunya_link_bul():
    url = "http://149.255.152.218/channels.aspx?channel=dunya.m3u8"
    try:
        response = requests.get(url, headers=headers, timeout=10)
        token_match = re.search(r'token=([a-f0-9]+)', response.text)
        e_match = re.search(r'e=([0-9]+)', response.text)
        token = token_match.group(1) if token_match else "27ec3d0239833be43b818aa00fa9995d"
        e_val = e_match.group(1) if e_match else "1782391302"
        return f"http://149.255.152.199/dunya.m3u8?bandwidth=2096&e={e_val}&playlistlength=5&shift=0&sid=coder_53&token={token}&user=37076"
    except Exception as e:
        print("Dunya TV token çekilemedi:", e)
    return "http://149.255.152.199/dunya.m3u8?bandwidth=2096&e=1782391302&playlistlength=5&shift=0&sid=coder_53&token=27ec3d0239833be43b818aa00fa9995d&user=37076"

# 7. GRUP: CBC TV Dinamik Çözücü (Mevcut Liste İçin)
def cbc_az_link_bul():
    url = "http://149.255.152.218/channels.aspx?channel=cbcaz.m3u8"
    try:
        response = requests.get(url, headers=headers, timeout=10)
        token_match = re.search(r'token=([a-f0-9]+)', response.text)
        e_match = re.search(r'e=([0-9]+)', response.text)
        token = token_match.group(1) if token_match else "b158f29892dd1c37d43b777aae7b9655"
        e_val = e_match.group(1) if e_match else "1782396949"
        return f"http://149.255.152.199/cbcaz.m3u8?bandwidth=2096&e={e_val}&playlistlength=5&shift=0&sid=coder_52&token={token}&user=37076"
    except Exception as e:
        print("CBC TV token çekilemedi:", e)
    return "http://149.255.152.199/cbcaz.m3u8?bandwidth=2096&e=1782396949&playlistlength=5&shift=0&sid=coder_52&token=b158f29892dd1c37d43b777aae7b9655&user=37076"

# 8. GRUP: ARB Güneş Dinamik Çözücü (Mevcut Liste İçin)
def arb_gunes_link_bul():
    url = "http://149.255.152.218/channels.aspx?channel=arbgunes.m3u8"
    try:
        response = requests.get(url, headers=headers, timeout=10)
        token_match = re.search(r'token=([a-f0-9]+)', response.text)
        e_match = re.search(r'e=([0-9]+)', response.text)
        token = token_match.group(1) if token_match else "fb5b7d89ffefef249100cbac9aa3d98c"
        e_val = e_match.group(1) if e_match else "1782397933"
        return f"http://149.255.152.199/arbgunes.m3u8?bandwidth=2096&e={e_val}&playlistlength=5&shift=0&sid=coder_52&token={token}&user=37076"
    except Exception as e:
        print("ARB Güneş token çekilemedi:", e)
    return "http://149.255.152.199/arbgunes.m3u8?bandwidth=2096&e=1782397933&playlistlength=5&shift=0&sid=coder_52&token=fb5b7d89ffefef249100cbac9aa3d98c&user=37076"


# --- LİNKLERİ VE TOKENLARI DERLEME ---

cbc_link = cbc_sport_link_bul()
guncel_token = yoda_token_bul()

# Bota özel dinamik çözücüler (Mevcut listenin ilgili kanalları için)
xezer_link = xezer_link_bul()
space_link = space_link_bul()
arb_link = arb_link_bul()
dunya_link = dunya_link_bul()
cbc_az_link = cbc_az_link_bul()
arb_gunes_link = arb_gunes_link_bul()

# Yedek Yoda Token (Sitenin korumaya geçme ihtimaline karşı)
if not guncel_token:
    guncel_token = "eyJpcCI6IjE1OC4xODEuNDUuNjciLCJ1YSI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2EgR2Vja28pIENocm9tZS8xNDkuMC4wLjAgU2FmYXJpLzUzNy4zNiIsImV4cCI6MTg4MjI0MzM2MSwianRpIjoiZGRiYTIyZDA5NTI0ZGRjZCJ9.2+7AgtxqqYc7QqKtDL9bO30SLXSmEZ7GjFp3KSK4gPg%3D"

# 1. GRUP: Mevcut Listenin Yoda Havuzu
aztv_link = f"https://str.yodacdn.net/azertv/tracks-v3a1/mono.ts.m3u8?token={guncel_token}"
medeniyyet_link = f"https://str2.yodacdn.net/medeniyyettele/tracks-v3a1/mono.ts.m3u8?token={guncel_token}"
idman_link = f"https://str2.yodacdn.net/idmantele/tracks-v3a1/mono.ts.m3u8?token={guncel_token}"
real_link = f"https://str.yodacdn.net/real/tracks-v1a1/mono.ts.m3u8?token={guncel_token}"
ntv_link = f"https://str.yodacdn.net/ntv/mono.m3u8?token={guncel_token}"
biznes_link = f"https://str.yodacdn.net/biznestv/tracks-v1a1/mono.ts.m3u8?token={guncel_token}"
arb24_link = f"https://str.yodacdn.net/arb24/tracks-v1a1/mono.ts.m3u8?token={guncel_token}"
qafqaz_link = f"https://str.yodacdn.net/qafkaz/tracks-v1a1/mono.ts.m3u8?token={guncel_token}"
apatv_link = f"https://str.yodacdn.net/apatv/tracks-v1a1/mono.ts.m3u8?token={guncel_token}"
mtvaz_link = f"https://str.yodacdn.net/mtvaz/tracks-v1a1/mono.ts.m3u8?token={guncel_token}"

# 2. GRUP: Yeni Eklenen 14 Kanalın Yoda Havuzu (Aynı dinamik tokenı paylaşırlar)
aztv2_link = f"https://str.yodacdn.net/azertv/tracks-v1a1/mono.ts.m3u8?token={guncel_token}"
medeniyyet2_link = f"https://str.yodacdn.net/medeniyyettele/tracks-v1a1/mono.ts.m3u8?token={guncel_token}"
idman2_link = f"https://str.yodacdn.net/idmantele/tracks-v1a1/mono.ts.m3u8?token={guncel_token}"
real2_link = f"https://str.yodacdn.net/real/mono.m3u8?token={guncel_token}"
xezer2_link = f"https://str.yodacdn.net/xazartv/tracks-v1a1/mono.ts.m3u8?token={guncel_token}"
azad2_link = f"https://str.yodacdn.net/atv/tracks-v1a1/mono.ts.m3u8?token={guncel_token}"
bakutv2_link = f"https://str.yodacdn.net/bakutv/tracks-v1a1/mono.ts.m3u8?token={guncel_token}"
space2_link = f"https://str.yodacdn.net/space/tracks-v1a1/mono.ts.m3u8?token={guncel_token}"
arb2_link = f"https://str.yodacdn.net/arb/tracks-v1a1/mono.ts.m3u8?token={guncel_token}"
cbctv2_link = f"https://str.yodacdn.net/cbc/tracks-v1a1/mono.ts.m3u8?token={guncel_token}"
arbgunesh2_link = f"https://str.yodacdn.net/arbgunesh/tracks-v1a1/mono.ts.m3u8?token={guncel_token}"

# Sabit CDN Altyapılı Kalıcı Linkler (Mevcut + Yeni Karışık)
itv_link = "https://ikolive-fwc.akamaized.net/fwc/fifa/fwc_1080ph/chunks.m3u8"
atv_link = "https://lives.atv.az:5443/ATV_TV_STREAM/streams/atvcanli.m3u8"
baku_link = "https://rtmp.baku.tv/hls/bakutv_1080p.m3u8"
kanals_link = "https://lives.atv.az:5443/KANAL-S/streams/kanals.m3u8"
cbc_sport2_link = "https://cbcsports-live.lg.mncdn.com/cbcsports_live/cbcsports/chunklist.m3u8"
dunyatv2_link = "https://stream.ftv.az/live/dunyatv.m3u8"


# --- M3U FORMAT YAPISI (TEK KATEGORİ - 35 KANAL DÜZ LİSTE) ---

m3u_satirlari = [
    "#EXTM3U",
    # --- İLK 21 KANAL ---
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
    f'#EXTINF:-1 tvg-id="RealTV" tvg-logo="https://i.ibb.co/Rpk9CspD/realtv.jpg" group-title="Azerbaijan",Real TV',
    f"{real_link}",
    f'#EXTINF:-1 tvg-id="XezerTV" tvg-logo="https://i.ibb.co/q3BGCK8n/xezer.png" group-title="Azerbaijan",Xezer TV',
    f"{xezer_link}",
    f'#EXTINF:-1 tvg-id="AzadAzerbaycanTV" tvg-logo="https://i.ibb.co/rDHp5Fk/azad.png" group-title="Azerbaijan",Azad Azerbaycan TV',
    f"{atv_link}",
    f'#EXTINF:-1 tvg-id="BakuTV" tvg-logo="https://i.ibb.co/23N9F7s8/bakutvv.png" group-title="Azerbaijan",Baku TV',
    f"{baku_link}",
    f'#EXTINF:-1 tvg-id="SpaceTV" tvg-logo="https://i.ibb.co/v49CGvL2/spacetv.jpg" group-title="Azerbaijan",Space TV',
    f"{space_link}",
    f'#EXTINF:-1 tvg-id="ARBHD" tvg-logo="https://i.ibb.co/fY05FcdF/arbhd.jpg" group-title="Azerbaijan",ARB HD',
    f"{arb_link}",
    f'#EXTINF:-1 tvg-id="DunyaTV" tvg-logo="https://i.ibb.co/whNG1qY9/dunyatv.jpg" group-title="Azerbaijan",Dunya TV',
    f"{dunya_link}",
    f'#EXTINF:-1 tvg-id="CBCTV" tvg-logo="https://i.ibb.co/mVjVMH0J/cbcaz.png" group-title="Azerbaijan",CBC TV',
    f"{cbc_az_link}",
    f'#EXTINF:-1 tvg-id="NaxcivanTV" tvg-logo="https://i.ibb.co/bgyrK5r2/NTV.png" group-title="Azerbaijan",Naxçıvan TV',
    f"{ntv_link}",
    f'#EXTINF:-1 tvg-id="ARBGunes" tvg-logo="https://i.ibb.co/1GG5X2mb/gunestv.png" group-title="Azerbaijan",ARB Güneş',
    f"{arb_gunes_link}",
    f'#EXTINF:-1 tvg-id="BiznesTV" tvg-logo="https://i.ibb.co/k60QQDpX/biznestv.png" group-title="Azerbaijan",Biznes TV',
    f"{biznes_link}",
    f'#EXTINF:-1 tvg-id="ARB24" tvg-logo="https://i.ibb.co/3mJSN4yT/arb24.png" group-title="Azerbaijan",ARB 24',
    f"{arb24_link}",
    f'#EXTINF:-1 tvg-id="QafqazTV" tvg-logo="https://i.ibb.co/dsn5NM67/qafqaz-tv.png" group-title="Azerbaijan",Qafqaz TV',
    f"{qafqaz_link}",
    f'#EXTINF:-1 tvg-id="APATV" tvg-logo="https://i.ibb.co/WNnQ0fw9/apatv.jpg" group-title="Azerbaijan",APA TV',
    f"{apatv_link}",
    f'#EXTINF:-1 tvg-id="KanalS" tvg-logo="https://i.ibb.co/RpgqMMct/Kanal-S.png" group-title="Azerbaijan",Kanal S',
    f"{kanals_link}",
    f'#EXTINF:-1 tvg-id="MTVAzerbaijan" tvg-logo="https://i.ibb.co/60Q8b9Q6/MTV.jpg" group-title="Azerbaijan",MTV Azerbaijan',
    f"{mtvaz_link}",

    # --- ARDINA EKLENEN YENİ 14 YEDEK KANAL (22 - 35) ---
    f'#EXTINF:-1 tvg-id="IctimaiTV2" tvg-logo="https://i.ibb.co/FbKMRyFz/itv2.jpg" group-title="Azerbaijan",Ictimai TV 2',
    f"http://149.255.152.199/ictimai.m3u8?bandwidth=2096&e=1783263773&playlistlength=5&shift=0&sid=coder_52&token=76ab141688bbf61a45cf657ec56ef492&user=37076",
    f'#EXTINF:-1 tvg-id="CBCSport2" tvg-logo="https://i.ibb.co/WvVYTGLR/cbc2.png" group-title="Azerbaijan",CBC Sport 2',
    f"{cbc_sport2_link}",
    f'#EXTINF:-1 tvg-id="AZTV2" tvg-logo="https://i.ibb.co/dwNh0pyg/aztv.jpg" group-title="Azerbaijan",AZTV 2',
    f"{aztv2_link}",
    f'#EXTINF:-1 tvg-id="MedeniyyetTV2" tvg-logo="https://i.ibb.co/B5BtPZLd/medeniyyet.jpg" group-title="Azerbaijan",Medeniyyet TV 2',
    f"{medeniyyet2_link}",
    f'#EXTINF:-1 tvg-id="IdmanTV2" tvg-logo="https://i.ibb.co/pBNzbCWD/idmanv.jpg" group-title="Azerbaijan",IdmanTV 2',
    f"{idman2_link}",
    f'#EXTINF:-1 tvg-id="RealTV2" tvg-logo="https://i.ibb.co/Rpk9CspD/realtv.jpg" group-title="Azerbaijan",Real TV 2',
    f"{real2_link}",
    f'#EXTINF:-1 tvg-id="XezerTV2" tvg-logo="https://i.ibb.co/q3BGCK8n/xezer.png" group-title="Azerbaijan",Xezer TV 2',
    f"{xezer2_link}",
    f'#EXTINF:-1 tvg-id="AzadAzerbaycan2" tvg-logo="https://i.ibb.co/rDHp5Fk/azad.png" group-title="Azerbaijan",Azad Azerbaycan 2',
    f"{azad2_link}",
    f'#EXTINF:-1 tvg-id="BakuTV2" tvg-logo="https://i.ibb.co/zWSLHdDt/bakutv.jpg" group-title="Azerbaijan",Baku TV 2',
    f"{bakutv2_link}",
    f'#EXTINF:-1 tvg-id="SpaceTV2" tvg-logo="https://i.ibb.co/v49CGvL2/spacetv.jpg" group-title="Azerbaijan",Space TV 2',
    f"{space2_link}",
    f'#EXTINF:-1 tvg-id="ARB2" tvg-logo="https://i.ibb.co/fY05FcdF/arbhd.jpg" group-title="Azerbaijan",ARB 2',
    f"{arb2_link}",
    f'#EXTINF:-1 tvg-id="CBCTV2" tvg-logo="https://i.ibb.co/mVjVMH0J/cbcaz.png" group-title="Azerbaijan",CBC TV 2',
    f"{cbctv2_link}",
    f'#EXTINF:-1 tvg-id="ARBGunes2" tvg-logo="https://i.ibb.co/prshwRH9/gunestv.png" group-title="Azerbaijan",ARB Gunes 2',
    f"{arbgunesh2_link}",
    f'#EXTINF:-1 tvg-id="DunyaTV2" tvg-logo="https://i.ibb.co/whNG1qY9/dunyatv.jpg" group-title="Azerbaijan",Dunya TV 2',
    f"{dunyatv2_link}"
]

m3u_yapisi = "\n".join(m3u_satirlari)

# listem.m3u dosyasına kaydetme
with open("listem.m3u", "w", encoding="utf-8") as f:
    f.write(m3u_yapisi)

print("35 kanallı kesintisiz tek parça M3U listesi başarıyla güncellendi!")
