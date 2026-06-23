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

# 2. KANAL: CBC Sport (Dinamik arayıcı ve kaynak korumalı)
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
        print("CBC Sport canlı linki çekilemedi, verdiğiniz m3u linki atanıyor:", e)
    # Siteden çekemezse senin verdiğin çalışan kesin m3u8 linkini taban alır
    return "https://cbcsports-live.lg.mncdn.com/cbcsports_live/cbcsports/chunklist.m3u8"

# Kanalların linklerini topluyoruz
itv_link = itv_link_bul()
cbc_link = cbc_sport_link_bul()

print(f"Güncel İTV Linki: {itv_link}")
print(f"Güncel CBC Sport Linki: {cbc_link}")

# M3U FORMATI (ARB Güneş silindi, CBC Sport yeni logosuyla eklendi)
m3u_yapisi = f"""#EXTM3U
#EXTINF:-1 tvg-id="ITV" tvg-logo="https://i.ibb.co/dsfZQ0Cq/itv.png" group-title="Azerbaijan",İctimai TV
{itv_link}
#EXTINF:-1 tvg-id="CBCSport" tvg-logo="https://i.ibb.co/pBpdbm2j/cbcs.png" group-title="Azerbaijan",CBC Sport
{cbc_link}
"""

# listem.m3u dosyasına kaydediyoruz
with open("listem.m3u", "w", encoding="utf-8") as f:
    f.write(m3u_yapisi)

print("Listem.m3u dosyası İTV ve CBC Sport ile başarıyla güncellendi!")
