import requests
import re

# 1. KANALI ÇEKME FONKSİYONU: İctimai TV
def itv_link_bul():
    url = "https://live.itv.az/player.php"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
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
        print("İTV linki bulunamadı, yedek link atanıyor:", e)
    return "https://live.itv.az/itv.m3u8"

# 2. KANALI ÇEKME FONKSİYONU: ATV Azerbaijan
def atv_link_bul():
    url = "https://atv.az/live"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Referer": "https://atv.az/"
    }
    try:
        response = requests.get(url, headers=headers, timeout=15)
        linkler = re.findall(r'(https?://[^\s"\']+\.m3u8[^\s"\']*)', response.text)
        if linkler:
            return linkler[0]
    except Exception as e:
        print("ATV linki bulunamadı, yedek link atanıyor:", e)
    return "https://live.atv.az/atv/index.m3u8"

# İki kanalın da en güncel linklerini çekiyoruz
itv_link = itv_link_bul()
atv_link = atv_link_bul()

print(f"Güncel İTV Linki: {itv_link}")
print(f"Güncel ATV Linki: {atv_link}")

# İKİ KANALI BİRDEN YENİ LOGOLARIYLA ALT ALTA BİRLEŞTİRİYORUZ
m3u_yapisi = f"""#EXTM3U
#EXTINF:-1 tvg-id="ITV" tvg-logo="https://i.ibb.co/dsfZQ0Cq/itv.png" group-title="Azerbaijan",İctimai TV
{itv_link}
#EXTINF:-1 tvg-id="ATV" tvg-logo="https://i.ibb.co/JRy9jg98/atv.png" group-title="Azerbaijan",ATV Azerbaijan
{atv_link}
"""

# listem.m3u dosyasına iki kanalı birden yazıyoruz
with open("listem.m3u", "w", encoding="utf-8") as f:
    f.write(m3u_yapisi)

print("Listem.m3u dosyası yeni logolarla ve iki kanalla başarıyla güncellendi!")
