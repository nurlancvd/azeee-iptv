import requests
import re

def guncel_link_bul():
    # Sizin verdiğiniz ana canlı yayın sayfası
    url = "https://live.itv.az/player.php"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Referer": "https://live.itv.az/"
    }
    
    try:
        response = requests.get(url, headers=headers)
        # Sayfanın kaynak kodlarından itv.m3u8?token=... linkini yakalıyoruz
        linkler = re.findall(r'(https?://[^\s"\']+\.m3u8[^\s"\']*)', response.text)
        if linkler:
            return linkler[0]
    except Exception as e:
        print("Link bulunamadı:", e)
    
    # Eğer tarayıcı korumayı geçemezse yedek olarak ana linki dön
    return "https://live.itv.az/itv.m3u8"

# 1. En güncel şifreli linki otomatik çek
canli_yayin_linki = guncel_link_bul()

# 2. Logolu ve kategorili M3U yapısını oluştur
m3u_yapisi = f"""#EXTM3U
#EXTINF:-1 tvg-id="ITV" tvg-logo="https://i.ibb.co/dsfZQ0Cq/itv.png" group-title="Azerbaijan",İctimai TV
{canli_yayin_linki}
"""

# 3. Hazırlanan bu yapıyı otomatik listem.m3u dosyasına yaz
with open("listem.m3u", "w", encoding="utf-8") as f:
    f.write(m3u_yapisi)

print("İşlem Başarılı! Listem.m3u logolu ve güncel linkle yenilendi.")
