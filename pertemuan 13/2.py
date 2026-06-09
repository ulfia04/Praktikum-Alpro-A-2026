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
    
    pilihan = input("Pilih menu: ")
    
    if pilihan == "1":
        # Read file
        daftar_file = []
        for file in os.listdir('.'):
            if file.endswith('.txt'):
                daftar_file.append(file)
        
        if len(daftar_file) == 0:
            print("Tidak ada file .txt ditemukan.")
        else:
            print("File tersedia:")
            for i in range(len(daftar_file)):
                print(f"[{i+1}] {daftar_file[i]}")
            
            try:
                nomor = int(input("Pilih file (nomor): "))
                if nomor >= 1 and nomor <= len(daftar_file):
                    nama_file = daftar_file[nomor-1]
                    print(f"--- Isi {nama_file} ---")
                    with open(nama_file, 'r') as f:
                        print(f.read())
                    print("--------------------")
                else:
                    print("Nomor tidak valid!")
            except:
                print("Input tidak valid!")
    
    elif pilihan == "2":
        # Write file
        daftar_file = []
        for file in os.listdir('.'):
            if file.endswith('.txt'):
                daftar_file.append(file)
        
        if len(daftar_file) > 0:
            print("File tersedia:")
            for i in range(len(daftar_file)):
                print(f"[{i+1}] {daftar_file[i]}")
        else:
            print("Tidak ada file .txt ditemukan.")
        
        pilih = input("Pilih nomor file atau ketik nama file baru: ")
        
        try:
            if pilih.isdigit():
                nomor = int(pilih)
                if nomor >= 1 and nomor <= len(daftar_file):
                    nama_file = daftar_file[nomor-1]
                else:
                    nama_file = input("Masukkan nama file baru: ")
                    if not nama_file.endswith('.txt'):
                        nama_file = nama_file + '.txt'
            else:
                nama_file = pilih
                if not nama_file.endswith('.txt'):
                    nama_file = nama_file + '.txt'
            
            isi = input("Masukkan isi teks: ")
            with open(nama_file, 'w') as f:
                f.write(isi)
            print(f"File {nama_file} berhasil disimpan!")
        except:
            print("Terjadi kesalahan!")
    
    elif pilihan == "3":
        # Delete file
        daftar_file = []
        for file in os.listdir('.'):
            if file.endswith('.txt'):
                daftar_file.append(file)
        
        if len(daftar_file) == 0:
            print("Tidak ada file .txt ditemukan.")
        else:
            print("File tersedia:")
            for i in range(len(daftar_file)):
                print(f"[{i+1}] {daftar_file[i]}")
            
            try:
                nomor = int(input("Pilih file (nomor): "))
                if nomor >= 1 and nomor <= len(daftar_file):
                    nama_file = daftar_file[nomor-1]
                    konfirmasi = input(f"Yakin ingin menghapus {nama_file}? (y/n): ")
                    if konfirmasi == 'y':
                        os.remove(nama_file)
                        print(f"File {nama_file} berhasil dihapus!")
                    else:
                        print("Penghapusan dibatalkan.")
                else:
                    print("Nomor tidak valid!")
            except:
                print("Input tidak valid!")
    
    elif pilihan == "0":
        print("Terima kasih telah menggunakan Python File Manager v1.0")
        break
    
    else:
        print("Pilihan tidak valid, silakan coba lagi.")
    
    print()