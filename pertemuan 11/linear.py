#soal 1

pasien = [
    "Budi Santoso", "Siti Rahayu", "Ahmad Fauzi", "Dewi Lestari",
    "Eko Prasetyo", "Fitri Handayani", "Gilang Ramadan", "Hana Pertiwi",
    "Irfan Maulana", "Joko Susilo"
]

def linearSearch(arr, targetVal):
    for i in range(len(arr)):
        if arr[i] == targetVal:
            return i
        return -1
    
pasien = ["Budi Santoso", "Siti Rahayu", "Ahmad Fauzi", "Dewi Lestari",
         "Eko Prsetyo", "Fitri Handayani", "Gilang Ramadan", "Hana Pertiwi:,"
          "Irfan Maulana", "Joko Susilo"
]
targetVal = input("Masukkan nama pasien yang dicari: ")

result = linearSearch(pasien, targetVal)

if result != -1:
    print (f"pasien ditemukan pada index {result}")
else:
    print("pasien tidak ditemukan")



#soal 2

id_karyawan = [
1021, 1045, 1089, 1102, 1157, 1203, 1245, 1312,
1378, 1401, 1456, 1502, 1567, 1634, 1700
]

def binarySearch(arr, targetVal):
    left = 0
    right = len(arr) -1

    while left <= right:
        mid = (left + right)// 2

        if arr[mid] == targetVal:
            return mid
        
        if arr[mid] < targetVal:
            left = mid + 1
        else:
            right = mid - 1

    return -1

id_karyawan = [
1021, 1045, 1089, 1102, 1157, 1203, 1245, 1312,
1378, 1401, 1456, 1502, 1567, 1634, 1700
]

result = binarySearch(id_karyawan, 1245)

if result != -1:
    print(f"ID karyawan ditemukan pada index {result}")
else:
    print("id karyawan tidak ditemukan")


#soal 3

rak_a = ["BK-045", "BK-012", "BK-078", "BK-033", "BK-091",
"BK-027", "BK-056"]
rak_b = ["BK-011", "BK-023", "BK-035", "BK-047", "BK-059",
"BK-071", "BK-083", "BK-095"]

def linearSearch(arr, targetVal):
    for i in range(len(arr)):
        if arr[i] == targetVal:
            return i
    return -1

rak_a = ["Bk-045", "Bk-012", "bK-078", "BK-033", "BK-091",
         "BK-027", "BK-056"]
x = input("Masukkan kode buku yang dicari: ")

result = linearSearch(rak_a, x)

if result != -1:
    print(f"Buku ditemukan pada index {result} di rak A")
else:
    result = linearSearch(rak_b, x)
    if result != -1:
        print(f"Buku ditemukan pada index {result} di rak A")
    else:
        print("Buku tidak ditemukan di rak A maupun rak B")

def binarySearch(arr, targetVal):
    left = 0
    right = len(arr) -1

    while left <= right:
        mid = (left + right)// 2

        if arr[mid] == targetVal:
            return mid
        
        if arr[mid] < targetVal:
            left = mid + 1
        else:
            right = mid - 1

    return -1

rak_b = ["BK-011", "BK-023", "BK-035", "BK-047", "BK-059",
         "BK-071", "BK-083", "BK-095"
        ]
x = input("Masukkan kode buku yang dicari: ")
result = binarySearch(rak_b, x)

if result != -1:
    print(f"Buku ditemukan pada index {result+1} di rak B")
else:
    result = binarySearch(rak_b, x)
    if result != -1:
        print(f"Buku ditemukan pada index {result+1} di rak B")
    else:
        print("Buku tidak ditemukan di rak A maupun rak B")
