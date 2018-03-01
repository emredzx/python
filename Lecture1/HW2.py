sira = int(input("Fibonacci sırası giriniz : "))

s1 = 0
s2 = 1
sayac = 1

if sira <= 0:
 print("0 ve daha küçük değerler girilemez..")

else:
    while sayac < sira:
       s3 = s1 + s2
       s1 = s2
       s2 = s3
       sayac += 1

    print("Fibonacci sırası",sira,", Sonucu",":",s1)