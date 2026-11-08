from datetime import datetime

def vize_sayaci():
    print("Lütfen sınav tarih ve saatini şu formatta giriniz:")
    print("Örnek: 2026-06-15 14:30 (Yıl-Ay-Gün Saat:Dakika)\n")
    
    while True:
        giris = input("Sınav tarih ve saati: ")
        try:

            sinav_tarihi = datetime.strptime(giris, "%Y-%m-%d %H:%M")
            simdiki_zaman = datetime.now()

            if sinav_tarihi < simdiki_zaman:
                print("⚠️ Girdiğiniz tarih geçmişte kaldı! Lütfen gelecekteki bir tarihi girin.")
                continue
            
            fark = sinav_tarihi - simdiki_zaman
            
            toplam_saniye = int(fark.total_seconds())
            gun = int(toplam_saniye / 86400)         
            kalan_saniye = int(toplam_saniye % 86400)
            saat = int(kalan_saniye / 3600)       
            dakika = int((kalan_saniye % 3600)/60)
    
            print(f"⏳ **{gun} gün, {saat} saat ve {dakika} dakika** kaldı. ")
            break
            
        except ValueError:
            print("❌ Hatalı format! Lütfen tarihi 'YYYY-AA-GG SS:DD' formatında girdiğinizden emin olun (Örn: 2026-06-15)")


vize_sayaci()
