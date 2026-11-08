while True:
    try:
        sayi = int(input("Lütfen bir sayı giriniz: "))
        print(f"Girdiğiniz sayı: {sayi}")
        break
        
    except ValueError:
        print("Lütfen geçerli bir sayı giriniz.")
