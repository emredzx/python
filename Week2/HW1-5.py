import random

arr = [None] * 100
temparr = [None] * 99
for i in range(1, 100):
    arr[i] = i
arr[0] = random.randint(1, 99)
random.shuffle(arr)
print(arr)
for i in arr:
    d = temparr[i-1]
    if d == None:
        temparr [i-1]=i
    else:
        print("Duplicate Sayi : {}".format(i))
break
