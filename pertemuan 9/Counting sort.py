#Implement Counting Sort in Python
#Menerapkan Menghitung Jenis dalam Python
#Counting Sort adalah algoritma pengurutan yang efisien untuk mengurutkan elemen-elemen dalam sebuah daftar, terutama ketika elemen-elemen tersebut berada dalam rentang nilai yang terbatas. Algoritma ini bekerja dengan menghitung jumlah kemunculan setiap elemen dalam daftar dan kemudian menggunakan informasi tersebut untuk menentukan posisi akhir dari setiap elemen dalam daftar yang sudah terurut.
#Berikut adalah implementasi Counting Sort dalam Python:
#buat sendiri algoritma counting sort

def counting_sort(arr):
    if not arr:
        return arr

    max_val = max(arr)
    count = [0] * (max_val + 1)

    for num in arr:
        count[num] += 1

    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])

    return sorted_arr
# Contoh penggunaan
mylist = [4, 2, 2, 6, 3, 
    3, 1, 6, 5, 2, 3]
sorted_list = counting_sort(mylist)
print(sorted_list)
#Solusi yang Lebih Baik
#Implementasi Counting Sort yang lebih efisien dengan menggunakan array untuk menyimpan hasil akhir
def counting_sort_efficient(arr):
    if not arr:
        return arr

    max_val = max(arr)
    count = [0] * (max_val + 1)

    for num in arr:
        count[num] += 1

    index = 0
    for i in range(len(count)):
        while count[i] > 0:
            arr[index] = i
            index += 1
            count[i] -= 1

    return arr
# Contoh penggunaan
mylist = [4, 2, 2, 6, 3,
    3, 1, 6, 5, 2, 3]
sorted_list = counting_sort_efficient(mylist)
print(sorted_list)

#w3school

def countingSort(arr):
  max_val = max(arr)
  count = [0] * (max_val + 1)

  while len(arr) > 0:
    num = arr.pop(0)
    count[num] += 1

  for i in range(len(count)):
    while count[i] > 0:
      arr.append(i)
      count[i] -= 1

  return arr

mylist = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
mysortedlist = countingSort(mylist)
print(mysortedlist)

