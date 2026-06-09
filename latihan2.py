# File: latihan2_pembagian.py

print("=== LATIHAN 2: PROGRAM PEMBAGIAN ===\n")

def program_pembagian():
    while True:
        try:
            print("\n--- Input Angka ---")
            angka1 = float(input('Masukkan angka pertama (pembilang): '))
            angka2 = float(input('Masukkan angka kedua (penyebut): '))
            
            hasil = angka1 / angka2
            
        except ValueError:
            print('[ERROR] Input harus berupa angka!')
            continue
            
        except ZeroDivisionError:
            print('[ERROR] Tidak bisa membagi dengan nol!')
            continue
            
        except Exception as e:
            print(f'[ERROR] Terjadi error tidak terduga: {e}')
            continue
            
        else:
            # Dijalankan jika tidak ada error
            print(f'\n✅ Hasil: {angka1} / {angka2} = {hasil:.2f}')
            
            # Tanya apakah ingin menghitung lagi
            ulang = input('\nHitung lagi? (y/n): ').lower()
            if ulang != 'y':
                print('Terima kasih telah menggunakan program ini.')
                break
                
        finally:
            print('.' * 30)  # Pemisah setiap iterasi

# Jalankan program
program_pembagian()