# List
List_Barang = ["esp32", "arduino", "raspberry"]

print("Isi List:")
for i in range(len(List_Barang)):
    print(i, "-", List_Barang[i])

print()

# While
n = 15

while n > 10:
    print("Saya Komjar")
    n -= 1

print()

# Range
x = range(3, 20, 2)

for n in x:
    print(n)