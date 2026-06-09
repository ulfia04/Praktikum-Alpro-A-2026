import os
def tampilan_menu():
    print("[1] Read file") 
    print("[2] Write file") 
    print("[3] Delete FILE") 
    print("[0] Exit") 
    
print("===========================") 
print("PYTHON FILE MANAGER v1.0") 
print("===========================") 

while True:
    pilihan = input("Pilih menu: ")
    if pilihan == "1":
        print("file tersedia")
        print("[1] catatan.txt")
        print("[2] tugas.txt")
        print("[3] jadwal.txt")
    else:
       print("file tidak tersedka")

    file_pilihan = input("Pilih file:(nomor)")
    if file_pilihan =="1":
        with open("catatan.txt", "r") as f:
            print(f.read())

    elif file_pilihan =="2":
        with open("tugas.txt", "r") as f:
            print(f.read())
            
    elif file_pilihan =="3":
        with open("jadwal.txt", "r") as f:
            print(f.read())
    else:
        print("file tidak tersedia")


        
       