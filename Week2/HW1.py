import random
arr = [None] * 100
for i in range(1, 100):
    arr[i] = i
arr[0] = random.randint(1, 99)
random.shuffle(arr)
print(arr)
tp = 0
for i in arr:
    tp = tp + i
rs = tp - 4950
print("Tekrar Eden Sayı :", rs)