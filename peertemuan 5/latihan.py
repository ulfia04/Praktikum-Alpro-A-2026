A = [[5, 3, 1],
    [2, 8, 4],
    [6, 0, 7]]

B = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

C_Tambah = [[A[i][j] + B[i][j] for j in range(len(A))] for i in range(len(A))]
C_Kurang = [[A[i][j] - B[i][j] for j in range(len(A))] for i in range(len(A))]
C_Skalar = [[A[i][j] * 4 for j in range (len(A))] for i in range(len(A))]

print("Hasil penjumlahan matriks A dan B:")
print(C_Tambah)

print("Hasil pengurangan matriks A dan B:")
print(C_Kurang)

print("Hasil perkalian matriks A dengan skalar 4:")
print(C_Skalar)
     
     