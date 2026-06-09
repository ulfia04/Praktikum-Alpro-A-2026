class Sepatu:
    def __init__(self, merek, warna, ukuran):
        self.Merek = merek
        self.warna = warna
        self.ukuran = ukuran
    
    def TampilkanWarna(self):
        print(f"{self.warna}")

    def Tampilkanmerek(self):
        print(f"{self.merek}")


p1 = Sepatu("Adidas", "Abu", 41)
p2 = Sepatu("nike", "Putih", 21)
p3 = Sepatu("nevada", "Hitam", 44)

p2.warna = "pink"
print(p2.warna)
