import re
import time
from playwright.sync_api import sync_playwright

def mediabay_tokenli_link_bul(channel_id, page_slug, yedek_link):
    """
    Her kanal için bağımsız taze oturum açar, player'ın ağ trafiğini dinler
    ve üretilen EN SON taze token'lı m3u8 linkini yakalar.
    """
    target_url = f"https://mediabay.tv/tv/{channel_id}/{page_slug}"
    found_links = []

    try:
        with sync_playwright() as p:
            # Temiz, önbelleksiz gizli tarayıcı başlat
            browser = p.chromium.launch(headless=True)
            context = browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
                viewport={"width": 1280, "height": 720}
            )
            page = context.new_page()

            # Ağ trafiğini dinle - Yakalanan m3u8 linklerini kaydet
            def handle_request(request):
                url = request.url
                if ".m3u8" in url and "token=" in url:
                    found_links.append(url)

            page.on("request", handle_request)

            # Sayfaya git ve player'ın yüklenmesini bekle
            page.goto(target_url, timeout=20000, wait_until="domcontentloaded")
            page.wait_for_timeout(3000)

            # Otomatik oynatma başlamadıysa ekrana tıkla
            try:
                page.click("video", timeout=2000)
            except:
                pass

            # Taze akış isteği için bekle
            page.wait_for_timeout(4000)

            browser.close()

            # Yakalanan en SON isteği al
            if found_links:
                latest_link = found_links[-1]
                print(f"ID {channel_id} için Taze Token Yakalandı!")
                return latest_link

    except Exception as e:
        print(f"ID {channel_id} Playwright Hatası:", e)

    print(f"ID {channel_id} için token bulunamadı, varsayılan linke düşüldü.")
    return yedek_link


def main():
    # Mediabay Kanallarınızın Listesi
    mediabay_kanallari = [
        {
            "id": "154",
            "slug": "cbc-tv",
            "name": "CBC TV",
            "tvg": "CBCTV",
            "logo": "https://i.ibb.co/mVjVMH0J/cbcaz.png",
            "yedek": "https://st2.mediabay.tv/CBC_AZ/tracks-v1a1/mono.m3u8"
        },
        {
            "id": "593",
            "slug": "cbc-sport",
            "name": "CBC Sport HD",
            "tvg": "CBCSport",
            "logo": "https://i.ibb.co/Lzr2xS4/cbcsport.png",
            "yedek": "https://st2.mediabay.tv/CBC_SPORT/tracks-v1a1/mono.m3u8"
        },
        {
            "id": "714",
            "slug": "atv-az",
            "name": "ATV Azerbaijan",
            "tvg": "ATVAz",
            "logo": "https://i.ibb.co/4vy3s9L/atvaz.png",
            "yedek": "https://st2.mediabay.tv/ATV_AZ/tracks-v1a1/mono.m3u8"
        },
        {
            "id": "715",
            "slug": "space-tv",
            "name": "Space TV",
            "tvg": "SpaceTV",
            "logo": "https://i.ibb.co/q9b9gZ9/spacetv.png",
            "yedek": "https://st2.mediabay.tv/SPACE_AZ/tracks-v1a1/mono.m3u8"
        },
        {
            "id": "716",
            "slug": "xazar-tv",
            "name": "Xazar TV",
            "tvg": "XazarTV",
            "logo": "https://i.ibb.co/5XZL6Z5/xazartv.png",
            "yedek": "https://st2.mediabay.tv/KHAZAR_AZ/tracks-v1a1/mono.m3u8"
        }
    ]

    playlist_lines = ["#EXTM3U"]
    cbc_tv_link = ""

    print("Mediabay Kanalları İşleniyor...")
    for kanal in mediabay_kanallari:
        link = mediabay_tokenli_link_bul(kanal["id"], kanal["slug"], kanal["yedek"])
        
        if kanal["id"] == "154":
            cbc_tv_link = link

        # M3U Formatına Header Bilgileriyle Birlikte Ekleme
        playlist_lines.append(f'#EXTINF:-1 tvg-id="{kanal["tvg"]}" tvg-logo="{kanal["logo"]}" group-title="Azerbaijan",{kanal["name"]}')
        playlist_lines.append('#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36')
        playlist_lines.append('#EXTVLCOPT:http-referrer=https://mediabay.tv/')
        playlist_lines.append('#EXTHTTP:{"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64)","Referer":"https://mediabay.tv/"}')
        playlist_lines.append(link)

    # M3U Dosyasını Yaz
    with open("listem.m3u", "w", encoding="utf-8") as f:
        f.write("\n".join(playlist_lines))

    print("-" * 40)
    print("ISLEM TAMAMLANDI!")
    print("Cekilen CBC TV Linki:", cbc_tv_link)
    print("-" * 40)


if __name__ == "__main__":
    main()
