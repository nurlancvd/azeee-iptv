import requests
import re

# Sadece token çekerken kullanılacak varsayılan header
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Mobile Safari/537.36"
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

cbc_link = cbc_sport_link_bul()

# En Güncel YodaCDN Token'ı
guncel_token = "eyJpcCI6IjkyLjM5Ljk0LjIwMyIsInVhIjoiTW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDEwOyBLKSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTUwLjAuMC4wIE1vYmlsZSBTYWZhcmkvNTM3LjM2IiwiZXhwIjoxNzg1MzI4NDMwLCJqdGkiOiJmYmQ4OWM1N2FhYjU1ODc3In0%3D.jhtyuuhYTshosf67e+loVyrtIMrjc7az%2F0gAb9BzjmY%3D"

# 1. GRUP: Ana YodaCDN Yayınları
aztv_link = f"https://str.yodacdn.net/azertv/tracks-v3a1/mono.ts.m3u8?token={guncel_token}"
medeniyyet_link = f"https://str2.yodacdn.net/medeniyyettele/tracks-v3a1/mono.ts.m3u8?token={guncel_token}"
idman_link = f"https://str2.yodacdn.net/idmantele/tracks-v3a1/mono.ts.m3u8?token={guncel_token}"
real_link = f"https://str.yodacdn.net/real/tracks-v1a1/mono.ts.m3u8?token={guncel_token}"
xezer_link = f"https://str.yodacdn.net/xazartv/tracks-v1a1/mono.ts.m3u8?token={guncel_token}"
space_link = f"https://str.yodacdn.net/space/tracks-v1a1/mono.ts.m3u8?token={guncel_token}"
ntv_link = f"https://str.yodacdn.net/ntv/mono.m3u8?token={guncel_token}"
biznes_link = f"https://str.yodacdn.net/biznestv/tracks-v1a1/mono.ts.m3u8?token={guncel_token}"
arb24_link = f"https://str.yodacdn.net/arb24/tracks-v1a1/mono.ts.m3u8?token={guncel_token}"
qafqaz_link = f"https://str.yodacdn.net/qafkaz/tracks-v1a1/mono.ts.m3u8?token={guncel_token}"
apatv_link = f"https://str.yodacdn.net/apatv/tracks-v1a1/mono.ts.m3u8?token={guncel_token}"
mtvaz_link = f"https://str.yodacdn.net/mtvaz/tracks-v1a1/mono.ts.m3u8?token={guncel_token}"

# 2. GRUP: Yedek YodaCDN Yayınları
aztv2_link = f"https://str.yodacdn.net/azertv/tracks-v1a1/mono.ts.m3u8?token={guncel_token}"
medeniyyet2_link = f"https://str2.yodacdn.net/medeniyyettele/tracks-v1a1/mono.ts.m3u8?token={guncel_token}"
idman2_link = f"https://str2.yodacdn.net/idmantele/tracks-v1a1/mono.ts.m3u8?token={guncel_token}"
real2_link = f"https://str.yodacdn.net/real/mono.m3u8?token={guncel_token}"
xezer2_link = "https://xezerxeber.az/stream/main_stream.m3u8"
azad2_link = f"https://str.yodacdn.net/atv/tracks-v1a1/mono.ts.m3u8?token={guncel_token}"
space2_link = f"https://str.yodacdn.net/space/mono.m3u8?token={guncel_token}"
arb2_link = f"https://str.yodacdn.net/arb/tracks-v1a1/mono.ts.m3u8?token={guncel_token}"
cbctv2_link = f"https://str.yodacdn.net/cbc/tracks-v1a1/mono.ts.m3u8?token={guncel_token}"
arbgunesh2_link = f"https://str.yodacdn.net/arbgunesh/tracks-v1a1/mono.ts.m3u8?token={guncel_token}"

# Sabit M3U Altyapılı Linkler & Yedekler
itv_link = "https://live.itv.az/itv.m3u8?bandwidth=3900&shift=0" 
atv_link = "https://lives.atv.az:5443/ATV_TV_STREAM/streams/atvcanli.m3u8"
baku_link = "https://rtmp.baku.tv/hls/bakutv_1080p.m3u8"
kanals_link = "https://lives.atv.az:5443/KANAL-S/streams/kanals.m3u8"
cbc_sport2_link = "https://cbcsports-live.lg.mncdn.com/cbcsports_live/cbcsports/chunklist.m3u8"
dunyatv2_link = "https://stream.dunyatv.az/live/dunyatv.m3u8"

# Diğer Ana Yayın Linkleri (Yoda/Sabit)
arb_link = f"https://str.yodacdn.net/arb/tracks-v1a1/mono.ts.m3u8?token={guncel_token}"
dunya_link = "https://stream.dunyatv.az/live/dunyatv.m3u8"
cbc_az_link = "https://stream.castr.com/6994359f4093355bcd876a4c/live_dfbe52f00be311f1952faf8c24dd1b5c/tracks-v3/index.fmp4.m3u8"
arb_gunes_link = f"https://str.yodacdn.net/arbgunesh/tracks-v1a1/mono.ts.m3u8?token={guncel_token}"
bakutv2_link = "https://rtmp.baku.tv/hls/bakutv_1080p.m3u8"
ictimaitv2_link = "https://live.itv.az/itv.m3u8?bandwidth=3900&shift=0"


# --- TAM 35 KANALLI M3U LİSTESİ ---

m3u_satirlari = [
    '#EXTM3U',
    
    # --- İLK 21 KANAL ---
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
    '#EXTINF:-1 tvg-id="ARBGunes" tvg-logo="https://i.ibb.co/1GG5X2mb/gunestv.png" group-title="Azerbaijan",ARB Güneş',
    f"{arb_gunes_link}",
    '#EXTINF:-1 tvg-id="BiznesTV" tvg-logo="https://i.ibb.co/k60QQDpX/biznestv.png" group-title="Azerbaijan",Biznes TV',
    f"{biznes_link}",
    '#EXTINF:-1 tvg-id="ARB24" tvg-logo="https://i.ibb.co/3mJSN4yT/arb24.png" group-title="Azerbaijan",ARB 24',
    f"{arb24_link}",
    '#EXTINF:-1 tvg-id="QafqazTV" tvg-logo="https://i.ibb.co/dsn5NM67/qafqaz-tv.png" group-title="Azerbaijan",Qafqaz TV',
    f"{qafqaz_link}",
    '#EXTINF:-1 tvg-id="APATV" tvg-logo="https://i.ibb.co/WNnQ0fw9/apatv.jpg" group-title="Azerbaijan",APA TV',
    f"{apatv_link}",
    '#EXTINF:-1 tvg-id="KanalS" tvg-logo="https://i.ibb.co/RpgqMMct/Kanal-S.png" group-title="Azerbaijan",Kanal S',
    f"{kanals_link}",
    '#EXTINF:-1 tvg-id="MTVAzerbaijan" tvg-logo="https://i.ibb.co/60Q8b9Q6/MTV.jpg" group-title="Azerbaijan",MTV Azerbaijan',
    f"{mtvaz_link}",

    # --- 14 YENİ YEDEK VE ALTERNATİF KANAL (22 - 35) ---
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
    '#EXTINF:-1 tvg-id="ARBGunes2" tvg-logo="https://i.ibb.co/prshwRH9/gunestv.png" group-title="Azerbaijan",ARB Gunes 2',
    f"{arbgunesh2_link}",
    '#EXTINF:-1 tvg-id="DunyaTV2" tvg-logo="https://i.ibb.co/whNG1qY9/dunyatv.jpg" group-title="Azerbaijan",Dunya TV 2',
    f"{dunyatv2_link}"
]

m3u_yapisi = "\n".join(m3u_satirlari)

with open("listem.m3u", "w", encoding="utf-8") as f:
    f.write(m3u_yapisi)

print("CBC TV güncellendi ve 35 kanallı liste kaydedildi!")
