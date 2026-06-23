import re
import requests

# Test etmek istediğiniz canlı tv izleme sitesinin linki
url = "https://live.itv.az/"  # Örnek hedef site

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}


def linki_yakala():
    try:
        response = requests.get(url, headers=headers)
        # Kaynak kodundaki .m3u8 veya token içeren yayın linkini arıyoruz
        match = re.search(r'(https://.*?\.m3u8\?token=[a-zA-Z0-9]+)', response.text)

        if match:
            stream_url = match.group(1)
            # M3U Dosya formatını oluşturuyoruz
            m3u_icerik = f"#EXTM3U\n#EXTINF:-1 tvg-logo=\"https://itv.az/assets/images/itv-logo.png\" group-title=\"Ulusal\", TRT 1\n{stream_url}\n"

            # Dosyaya kaydet
            with open("listem.m3u", "w", encoding="utf-8") as f:
                f.write(m3u_icerik)
            print("M3U Listesi başarıyla güncellendi!")
        else:
            print("Kaynak kodunda m3u8 linki bulunamadı.")
    except Exception as e:
        print("Hata oluştu:", e)


if __name__ == "__main__":
    linki_yakala()
