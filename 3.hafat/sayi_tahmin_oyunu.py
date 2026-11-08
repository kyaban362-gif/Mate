import random

def sayi_tahmin_oyunu():
    print("1 ile 100 arasında bir sayı tuttum. Tahmin etmeyi dene?\n")
    
    tutulan_sayi = random.randint(1, 100)
    deneme_sayisi = 0
    
    while True:
        try:            
            tahmin = int(input("Tahmininiz nedir? "))
            deneme_sayisi += 1

            if tahmin < 1 or tahmin > 100:
                print("⚠️ Lütfen 1 ile 100 arasında bir sayı girin.")
                continue
            if tahmin < tutulan_sayi:
                print("📈 Yukarı çık! Daha büyük bir sayı söyle.")
            elif tahmin > tutulan_sayi:
                print("📉 Aşağı in! Daha küçük bir sayı söyle.")
            else:
                print(f"\n🎉 Tebrikler! {tutulan_sayi} sayısını {deneme_sayisi}. denemede bildin!")
                break
                
        except ValueError:
            print("❌ Lütfen geçerli bir tam sayı giriniz.")
sayi_tahmin_oyunu()
