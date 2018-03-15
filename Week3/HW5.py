import timeit
def app(str):
    arr = ['ext', 'app']
    arr2=[]
    a=len(str)
    for i in range(a):
        arr2.append(str[i])
    arr.append(arr2)
    return arr
def ext(str):
    arr = ['ext', 'app']
    arr2 = []
    a=len(str)
    for i in range(a):
        arr2.extend(str[i])
    arr.extend(arr2)
    return arr
data=input("Bir şeyler giriniz : ")
print(app(data))
print(ext(data))
start_time = timeit.default_timer()
app(data)
print(timeit.default_timer() - start_time)
start_time = timeit.default_timer()
ext(data)
print(timeit.default_timer() - start_time)

