e = int(input("Aralık giriniz. : "))
if (e == 0):
    print("Aralık 0 girilemez..")
else:
    for x in range(0, e):
        print("Kullanıcının Girmiş Olduğu 2 Sayı Üzerinde 4 İşlem Yapabilen Uygulama")
        sayi1 = int(input("1. Sayıyı Giriniz : "))
        sayi2 = int(input("2. Sayıyı Giriniz : "))
        islem = input("İşlem Seçiniz : {Toplama (+) - Çıkarma (-) - Çarpma (*) - Bölme(/) : ")

        if (islem == "+"):
            toplam = sayi1 + sayi2
            print("Toplam : ", toplam)

        elif (islem == "-"):
            fark = sayi1 - sayi2
            print("Kalan : ", fark)

        elif (islem == "*"):

            carp = sayi1 * sayi2
            print("Kalan : ", carp)

        elif (islem == "/"):
            if (sayi2 == 0):
                print("Bölmede 2.sayı 0 girilemez..")
            else:
                bol = sayi1 // sayi2
                print("Bölüm : ", bol)

        elif (islem == "exit"):
            break

        else:
            print("Bir işlem seçiniz...")
