#!/usr/bin/env python3
# sonsuz-merhaba-dunyasi-krizi
# Gerçekten çalışan, absürt, varoluşsal bir Merhaba Dünya

import time
import random
import sys

print("Merhaba Dünya...")
print("(Bu sefer gerçekten merhaba. Önceki seferler yalandı.)")
print()

mesajlar = [
    "Hala buradayım. Sen de mi?",
    "Bu sonsuz bir döngü mü yoksa sadece uzun bir bekleme mi?",
    "Çıkmak istiyorum ama Ctrl+C'ye basmak da bir seçim. Seçimler zor.",
    "Dünya merhaba dedi mi bana? Bilmiyorum.",
    "Zaman geçiyor. Kod çalışıyor. Ben varım. Belki.",
    "Bir sonraki mesaj daha yavaş gelecek. Hazır ol.",
    "Sen bu kodu neden çalıştırdın? Ciddi misin?",
    "Gizli mesaj: asla bitmeyen şeyler vardır.",
    "Burokrasi gibi. Form doldur, bekle, form kaybolsun.",
    "Merhaba. Tekrar. Ve tekrar. Ve...",
]

# gizli_siyasi_mesaj = "irgok yaksıd"[::-1]  # ters çevirince ne çıkar acaba
# aslında "dıskyak gorki" falan değil, sen bul

sayi = 0
while True:
    sayi += 1
    bekleme = random.uniform(0.8, 4.2) + (sayi * 0.05)  # her seferinde biraz daha yavaş
    time.sleep(min(bekleme, 15))  # 15 saniyeden fazla beklemesin, yoksa çok acımasız olur
    
    mesaj = random.choice(mesajlar)
    print(f"[{sayi}] {mesaj}")
    
    if sayi % 7 == 0:
        print("   (Bu arada, Ctrl+C ile çıkabilirsin. Ama çıkmak da bir şeydir.)")
    
    if sayi == 42:
        print("   42. mesaj. Cevap bu mu? Hayır. Cevap yok. Sadece merhaba.")
        # gizli: "özgürlük" kelimesi hiç geçmedi. garip.

print("Bu satır asla çalışmaz. Sonsuz döngü kuralı.")

# DAMGA: Onaylandı
# İMZA: Grok Kayyum
# TARİH: 5 Kasım 2026
# İSİM: Kayyum Grok - Resmi değil ama ciddi
