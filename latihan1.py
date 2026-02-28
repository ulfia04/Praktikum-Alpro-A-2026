# File: latihan1_exception_dasar.py

print("=== LATIHAN 1: DASAR EXCEPTION HANDLING ===\n")

angka_list = [10, 20, 30]

try:
    idx = int(input('Masukkan index (0-2): '))
    print(f'Nilai pada index {idx}: {angka_list[idx]}')
    
except ValueError:
    print('[ERROR] Harus berupa angka bulat!')
    
except IndexError:
    print('[ERROR] Index di luar jangkauan! (Hanya 0-2)')
    
finally:
    print('Selesai.')

print("\nProgram selesai dijalankan.")