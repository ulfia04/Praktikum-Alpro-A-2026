#Implement Quicksort in Python
#Menerapkan Quicksort dalam Python
#Quicksort adalah algoritma pengurutan yang efisien dan banyak digunakan. Algoritma ini bekerja dengan memilih elemen sebagai pivot dan membagi array menjadi dua bagian berdasarkan pivot tersebut. Elemen yang lebih kecil dari pivot ditempatkan di sebelah kiri, sementara elemen yang lebih besar ditempatkan di sebelah kanan. Proses ini kemudian diulang secara rekursif pada kedua bagian hingga seluruh array terurut.
#Berikut adalah implementasi Quicksort dalam Python:
#buat sendiri algoritma quicksort

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]  # Memilih pivot sebagai elemen tengah
        left = [x for x in arr if x < pivot]  # Elemen yang lebih kecil dari pivot
        middle = [x for x in arr if x == pivot]  # Elemen yang sama dengan pivot
        right = [x for x in arr if x > pivot]  # Elemen yang lebih besar dari pivot
        return quicksort(left) + middle + quicksort(right)  # Rekursif pada bagian kiri dan kanan
# Contoh penggunaan
mylist = [64, 34, 25, 12, 22, 11, 90, 5]
sorted_list = quicksort(mylist)
print(sorted_list)
#Solusi yang Lebih Baik
#Implementasi Quicksort yang lebih efisien menggunakan pendekatan in-place
def quicksort_inplace(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)  # Mempartisi array
        quicksort_inplace(arr, low, pi - 1)  # Rekursif pada bagian kiri
        quicksort_inplace(arr, pi + 1, high)  # Rekursif pada bagian kanan
def partition(arr, low, high):
    pivot = arr[high]  # Memilih pivot sebagai elemen terakhir
    i = low - 1  # Indeks untuk elemen yang lebih kecil
    for j in range(low, high):
        if arr[j] < pivot:  # Jika elemen saat ini lebih kecil dari pivot
            i += 1  # Increment indeks elemen yang lebih kecil
            arr[i], arr[j] = arr[j], arr[i]  # Tukar elemen
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Tukar pivot ke posisi yang benar
    return i + 1  # Kembalikan indeks pivot
# Contoh penggunaan
mylist = [64, 34, 25, 12, 22,
11, 90, 5]
quicksort_inplace(mylist, 0, len(mylist) - 1)
print(mylist)


#w3school

def partition(array, low, high):
  pivot = array[high]
  i = low - 1

  for j in range(low, high):
     if array[j] <= pivot:
       i += 1
       array[i], array[j] = array[j], array[i]

  array[i+1], array[high] = array[high], array[i+1]
  return i+1

def quicksort(array, low=0, high=None):
  if high is None:
    high = len(array) - 1

  if low < high:
    pivot_index = partition(array, low, high)
    quicksort(array, low, pivot_index-1)
    quicksort(array, pivot_index+1, high)

mylist = [64, 34, 25, 5, 22, 11, 90, 12]
quicksort(mylist)
print(mylist)

