def indirim_hesapla():
  indirimsiz_tutar = float(input("Aldiginiz urunun indirimsiz tutarini giriniz:"))
  indirim_orani = float(input("Indirim orani nedir %? "))
  indirim_tutari = float(indirimsiz_tutar*(indirim_orani/100))
  son_fiyat = (indirimsiz_tutar - indirim_tutari)
  print(f"Aldiginiz urunun indirimli fiyati: {son_fiyat} TL.")


indirim_hesapla()
