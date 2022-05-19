import random

k1 = []
for x in range(1000):
    k1.append(random.randint(1, 1000))


k2 = []
for y in range(2000):
    k2.append(random.randint(1, 2000))


k3 = []
for z in range(3000):
    k3.append(random.randint(1, 3000))


def bubbleSort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


print("k1 desordenado:")
for i in range(len(k1)):
    print("% d" % k1[i], end=" ")

bubbleSort(k1)

print("\nk1 ordenado:")
for i in range(len(k1)):
    print("% d" % k1[i], end=" ")

print("\nk2 desordenado:")
for i in range(len(k2)):
    print("% d" % k2[i], end=" ")

bubbleSort(k2)

print("\nk2 ordenado:")
for i in range(len(k2)):
    print("% d" % k2[i], end=" ")

print("\nk3 desordenado:")
for i in range(len(k3)):
    print("% d" % k3[i], end=" ")

bubbleSort(k3)

print("\nk3 ordenado:")
for i in range(len(k3)):
    print("% d" % k3[i], end=" ")


k1 = []
print("\nk1 vacio:")
for i in range(len(k1)):
    print("% d" % k1[i], end=" ")



