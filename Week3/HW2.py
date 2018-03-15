s = input("Bir kelime giriniz : ")
s = s.lower()
tmp=[None]*len(s)
i=0
for c in s:
    print(c)
    varmi=False
    for j in range(len(s)):
        k=tmp[j]
        if c==k:
            varmi=True
    if varmi == False:
        tmp[i]=c
        i = i+1
print(tmp)
