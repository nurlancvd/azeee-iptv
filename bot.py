import requests
import re

# 1. KANAL: İctimai TV (Dinamik link arayıcı)
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
        print("İTV linki çekilemedi:", e)
    return "https://live.itv.az/itv.m3u8"

# 2. KANAL: ARB Güneş TV (Dinamik hash arayıcı)
def arb_gunes_link_bul():
    url = "https://canlitv.com/arb-gunes-tv?ulke=az"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Referer": "https://canlitv.com/"
    }
    try:
        response = requests.get(url, headers=headers, timeout=15)
        linkler = re.findall(r'(https?://[^\s"\']+\.m3u8[^\s"\']*)', response.text)
        if linkler:
            for link in linkler:
                if "arbgunes" in link.lower() or "canlitv" in link.lower():
                    return link
            return linkler[0]
    except Exception as e:
        print("ARB Güneş linki çekilemedi:", e)
    return "https://yayin2.canlitv.fun/live/arbgunes.stream/chunklist_w1263573850.m3u8"

# Aktif kanalların linklerini çekiyoruz
itv_link = itv_link_bul()
arb_gunes_link = arb_gunes_link_bul()

print(f"İTV Güncel Linki: {itv_link}")
print(f"ARB Güneş Anlık Linki: {arb_gunes_link}")

# YENİ İKİ KANALLI M3U FORMATI (ATV kaldırıldı, yeni ARB Güneş logosu eklendi)
m3u_yapisi = f"""#EXTM3U
#EXTINF:-1 tvg-id="ITV" tvg-logo="https://i.ibb.co/dsfZQ0Cq/itv.png" group-title="Azerbaijan",İctimai TV
{itv_link}
#EXTINF:-1 tvg-id="ARBGunes" tvg-logo="https://i.ibb.co/B5PVstQJ/gunes.jpg" group-title="Azerbaijan",ARB Güneş TV
{arb_gunes_link}
"""

# Ortak listem.m3u dosyasına kaydet
with open("listem.m3u", "w", encoding="utf-8") as f:
    f.write(m3u_yapisi)

print("Listem.m3u dosyası güncellendi: ATV silindi, ARB Güneş logosu yenilendi!")
