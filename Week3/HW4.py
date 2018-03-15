def rev(str):
  x=len(str)
  arr=[]
  for i in range(x):
    arr.append(str[i])
  ort=x/2
  ort=int(ort)
  for i in range (0,ort):
    arr[i], arr[0 - (i + 1)] = arr[0 - (i + 1)] , arr[i]
  arr="".join(arr)
  return arr
klm=input("Bir kelime giriniz : ")
print(rev(klm))
