import os

print("============================")
print("PYTHON FILE MANAGER v1.0")
print("============================")


while True:
    print("[1] Read file")
    print("[2] Write file")
    print("[3] Delete file")   
    print("[0] Exit")
    print("------------------------------")

    pilihan = input("Pilih menu: ").strip()
    if pilihan == "1":
        file = [f for f in os.listdir() if f.endswith(".txt")]
        
        if len(file) == 0:
            print("tidak ada file .txt yang ditemukan")
        else:
            print("File tersedia:")
            for i in range(len(file)):
                print(f"[{i+1}] {file[i]}")

            try:
                pilih_file = int(input("Pilih file (nomor): "))
                nama_file = file[pilih_file - 1]

                f = open(nama_file, "rt")
                print(f"--- Isi {nama_file} ---")
                print(f.read())
                print("--------------------")
                f.close()
            except (ValueError, IndexError):
                print("Pilihan tidak valid.")
    

    elif pilihan == "2":
        file = [f for f in os.listdir() if f.endswith(".txt")]

        print("file tersedia:")

        if len(file) == 0:
            print("tidak ada file .txt yang ditemukan")
        else:        
            for i in range(len(file)):
                print(f"[{i+1}] {file[i]}")

        pilih_file = input("Pilih file (nomor) atau ketik nama file baru: ")

        try:
            if pilih_file.isdigit() and len(file) > 0:
               nama_file = file[int(pilih_file) - 1]
            else:
                nama_file = pilih_file
                if not nama_file.endswith(".txt"):
                    nama_file += ".txt"
            
            mode = input("Pilih mode (a untuk append, w untuk overwrite): ").lower()
            
            isi = input("Masukkan isi teks: ")

            f = open(nama_file, mode)
            f.write(isi + "\n")
            f.close()

            print(f"Berhasil menulis ke {nama_file}.")
        
        except (ValueError, IndexError):
            print("Pilihan tidak valid.")

    elif pilihan == "3":
        file = [f for f in os.listdir() if f.endswith(".txt")]

        if len(file) == 0:
            print("tidak ada file .txt yang ditemukan")
        else:
            print("File tersedia:")
            for i in range(len(file)):
                print(f"[{i+1}] {file[i]}")

            try:
                pilih_file = int(input("Pilih file untuk dihapus (nomor): "))
                nama_file = file[pilih_file - 1]

                konfirmasi = input(f"ingin menghapus {nama_file}? (y/n): ").lower()
                if konfirmasi == "y":
                    if os.path.exists(nama_file):
                        os.remove(nama_file)
                        print(f"{nama_file} berhasil dihapus.")
                    else:
                        print(f"{nama_file} tidak ditemukan.")
                else:
                    print("Penghapusan dibatalkan.")

            except (ValueError, IndexError):
                print("Pilihan tidak valid.")

    elif pilihan == "0":
        print("program selesai hehe")
        break

    else:
        print("Pilihan tidak valid.")

