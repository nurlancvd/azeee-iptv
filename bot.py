import requests
import re

# 1. KANAL: İctimai TV
def itv_link_bul():
    url = "https://live.itv.az/player.php"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    try:
        response = requests.get(url, headers=headers, timeout=15)
        linkler = re.findall(r'(https?://[^\s"\']+\.m3u8[^\s"\']*)', response.text)
        if linkler:
            for link in linkler:
                if "itv" in link.lower() and "player.php" not in link:
                    return link
            return linkler[0]
    except Exception as e:
        print("İTV hatası:", e)
    return "https://live.itv.az/itv.m3u8"

# 2. KANAL: CBC Sport
def cbc_sport_link_bul():
    url = "https://cbcsport.az/live/"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    try:
        response = requests.get(url, headers=headers, timeout=15)
        linkler = re.findall(r'(https?://[^\s"\']+\.m3u8[^\s"\']*)', response.text)
        if linkler:
            return linkler[0]
    except Exception as e:
        print("CBC hatası:", e)
    return "https://cbcsports-live.lg.mncdn.com/cbcsports_live/cbcsports/chunklist.m3u8"

# YODACDN (AzTV, Medeniyyet, İdman) Ortak Token Çözücü
def yoda_token_bul():
    url = "https://aztv.az/az/live"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Referer": "https://aztv.az/"
    }
    try:
        response = requests.get(url, headers=headers, timeout=15)
        # Sitedeki canlı yayın linkinin içinden token kısmını cımbızlıyoruz
        token_match = re.search(r'token=([A-Za-z0-9%_\-\.\+]+)', response.text)
        if token_match:
            return token_match.group(1)
    except Exception as e:
        print("Token çekilemedi:", e)
    return None

# Ana Akışı Çalıştırıyoruz
itv_link = itv_link_bul()
cbc_link = cbc_sport_link_bul()
guncel_token = yoda_token_bul()

# Eğer siteden token çekilemezse listeyi patlatmamak için yedek token'lar (senin verdiklerin) devkeye girer
if not guncel_token:
    guncel_token = "eyJpcCI6IjE1OC4xODEuNDUuNjciLCJ1YSI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xNDkuMC4wLjAgU2FmYXJpLzUzNy4zNiIsImV4cCI6MTc4MjI0MzM2MSwianRpIjoiZGRiYTIyZDA5NTI0ZGRjZCJ9.2+7AgtxqqYc7QqKtDL9bO30SLXSmEZ7GjFp3KSK4gPg%3D"

# Kanalları güncel dinamik token ile oluşturuyoruz
aztv_link = f"https://str.yodacdn.net/azertv/tracks-v3a1/mono.ts.m3u8?token={guncel_token}"
medeniyyet_link = f"https://str2.yodacdn.net/medeniyyettele/tracks-v3a1/mono.ts.m3u8?token={guncel_token}"
idman_link = f"https://str2.yodacdn.net/idmantele/tracks-v3a1/mono.ts.m3u8?token={guncel_token}"

# M3U Formatı - Satır satır güvenli birleştirme
m3u_satirlari = [
    "#EXTM3U",
    f'#EXTINF:-1 tvg-id="ITV" tvg-logo="https://i.ibb.co/dsfZQ0Cq/itv.png" group-title="Azerbaijan",İctimai TV',
    f"{itv_link}",
    f'#EXTINF:-1 tvg-id="CBCSport" tvg-logo="https://i.ibb.co/pBpdbm2j/cbcs.png" group-title="Azerbaijan",CBC Sport',
    f"{cbc_link}",
    f'#EXTINF:-1 tvg-id="AzTV" tvg-
