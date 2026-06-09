import os
 
print("=1===========================")
print("PYTHON FILE MANAGER v1.0")
print("============================")

while True:
    print("[1] Read file")
    print("[2] Write file")
    print("[3] Delete file")   
    print("[0] Exit")
    print("------------------------------")

    pilihan = input("Pilih menu: ")
    if pilihan == "1":
        print("file tersedia")
        print("[1] catatan.txt")
        print("[2] tugas.txt")
        print("[3] jadwal.txt")
    
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
        
    elif pilihan == "2":
        print("file tersedia")
        print("[1] catatan.txt")
        print("[2] tugas.txt")
        print("[3] jadwal.txt")
    
        file_pilihan = input("pilihan file:(nomor)")
        if file_pilihan =="1":
            with open("catatan.txt", "w") as f:
                f.write(input("masukkan isi catatan: "))
        elif file_pilihan =="2":
            with open("tugas.txt", "w") as f:
                f.write(input("masukkan isi tugas: "))

        elif file_pilihan =="3":
            with open("jadwal.txt", "w") as f:
                f.write(input("masukkan isi jadwal: "))
        else:
            print("file tidak tersedia")

    elif pilihan == "3":
        print("file tersedia")
        print("[1] catatan.txt")
        print("[2] tugas.txt")
        print("[3] jadwal.txt")
    
       