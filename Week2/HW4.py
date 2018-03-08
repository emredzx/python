x = input("Lütfen Bir Kelime Giriniz : ")
length = len(x)
y = 0
while y < length / 2 + 1:
    if x[y] != x[-y - 1]:
        print("Girdiğiniz Kelime Polindrom Değildir.")
        break
    y += 1
else:
    print("Girdiğiniz Kelime Polindromdur.")