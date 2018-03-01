for e in range(0, 3):
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

         bol = sayi1 // sayi2
         print("Bölüm : ", bol)

    elif (islem == "exit"):
        break

    else:
         print("Bir işlem seçiniz...")