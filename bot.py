from curl_cffi import requests
import re
from datetime import datetime

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Referer": "https://mediabay.tv/",
    "Origin": "https://mediabay.tv"
}

# --- DİNAMİK TOKEN ÇÖZÜCÜ FONKSİYONLAR ---

def cbc_sport_link_bul():
    # CBC Sport sitesine CORS Proxy üzerinden erişim
    proxy_url = "https://corsproxy.io/?https://cbcsport.az/live/"
    try:
        response = requests.get(proxy_url, headers=headers, impersonate="chrome120", timeout=12)
        linkler = re.findall(r'(https?://[^\s"\']+\.m3u8[^\s"\']*)', response.text)
        if linkler:
            print("CBC Sport linki başarıyla çekildi!")
            return linkler[0]
    except Exception as e:
        print("CBC Sport çekilemedi, hatası:", e)
    return "https://cbcsports-live.lg.mncdn.com/cbcsports_live/cbcsports/chunklist.m3u8"

def mediabay_tokenli_link_bul(channel_id, page_slug, yedek_link):
    """
    GitHub Runner IP/DNS engellerini aşmak için CORS Proxy üzerinden 
    Mediabay API'sine erişir ve geçerli token'lı canlı yayın linkini çeker.
    """
    proxy_api_url = f"https://corsproxy.io/?https://api.mediabay.tv/v2/stream/get-url?id={channel_id}"
    
    try:
        res = requests.get(proxy_api_url, headers=headers, impersonate="chrome120", timeout=12)
        if res.status_code == 200:
            data = res.json()
            stream_url = data.get("data", {}).get("url") or data.get("url")
            if stream_url and "token=" in stream_url:
                print(f"ID {channel_id} için Başarıyla Token Alındı!")
                return stream_url
            elif stream_url:
                return stream_url
    except Exception as e:
        print(f"Mediabay Proxy API hatası (ID: {channel_id}):", e)

    print(f"ID {channel_id} için token alınamadı, yedek linke düşüldü.")
    return yedek_link

# --- CANLI LİNK ÇEKİMLERİ ---

# CBC Sport
cbc_link = cbc_sport_link_bul()

# Mediabay Kanalları
cbc_az_link = mediabay_tokenli_link_bul(
    154, "CBC%20(Caspian%20Broadcasting%20Company)",
    "https://st2.mediabay.tv/CBC_AZ/tracks-v2a1/mono.m3u8"
)

mtvaz_link = mediabay_tokenli_link_bul(
    593, "MTV%20Azerbaijan",
    "https://st2.mediabay.tv/MTV_AZ/tracks-v2a1/mono.m3u8"
)

kn_music_link = mediabay_tokenli_link_bul(
    714, "KNTV",
    "https://st2.mediabay.tv/KNTV/tracks-v3a1/mono.m3u8"
)

konul_link = mediabay_tokenli_link_bul(
    715, "Konul%20Tv",
    "https://st2.mediabay.tv/KonulTV/tracks-v3a1/mono.m3u8"
)

k_music_link = mediabay_tokenli_link_bul(
    716, "Konul%20Music%20Tv",
    "https://st2.mediabay.tv/Konul_MusicTV/tracks-v3a1/mono.m3u8"
)

# En Güncel YodaCDN Token'ı
guncel_token = "eyJpcCI6IjkyLjM5Ljk0LjIwMyIsInVhIjoiTW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDEwOyBLKSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvNTUwLjAuMC4wIE1vYmlsZSBTYWZhcmkvNTM3MzYiLCJleHAiOjE3ODUzMjg0MzAsImp0aSI6ImZiZDg5YzU3YWFiNTU4NzcifQ%3D%3D.jhtyuuhYTshosf67e+loVyrtIMrjc7az%2F0gAb9BzjmY%3D"

# Diğer Eklenen Kanallar
ayaz_link = "https://janya-ayaztv.vgcdn.net/ptnr-WebApp/title-Ayaz_TV/v1/vglive-sk-934820/AyazTV_800k.m3u8"
ftv_link = "https://stream.ftv.az/live/ftv.m3u8"

# 1. GRUP: YodaCDN & Sabit Yayınlar
aztv_link = f"https://str.yodacdn.net/azertv/tracks-v3a1/mono.ts.m3u8?token={guncel_token}"
medeniyyet_link = f"https://str2.yodacdn.net/medeniyyettele/tracks-v3a1/mono.ts.m3u8?token={guncel_token}"
idman_link = f"https://str2.yodacdn.net/idmantele/tracks-v3a1/mono.ts.m3u8?token={guncel_token}"
real_link = f"https://str.yodacdn.net/real/tracks-v1a1/mono.ts.m3u8?token={guncel_token}"
xezer_link = f"https://str.yodacdn.net/xazartv/tracks-v1a1/mono.ts.m3u8?token={guncel_token}"
space_link = f"https://str.yodacdn.net/space/tracks-v1a1/mono.ts.m3u8?token={guncel_token}"
ntv_link = f"https://str.yodacdn.net/ntv/mono.m3u8?token={guncel_token}"
qafqaz_link = f"https://str.yodacdn.net/qafkaz/tracks-v1a1/mono.ts.m3u8?token={guncel_token}"
apatv_link = f"https://str.yodacdn.net/apatv/tracks-v1a1/mono.ts.m3u8?token={guncel_token}"
arb_link = f"https://str.yodacdn.net/arb/tracks-v1a1/mono.ts.m3u8?token={guncel_token}"

# Sabit M3U Altyapılı Linkler
itv_link = "https://live.itv.az/itv.m3u8?bandwidth=3900&shift=0"
atv_link = "https://lives.atv.az:5443/ATV_TV_STREAM/streams/atvcanli.m3u8"
baku_link = "https://rtmp.baku.tv/hls/bakutv_1080p.m3u8"
kanals_link = "https://lives.atv.az:5443/KANAL-S/streams/kanals.m3u8"
dunya_link = "https://stream.dunyatv.az/live/dunyatv.m3u8"

# 2. GRUP: Yedek Yayınlar
aztv2_link = f"https://str.yodacdn.net/azertv/tracks-v1a1/mono.ts.m3u8?token={guncel_token}"
medeniyyet2_link = f"https://str2.yodacdn.net/medeniyyettele/tracks-v3a1/mono.ts.m3u8?token={guncel_token}"
idman2_link = f"https://str2.yodacdn.net/idmantele/tracks-v1a1/mono.ts.m3u8?token={guncel_token}"
real2_link = f"https://str.yodacdn.net/real/mono.m3u8?token={guncel_token}"
xezer2_link = "https://xezerxeber.az/stream/main_stream.m3u8"
azad2_link = f"https://str.yodacdn.net/atv/tracks-v1a1/mono.ts.m3u8?token={guncel_token}"
space2_link = f"https://str.yodacdn.net/space/mono.m3u8?token={guncel_token}"
arb2_link = f"https://str.yodacdn.net/arb/tracks-v1a1/mono.ts.m3u8?token={guncel_token}"
cbctv2_link = f"https://str.yodacdn.net/cbc/tracks-v1a1/mono.ts.m3u8?token={guncel_token}"
cbc_sport2_link = "https://cbcsports-live.lg.mncdn.com/cbcsports_live/cbcsports/chunklist.m3u8"
dunyatv2_link = "https://stream.dunyatv.az/live/dunyatv.m3u8"
bakutv2_link = "https://rtmp.baku.tv/hls/bakutv_1080p.m3u8"
ictimaitv2_link = "https://live.itv.az/itv.m3u8?bandwidth=3900&shift=0"

# --- M3U LİSTESİ OLUŞTURMA ---

m3u_satirlari = [
    '#EXTM3U',
    f'# EXTM3U - Son Guncelleme: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")} UTC',
    
    # --- ANA KANAL GRUBU ---
    '#EXTINF:-1 tvg-id="ITV" tvg-logo="https://i.ibb.co/dsfZQ0Cq/itv.png" group-title="Azerbaijan",İctimai TV',
    f"{itv_link}",
    '#EXTINF:-1 tvg-id="CBCSport" tvg-logo="https://i.ibb.co/pBpdbm2j/cbcs.png" group-title="Azerbaijan",CBC Sport',
    f"{cbc_link}",
    '#EXTINF:-1 tvg-id="AzTV" tvg-logo="https://i.ibb.co/dwNh0pyg/aztv.jpg" group-title="Azerbaijan",AzTV',
    f"{aztv_link}",
    '#EXTINF:-1 tvg-id="MedeniyyetTV" tvg-logo="https://i.ibb.co/B5BtPZLd/medeniyyet.jpg" group-title="Azerbaijan",Medeniyyet TV',
    f"{medeniyyet_link}",
    '#EXTINF:-1 tvg-id="IdmanTV" tvg-logo="https://i.ibb.co/pBNzbCWD/idmanv.jpg" group-title="Azerbaijan",İdman TV',
    f"{idman_link}",
    '#EXTINF:-1 tvg-id="RealTV" tvg-logo="https://i.ibb.co/Rpk9CspD/realtv.jpg" group-title="Azerbaijan",Real TV',
    f"{real_link}",
    '#EXTINF:-1 tvg-id="XezerTV" tvg-logo="https://i.ibb.co/q3BGCK8n/xezer.png" group-title="Azerbaijan",Xezer TV',
    f"{xezer_link}",
    '#EXTINF:-1 tvg-id="AzadAzerbaycanTV" tvg-logo="https://i.ibb.co/rDHp5Fk/azad.png" group-title="Azerbaijan",Azad Azerbaycan TV',
    f"{atv_link}",
    '#EXTINF:-1 tvg-id="BakuTV" tvg-logo="https://i.ibb.co/23N9F7s8/bakutvv.png" group-title="Azerbaijan",Baku TV',
    f"{baku_link}",
    '#EXTINF:-1 tvg-id="SpaceTV" tvg-logo="https://i.ibb.co/v49CGvL2/spacetv.jpg" group-title="Azerbaijan",Space TV',
    f"{space_link}",
    '#EXTINF:-1 tvg-id="ARBHD" tvg-logo="https://i.ibb.co/fY05FcdF/arbhd.jpg" group-title="Azerbaijan",ARB HD',
    f"{arb_link}",
    '#EXTINF:-1 tvg-id="DunyaTV" tvg-logo="https://i.ibb.co/whNG1qY9/dunyatv.jpg" group-title="Azerbaijan",Dunya TV',
    f"{dunya_link}",
    '#EXTINF:-1 tvg-id="CBCTV" tvg-logo="https://i.ibb.co/mVjVMH0J/cbcaz.png" group-title="Azerbaijan",CBC TV',
    f"{cbc_az_link}",
    '#EXTINF:-1 tvg-id="NaxcivanTV" tvg-logo="https://i.ibb.co/bgyrK5r2/NTV.png" group-title="Azerbaijan",Naxçıvan TV',
    f"{ntv_link}",
    '#EXTINF:-1 tvg-id="QafqazTV" tvg-logo="https://i.ibb.co/dsn5NM67/qafqaz-tv.png" group-title="Azerbaijan",Qafqaz TV',
    f"{qafqaz_link}",
    '#EXTINF:-1 tvg-id="APATV" tvg-logo="https://i.ibb.co/WNnQ0fw9/apatv.jpg" group-title="Azerbaijan",APA TV',
    f"{apatv_link}",
    '#EXTINF:-1 tvg-id="KanalS" tvg-logo="https://i.ibb.co/RpgqMMct/Kanal-S.png" group-title="Azerbaijan",Kanal S',
    f"{kanals_link}",
    '#EXTINF:-1 tvg-id="MTVAzerbaijan" tvg-logo="https://i.ibb.co/60Q8b9Q6/MTV.jpg" group-title="Azerbaijan",MTV Azerbaijan',
    f"{mtvaz_link}",

    # --- MÜZİK VE DİĞER KANALLAR ---
    '#EXTINF:-1 tvg-id="AyazTV" tvg-logo="https://i.ibb.co/gNdFzTf/ayaztv.png" group-title="Azerbaijan",Ayaz TV',
    f"{ayaz_link}",
    '#EXTINF:-1 tvg-id="KNMusicTV" tvg-logo="https://i.ibb.co/BVwxFNfn/kntv.png" group-title="Azerbaijan",KN Music TV',
    f"{kn_music_link}",
    '#EXTINF:-1 tvg-id="KonulTV" tvg-logo="https://i.ibb.co/YFh87zMF/ktv.jpg" group-title="Azerbaijan",Konul TV',
    f"{konul_link}",
    '#EXTINF:-1 tvg-id="KMusicTV" tvg-logo="https://i.ibb.co/xSp2kZ5S/kmusic.png" group-title="Azerbaijan",K Music TV',
    f"{k_music_link}",
    '#EXTINF:-1 tvg-id="FTV" tvg-logo="https://i.ibb.co/tMwJ0tBm/ftv.png" group-title="Azerbaijan",FTV',
    f"{ftv_link}",

    # --- YEDEK KANAL GRUBU ---
    '#EXTINF:-1 tvg-id="IctimaiTV2" tvg-logo="https://i.ibb.co/FbKMRyFz/itv2.jpg" group-title="Azerbaijan",Ictimai TV 2',
    f"{ictimaitv2_link}",
    '#EXTINF:-1 tvg-id="CBCSport2" tvg-logo="https://i.ibb.co/WvVYTGLR/cbc2.png" group-title="Azerbaijan",CBC Sport 2',
    f"{cbc_sport2_link}",
    '#EXTINF:-1 tvg-id="AZTV2" tvg-logo="https://i.ibb.co/dwNh0pyg/aztv.jpg" group-title="Azerbaijan",AZTV 2',
    f"{aztv2_link}",
    '#EXTINF:-1 tvg-id="MedeniyyetTV2" tvg-logo="https://i.ibb.co/B5BtPZLd/medeniyyet.jpg" group-title="Azerbaijan",Medeniyyet TV 2',
    f"{medeniyyet2_link}",
    '#EXTINF:-1 tvg-id="IdmanTV2" tvg-logo="https://i.ibb.co/pBNzbCWD/idmanv.jpg" group-title="Azerbaijan",IdmanTV 2',
    f"{idman2_link}",
    '#EXTINF:-1 tvg-id="RealTV2" tvg-logo="https://i.ibb.co/Rpk9CspD/realtv.jpg" group-title="Azerbaijan",Real TV 2',
    f"{real2_link}",
    '#EXTINF:-1 tvg-id="XezerTV2" tvg-logo="https://i.ibb.co/q3BGCK8n/xezer.png" group-title="Azerbaijan",Xezer TV 2',
    f"{xezer2_link}",
    '#EXTINF:-1 tvg-id="AzadAzerbaycan2" tvg-logo="https://i.ibb.co/rDHp5Fk/azad.png" group-title="Azerbaijan",Azad Azerbaycan 2',
    f"{azad2_link}",
    '#EXTINF:-1 tvg-id="BakuTV2" tvg-logo="https://i.ibb.co/zWSLHdDt/bakutv.jpg" group-title="Azerbaijan",Baku TV 2',
    f"{bakutv2_link}",
    '#EXTINF:-1 tvg-id="SpaceTV2" tvg-logo="https://i.ibb.co/v49CGvL2/spacetv.jpg" group-title="Azerbaijan",Space TV 2',
    f"{space2_link}",
    '#EXTINF:-1 tvg-id="ARB2" tvg-logo="https://i.ibb.co/fY05FcdF/arbhd.jpg" group-title="Azerbaijan",ARB 2',
    f"{arb2_link}",
    '#EXTINF:-1 tvg-id="CBCTV2" tvg-logo="https://i.ibb.co/mVjVMH0J/cbcaz.png" group-title="Azerbaijan",CBCTV 2',
    f"{cbctv2_link}",
    '#EXTINF:-1 tvg-id="DunyaTV2" tvg-logo="https://i.ibb.co/whNG1qY9/dunyatv.jpg" group-title="Azerbaijan",Dunya TV 2',
    f"{dunyatv2_link}"
]

m3u_yapisi = "\n".join(m3u_satirlari)

with open("listem.m3u", "w", encoding="utf-8") as f:
    f.write(m3u_yapisi)

print("----------------------------------------")
print("ISLEM TAMAMLANDI!")
print("Cekilen CBC TV Linki:", cbc_az_link)
print("----------------------------------------")
