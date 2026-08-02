import requests
import re

# Web istekleri için kullanılacak varsayılan header
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# ==============================================================================
# SİTELERDEN YALNIZCA TAZE M3U8 LİNKİ ÇEKEN SADELEŞTİRİLMİŞ FONKSİYON
# ==============================================================================

def taze_link_cek(url, regex_pattern=r'(https?://[^\s"\']+\.m3u8[^\s"\']*)'):
    """
    Sadece belirtilen URL'ye gider ve M3U8 adresini arar.
    Bulursa taze linki döndürür, bulamazsa None döner (Yedek link kullanmaz).
    """
    try:
        response = requests.get(url, headers=headers, timeout=10)
        linkler = re.findall(regex_pattern, response.text)
        if linkler:
            temiz_link = linkler[0].replace('\\/', '/')
            print(f"[BAŞARILI] {url} -> Taze link çekildi.")
            return temiz_link
    except Exception as e:
        print(f"[UYARI] {url} adresinden link çekilemedi: {e}")
    
    return None


# 1. Otomatik Çekilen Bağımsız Kanallar
itv_link = taze_link_cek("https://live.itv.az/")
cbc_link = taze_link_cek("https://cbcsport.az/live/")
atv_link = taze_link_cek("https://atv.az/live")
baku_link = taze_link_cek("https://baku.tv/live")
kanals_link = taze_link_cek("https://kalons.az/live")
ayaz_link = taze_link_cek("https://ayaztv.az/")
dunya_link = taze_link_cek("https://dunyatv.az/live")
kn_music_link = taze_link_cek("https://kntv.az/")
ftv_link = taze_link_cek("https://ftv.az/")

# Sabit M3U8 Linkli Kanallar
show_plus_link = "https://rtmp.showplus.tv/hls/myshow.m3u8"


# ==============================================================================
# YODACDN VE DİĞER SABİT GRUP TANIMLAMALARI
# ==============================================================================

# YodaCDN Tekil Token Yönetimi
guncel_token = "eyJpcCI6IjkyLjM5Ljk0LjIwMyIsInVhIjoiTW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDEwOyBLKSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvNTUwLjAuMC4wIE1vYmlsZSBTYWZhcmkvNTM3MzYiLCJleHAiOjE3ODUzMjg0MzAsImp0aSI6ImZiZDg5YzU3YWFiNTU4NzcifQ%3D%3D.jhtyuuhYTshosf67e+loVyrtIMrjc7az%2F0gAb9BzjmY%3D"

# YodaCDN Akışları
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

# YodaCDN Yedek Grubu
aztv2_link = f"https://str.yodacdn.net/azertv/tracks-v1a1/mono.ts.m3u8?token={guncel_token}"
medeniyyet2_link = f"https://str2.yodacdn.net/medeniyyettele/tracks-v3a1/mono.ts.m3u8?token={guncel_token}"
idman2_link = f"https://str2.yodacdn.net/idmantele/tracks-v1a1/mono.ts.m3u8?token={guncel_token}"
real2_link = f"https://str.yodacdn.net/real/mono.m3u8?token={guncel_token}"
xezer2_link = "https://xezerxeber.az/stream/main_stream.m3u8"
azad2_link = f"https://str.yodacdn.net/atv/tracks-v1a1/mono.ts.m3u8?token={guncel_token}"
space2_link = f"https://str.yodacdn.net/space/mono.m3u8?token={guncel_token}"
arb2_link = f"https://str.yodacdn.net/arb/tracks-v1a1/mono.ts.m3u8?token={guncel_token}"
cbctv2_link = f"https://str.yodacdn.net/cbc/tracks-v1a1/mono.ts.m3u8?token={guncel_token}"


# ==============================================================================
# M3U LİSTESİ OLUŞTURMA
# ==============================================================================

m3u_satirlari = ['#EXTM3U']

# Yardımcı Sözlük: Siteden Çekilen ve Sabit Kanallar
dinamik_kanallar = [
    ("ITV", "https://i.ibb.co/dsfZQ0Cq/itv.png", "İctimai TV", itv_link),
    ("CBCSport", "https://i.ibb.co/pBpdbm2j/cbcs.png", "CBC Sport", cbc_link),
    ("AzadAzerbaycanTV", "https://i.ibb.co/rDHp5Fk/azad.png", "Azad Azerbaycan TV", atv_link),
    ("BakuTV", "https://i.ibb.co/23N9F7s8/bakutvv.png", "Baku TV", baku_link),
    ("KanalS", "https://i.ibb.co/RpgqMMct/Kanal-S.png", "Kanal S", kanals_link),
    ("DunyaTV", "https://i.ibb.co/whNG1qY9/dunyatv.jpg", "Dunya TV", dunya_link),
    ("AyazTV", "https://i.ibb.co/gNdFzTf/ayaztv.png", "Ayaz TV", ayaz_link),
    ("ShowPlusTV", "https://i.ibb.co/nsS1GSMZ/showplus.png", "Show Plus TV", show_plus_link), # Ayaz TV'den sonra eklendi
    ("KNMusicTV", "https://i.ibb.co/BVwxFNfn/kntv.png", "KN Music TV", kn_music_link),
    ("FTV", "https://i.ibb.co/tMwJ0tBm/ftv.png", "FTV", ftv_link),
]

# Dinamik ve Sabit Bağımsız Kanalları Listeye Ekle
for tvg_id, logo, isim, link in dinamik_kanallar:
    if link:
        m3u_satirlari.append(f'#EXTINF:-1 tvg-id="{tvg_id}" tvg-logo="{logo}" group-title="Azerbaijan",{isim}')
        m3u_satirlari.append(link)

# YodaCDN Ana Kanalları
yoda_kanallari = [
    ('AzTV', 'https://i.ibb.co/dwNh0pyg/aztv.jpg', 'AzTV', aztv_link),
    ('MedeniyyetTV', 'https://i.ibb.co/B5BtPZLd/medeniyyet.jpg', 'Medeniyyet TV', medeniyyet_link),
    ('IdmanTV', 'https://i.ibb.co/pBNzbCWD/idmanv.jpg', 'İdman TV', idman_link),
    ('RealTV', 'https://i.ibb.co/Rpk9CspD/realtv.jpg', 'Real TV', real_link),
    ('XezerTV', 'https://i.ibb.co/q3BGCK8n/xezer.png', 'Xezer TV', xezer_link),
    ('SpaceTV', 'https://i.ibb.co/v49CGvL2/spacetv.jpg', 'Space TV', space_link),
    ('ARBHD', 'https://i.ibb.co/fY05FcdF/arbhd.jpg', 'ARB HD', arb_link),
    ('NaxcivanTV', 'https://i.ibb.co/bgyrK5r2/NTV.png', 'Naxçıvan TV', ntv_link),
    ('QafqazTV', 'https://i.ibb.co/dsn5NM67/qafqaz-tv.png', 'Qafqaz TV', qafqaz_link),
    ('APATV', 'https://i.ibb.co/WNnQ0fw9/apatv.jpg', 'APA TV', apatv_link),
]

for tvg_id, logo, isim, link in yoda_kanallari:
    m3u_satirlari.append(f'#EXTINF:-1 tvg-id="{tvg_id}" tvg-logo="{logo}" group-title="Azerbaijan",{isim}')
    m3u_satirlari.append(link)

# YodaCDN Yedek Grubu
yedek_kanallar = [
    ('AZTV2', 'https://i.ibb.co/dwNh0pyg/aztv.jpg', 'AZTV 2', aztv2_link),
    ('MedeniyyetTV2', 'https://i.ibb.co/B5BtPZLd/medeniyyet.jpg', 'Medeniyyet TV 2', medeniyyet2_link),
    ('IdmanTV2', 'https://i.ibb.co/pBNzbCWD/idmanv.jpg', 'IdmanTV 2', idman2_link),
    ('RealTV2', 'https://i.ibb.co/Rpk9CspD/realtv.jpg', 'Real TV 2', real2_link),
    ('XezerTV2', 'https://i.ibb.co/q3BGCK8n/xezer.png', 'Xezer TV 2', xezer2_link),
    ('AzadAzerbaycan2', 'https://i.ibb.co/rDHp5Fk/azad.png', 'Azad Azerbaycan 2', azad2_link),
    ('SpaceTV2', 'https://i.ibb.co/v49CGvL2/spacetv.jpg', 'Space TV 2', space2_link),
    ('ARB2', 'https://i.ibb.co/fY05FcdF/arbhd.jpg', 'ARB 2', arb2_link),
    ('CBCTV2', 'https://i.ibb.co/mVjVMH0J/cbcaz.png', 'CBCTV 2', cbctv2_link),
]

for tvg_id, logo, isim, link in yedek_kanallar:
    m3u_satirlari.append(f'#EXTINF:-1 tvg-id="{tvg_id}" tvg-logo="{logo}" group-title="Azerbaijan",{isim}')
    m3u_satirlari.append(link)

# Dosyayı Yazma
m3u_yapisi = "\n".join(m3u_satirlari)

with open("listem.m3u", "w", encoding="utf-8") as f:
    f.write(m3u_yapisi)

print("Show Plus TV eklendi ve listem.m3u güncellendi!")
