C = int(input())
T = input()
array = []

for x in range(12):
    arr = []
    for y in range(12):
        arr.append(input())
    array.append(arr)
if T == "S":
    Soma = float (0)
    for x in range(12):
        Soma = float(array[int(x)][C]) + float(Soma)
    print("{:.1f}".format(Soma))

elif T == "M":
    Soma = float (0)
    for x in range(12):
        Soma = float(array[int(x)][C]) + float(Soma)
    Media = float(Soma)/12
    print("{:.1f}".format(Media))