import requests
import re

# Web istekleri için kullanılacak varsayılan header
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# --- DİNAMİK TOKEN ÇÖZÜCÜ FONKSİYONLAR ---

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

# CBC Sport Linki
cbc_link = cbc_sport_link_bul()

# En Güncel YodaCDN Token'ı (Ana Kanallar İçin)
guncel_token = "eyJpcCI6IjkyLjM5Ljk0LjIwMyIsInVhIjoiTW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDEwOyBLKSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvNTUwLjAuMC4wIE1vYmlsZSBTYWZhcmkvNTM3MzYiLCJleHAiOjE3ODUzMjg0MzAsImp0aSI6ImZiZDg5YzU3YWFiNTU4NzcifQ%3D%3D.jhtyuuhYTshosf67e+loVyrtIMrjc7az%2F0gAb9BzjmY%3D"

# Cloudflare Worker Linkleri
arb24_link = "https://empty-fire-e7df.ipx2026.workers.dev/arb24.m3u8"
arbgunesh_link = "https://empty-fire-e7df.ipx2026.workers.dev/arbgunes.m3u8"
mtv_link = "https://empty-fire-e7df.ipx2026.workers.dev/mtv.m3u8"
livetvaz_link = "https://empty-fire-e7df.ipx2026.workers.dev/livetvaz.m3u8"
cbctv_link = "https://empty-fire-e7df.ipx2026.workers.dev/cbc.m3u8"
spacetv2_link = "https://empty-fire-e7df.ipx2026.workers.dev/spacetv.m3u8"
arbhd2_link = "https://empty-fire-e7df.ipx2026.workers.dev/arb.m3u8"
real2_link = "https://empty-fire-e7df.ipx2026.workers.dev/realtv.m3u8"
xezer2_link = "https://empty-fire-e7df.ipx2026.workers.dev/xezertv.m3u8"

# Diğer Eklenen Kanallar
ayaz_link = "https://janya-ayaztv.vgcdn.net/ptnr-WebApp/title-Ayaz_TV/v1/vglive-sk-934820/AyazTV_800k.m3u8"
kn_music_link = "https://cdn4.yayin.com.tr/kntv/tracks-v1a1/mono.m3u8"
showplus_link = "https://rtmp.showplus.tv/hls/myshow.m3u8"
ktv_link = "https://cdn-konultvazerbaijan.yayin.com.tr/konultvazerbaijan/konultvazerbaijan/playlist.m3u8"
ftv_link = "https://stream.ftv.az/live/ftv.m3u8"
diginet_link = "https://a8.radyotelekom.com.tr:3276/stream/play.m3u8"
el_tv_link = "https://str.yodacdn.net/eltv/tracks-v1a1/mono.ts.m3u8?token=eyJpcCI6IjE4NS4xNDYuMTE1LjIyMCIsInVhIjoiTW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDE0OyBDVk02MzNBMTRUKSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvOTguMC40NzU4Ljg3IE1vYmlsZSBTYWZhcmkvNTM3IiwiZXhwIjoxNzg3MDg1ODE1LCJqdGkiOiIyZjVkZjI1MjdkMWUwOWI4In0%3D.R0FWS%2FtJTn4pMPtLjKFvAYVlLFdJtqPzXHHJ8xRXj+M%3D"
vip_hd_link = "https://str.yodacdn.net/vip/tracks-v1a1/mono.ts.m3u8?token=eyJpcCI6IjE4NS4xNDYuMTEyLjIyNSIsInVhIjoiTW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDEwOyBLKSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTUxLjAuMC4wIE1vYmlsZSBTYWZhcmkvNTM3LjM2IiwiZXhwIjoxNzg2MDEwNTU3LCJqdGkiOiI5Y2U3NDg5Zjk2MzRjNjJiIn0%3D.xwF8SuCFm335A5dAHY4C8jXAOR4K2fR0XApZggAR1l4%3D"

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

# 2. GRUP: Güncellenmiş Yedek Yayınlar
ictimaitv2_link = "https://str.yodacdn.net/ictimaitele/tracks-v1a1/mono.ts.m3u8?token=eyJpcCI6Ijg1LjEzMi4yNy4xODIiLCJ1YSI6Ik1vemlsbGEvNS4wIChNYWNpbnRvc2g7IEludGVsIE1hYyBPUyBYIDEwXzE1XzcpIEFwcGxlV2ViS2l0LzYwNS4xLjE1IChLSFRNTCwgbGlrZSBHZWNrbykgVmVyc2lvbi8xNy4zLjEgU2FmYXJpLzYwNS4xLjE1IiwiZXhwIjoxNzg1ODU0Mjc4LCJqdGkiOiI3MjhmZjgzOGE2OWY0YzIyIn0%3D.SVGB8xCW60QQlO23gP25hBeDJoHeJspZk7HfLMk2OBw%3D"
aztv2_link = "https://empty-fire-e7df.ipx2026.workers.dev/aztv"
medeniyyet2_link = "https://empty-fire-e7df.ipx2026.workers.dev/medeniyyet"
atv2_link = "https://empty-fire-e7df.ipx2026.workers.dev/atv"
bakutv2_link = "https://str.yodacdn.net/bakutv/tracks-v1a1/mono.ts.m3u8?token=eyJpcCI6Ijg1LjEzMi4yNy4xODIiLCJ1YSI6Ik1vemlsbGEvNS4wIChNYWNpbnRvc2g7IEludGVsIE1hYyBPUyBYIDEwXzE1XzcpIEFwcGxlV2ViS2l0LzYwNS4xLjE1IChLSFRNTCwgbGlrZSBHZWNrbykgVmVyc2lvbi8xNy4zLjEgU2FmYXJpLzYwNS4xLjE1IiwiZXhwIjoxNzg1ODU0Mjc4LCJqdGkiOiI3MjhmZjgzOGE2OWY0YzIyIn0%3D.SVGB8xCW60QQlO23gP25hBeDJoHeJspZk7HfLMk2OBw%3D"


# --- M3U LİSTESİ OLUŞTURMA ---

m3u_satirlari = [
    '#EXTM3U',
    
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
    '#EXTINF:-1 tvg-id="ARB24" tvg-logo="https://i.ibb.co/67DJBLqt/arb24.png" group-title="Azerbaijan",ARB 24',
    f"{arb24_link}",
    '#EXTINF:-1 tvg-id="ARBGunesh" tvg-logo="https://i.ibb.co/BHJ1vbr5/arbgunesh.png" group-title="Azerbaijan",ARB Gunesh',
    f"{arbgunesh_link}",
    '#EXTINF:-1 tvg-id="DunyaTV" tvg-logo="https://i.ibb.co/whNG1qY9/dunyatv.jpg" group-title="Azerbaijan",Dunya TV',
    f"{dunya_link}",
    '#EXTINF:-1 tvg-id="NaxcivanTV" tvg-logo="https://i.ibb.co/bgyrK5r2/NTV.png" group-title="Azerbaijan",Naxçıvan TV',
    f"{ntv_link}",
    '#EXTINF:-1 tvg-id="QafqazTV" tvg-logo="https://i.ibb.co/dsn5NM67/qafqaz-tv.png" group-title="Azerbaijan",Qafqaz TV',
    f"{qafqaz_link}",
    '#EXTINF:-1 tvg-id="APATV" tvg-logo="https://i.ibb.co/WNnQ0fw9/apatv.jpg" group-title="Azerbaijan",APA TV',
    f"{apatv_link}",
    '#EXTINF:-1 tvg-id="MTVAzerbaijan" tvg-logo="https://i.ibb.co/WvhWckLW/mtvaz.png" group-title="Azerbaijan",MTV Azerbaijan',
    f"{mtv_link}",
    '#EXTINF:-1 tvg-id="VIPHD" tvg-logo="https://i.ibb.co/WvY8zPt4/viphd.png" group-title="Azerbaijan",VIP HD',
    f"{vip_hd_link}",
    '#EXTINF:-1 tvg-id="KanalS" tvg-logo="https://i.ibb.co/RpgqMMct/Kanal-S.png" group-title="Azerbaijan",Kanal S',
    f"{kanals_link}",
    '#EXTINF:-1 tvg-id="CBCTV" tvg-logo="https://i.ibb.co/NgcJ7xPb/cbctv.png" group-title="Azerbaijan",CBC TV',
    f"{cbctv_link}",

    # --- MÜZİK VE DİĞER KANALLAR ---
    '#EXTINF:-1 tvg-id="AyazTV" tvg-logo="https://i.ibb.co/gNdFzTf/ayaztv.png" group-title="Azerbaijan",Ayaz TV',
    f"{ayaz_link}",
    '#EXTINF:-1 tvg-id="KNMusicTV" tvg-logo="https://i.ibb.co/BVwxFNfn/kntv.png" group-title="Azerbaijan",KN Music TV',
    f"{kn_music_link}",
    '#EXTINF:-1 tvg-id="ShowPlusTV" tvg-logo="https://i.ibb.co/nsS1GSMZ/showplus.png" group-title="Azerbaijan",Show Plus TV',
    f"{showplus_link}",
    '#EXTINF:-1 tvg-id="LivetvAZ" tvg-logo="https://i.ibb.co/cK9TKFJt/livetvaz.png" group-title="Azerbaijan",LivetvAZ',
    f"{livetvaz_link}",
    '#EXTINF:-1 tvg-id="KTV" tvg-logo="https://i.ibb.co/jkptgkwH/ktv.png" group-title="Azerbaijan",KTV',
    f"{ktv_link}",
    '#EXTINF:-1 tvg-id="FTV" tvg-logo="https://i.ibb.co/tMwJ0tBm/ftv.png" group-title="Azerbaijan",FTV',
    f"{ftv_link}",
    '#EXTINF:-1 tvg-id="DiginetCinema" tvg-logo="https://i.ibb.co/My64g8Fv/digi.png" group-title="Azerbaijan",Diginet Cinema',
    f"{diginet_link}",
    '#EXTINF:-1 tvg-id="ELTV" tvg-logo="https://i.ibb.co/5WV8sz7s/eltvaz.png" group-title="Azerbaijan",EL TV',
    f"{el_tv_link}",

    # --- YEDEK KANAL GRUBU ---
    '#EXTINF:-1 tvg-id="IctimaiTV2" tvg-logo="https://i.ibb.co/FbKMRyFz/itv2.jpg" group-title="Azerbaijan",Ictimai TV 2',
    f"{ictimaitv2_link}",
    '#EXTINF:-1 tvg-id="AZTV2" tvg-logo="https://i.ibb.co/dwNh0pyg/aztv.jpg" group-title="Azerbaijan",AZTV 2',
    f"{aztv2_link}",
    '#EXTINF:-1 tvg-id="MedeniyyetTV2" tvg-logo="https://i.ibb.co/B5BtPZLd/medeniyyet.jpg" group-title="Azerbaijan",Medeniyyet TV 2',
    f"{medeniyyet2_link}",
    '#EXTINF:-1 tvg-id="AzadAzerbaycanTV2" tvg-logo="https://i.ibb.co/rDHp5Fk/azad.png" group-title="Azerbaijan",Azad Azerbaycan TV 2',
    f"{atv2_link}",
    '#EXTINF:-1 tvg-id="RealTV2" tvg-logo="https://i.ibb.co/Rpk9CspD/realtv.jpg" group-title="Azerbaijan",Real TV 2',
    f"{real2_link}",
    '#EXTINF:-1 tvg-id="XezerTV2" tvg-logo="https://i.ibb.co/q3BGCK8n/xezer.png" group-title="Azerbaijan",Xezer TV 2',
    f"{xezer2_link}",
    '#EXTINF:-1 tvg-id="BakuTV2" tvg-logo="https://i.ibb.co/zWSLHdDt/bakutv.jpg" group-title="Azerbaijan",Baku TV 2',
    f"{bakutv2_link}",
    '#EXTINF:-1 tvg-id="SpaceTV2" tvg-logo="https://i.ibb.co/jpX0Z9v/spacetvv.png" group-title="Azerbaijan",Space TV 2',
    f"{spacetv2_link}",
    '#EXTINF:-1 tvg-id="ARBHD2" tvg-logo="https://i.ibb.co/fY05FcdF/arbhd.jpg" group-title="Azerbaijan",ARB HD 2',
    f"{arbhd2_link}"
]

m3u_yapisi = "\n".join(m3u_satirlari)

with open("listem.m3u", "w", encoding="utf-8") as f:
    f.write(m3u_yapisi)

print("Show Plus TV ve Diginet Cinema eklendi. Toplam 38 kanallı listem.m3u hazır!")
