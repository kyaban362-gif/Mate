def harf_notu_hesapla():
    vize = int(input("Vize notu:"))
    final = int(input("Final notu:"))
    ortalama = float(vize*40/100 + final*60/100)

    if(ortalama >=90):
            harf_notu = "AA"
    elif(ortalama >=80):
            harf_notu = "BA"
    elif(ortalama >=70):
            harf_notu = "BB"
    elif(ortalama >=60):
            harf_notu = "CB"
    elif(ortalama >=50):
               harf_notu = "CC"
    elif(ortalama >=40):
               harf_notu = "DC"
    elif(ortalama >=30):
               harf_notu = "DD"
    else:
            harf_notu = "FF"
    print(f"Harf notun {harf_notu}")

harf_notu_hesapla()
