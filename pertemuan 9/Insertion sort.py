#Menerapkan Informasi Penyisipan dalam Python
#Insertion Sort adalah algoritma pengurutan yang sederhana dan efisien untuk mengurutkan elemen-elemen dalam sebuah daftar. Algoritma ini bekerja dengan membagi daftar menjadi dua bagian: bagian yang sudah terurut dan bagian yang belum terurut. Pada setiap iterasi, elemen dari bagian yang belum terurut dipilih dan disisipkan ke posisi yang tepat dalam bagian yang sudah terurut.
#Berikut adalah implementasi Insertion Sort dalam Python:
#buat sendiri algoritma penyisipan
#w3scholl

mylist = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(mylist)
for i in range(1,n):
  insert_index = i
  current_value = mylist.pop(i)
  for j in range(i-1, -1, -1):
    if mylist[j] > current_value:
      insert_index = j
  mylist.insert(insert_index, current_value)

print(mylist)

#Solusi yang Lebih Baik
#Menerapkan Informasi Penyisipan dalam Python dengan cara yang lebih baik
#Dalam solusi ini, kita menggunakan variabel `j` untuk melacak posisi saat kita membandingkan elemen-elemen dalam daftar. Kita memindahkan elemen-elemen yang lebih besar ke kanan hingga kita menemukan posisi yang tepat untuk menyisipkan nilai saat ini.
#Ini menghindari penggunaan metode `pop()` dan `insert()`, yang dapat menjadi tidak efisien karena mereka memerlukan pergeseran elemen-elemen dalam daftar. Dengan menggunakan pendekatan ini, kita hanya melakukan pergeseran elemen yang diperlukan, sehingga meningkatkan efisiensi algoritma penyisipan.
#Berikut adalah implementasi yang lebih baik dari algoritma penyisipan dalam Python:
#buat sendiri algoritma penyisipan

mylist = [64, 34, 25, 12, 22, 11, 90, 5]
n = len(mylist)
for i in range(1, n):
    current_value = mylist[i]
    j = i - 1
    while j >= 0 and mylist[j] > current_value:
      mylist[j + 1] = mylist[j]
      j -= 1
    mylist[j + 1] = current_value
print(mylist)

#Solusi yang Lebih Baik
#w3scholl

mylist = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(mylist)
for i in range(1,n):
  insert_index = i
  current_value = mylist[i]
  for j in range(i-1, -1, -1):
     if mylist[j] > current_value:
       mylist[j+1] = mylist[j]
       insert_index = j
     else:
       break
  mylist[insert_index] = current_value

print(mylist)




