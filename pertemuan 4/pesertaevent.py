# File: tugas_registrasi_event.py
# Program Registrasi Peserta Seminar dengan Validasi Input

print("=" * 40)
print("=== REGISTRASI PESERTA SEMINAR ===")
print("=" * 40)

# ========== CUSTOM EXCEPTION ==========

class NamaError(Exception):
    """Custom exception untuk validasi nama"""
    def __init__(self, nama):
        self.nama = nama
        super().__init__(f'Nama "{nama}" terlalu pendek! Minimal 3 karakter.')

class UmurError(Exception):
    """Custom exception untuk validasi umur"""
    def __init__(self, umur):
        self.umur = umur
        super().__init__(f'Umur {umur} tidak memenuhi syarat (17-60 tahun).')

class EmailError(Exception):
    """Custom exception untuk validasi email"""
    def __init__(self, email):
        self.email = email
        super().__init__(f'Email "{email}" tidak valid! Harus mengandung "@".')

class NoHpError(Exception):
    """Custom exception untuk validasi nomor HP"""
    def __init__(self, no_hp):
        self.no_hp = no_hp
        super().__init__(f'No HP "{no_hp}" tidak valid! Harus 10-13 digit angka.')


# ========== FUNGSI VALIDASI ==========

def validasi_nama(nama):
    """Validasi nama minimal 3 karakter"""
    if len(nama) < 3:
        raise NamaError(nama)
    return nama

def validasi_umur(umur):
    """Validasi umur antara 17-60 tahun"""
    try:
        umur_int = int(umur)
        if umur_int < 17 or umur_int > 60:
            raise UmurError(umur_int)
        return umur_int
    except ValueError:
        raise ValueError("Umur harus berupa angka!")

def validasi_email(email):
    """Validasi email harus mengandung @"""
    if '@' not in email:
        raise EmailError(email)
    return email

def validasi_no_hp(no_hp):
    """Validasi nomor HP 10-13 digit angka"""
    # Hapus spasi dan karakter non-digit
    no_hp_bersih = ''.join(filter(str.isdigit, no_hp))
    
    if len(no_hp_bersih) < 10 or len(no_hp_bersih) > 13:
        raise NoHpError(no_hp)
    
    # Jika ada karakter non-digit selain yang sudah dibersihkan
    if len(no_hp_bersih) != len(no_hp):
        print("[INFO] Karakter non-digit diabaikan.")
    
    return no_hp_bersih


# ========== FUNGSI INPUT DENGAN VALIDASI ==========

def input_nama():
    """Meminta input nama dengan validasi"""
    while True:
        try:
            nama = input("\nNama lengkap: ").strip()
            return validasi_nama(nama)
            
        except NamaError as e:
            print(f"[ERROR] {e}")
        except Exception as e:
            print(f"[ERROR] Terjadi kesalahan: {e}")

def input_umur():
    """Meminta input umur dengan validasi"""
    while True:
        try:
            umur = input("Umur: ").strip()
            return validasi_umur(umur)
            
        except UmurError as e:
            print(f"[ERROR] {e}")
        except ValueError as e:
            print(f"[ERROR] {e}")
        except Exception as e:
            print(f"[ERROR] Terjadi kesalahan: {e}")

def input_email():
    """Meminta input email dengan validasi"""
    while True:
        try:
            email = input("Email: ").strip()
            return validasi_email(email)
            
        except EmailError as e:
            print(f"[ERROR] {e}")
        except Exception as e:
            print(f"[ERROR] Terjadi kesalahan: {e}")

def input_no_hp():
    """Meminta input nomor HP dengan validasi"""
    while True:
        try:
            no_hp = input("No HP: ").strip()
            return validasi_no_hp(no_hp)
            
        except NoHpError as e:
            print(f"[ERROR] {e}")
        except Exception as e:
            print(f"[ERROR] Terjadi kesalahan: {e}")


# ========== PROGRAM UTAMA ==========

def main():
    """Fungsi utama program registrasi"""
    
    try:
        # Input data dengan validasi
        nama = input_nama()
        umur = input_umur()
        email = input_email()
        no_hp = input_no_hp()
        
    except Exception as e:
        print(f"\n[ERROR KRITIS] {e}")
        
    finally:
        # Blok finally selalu dijalankan
        print("\nProses input selesai.")
    
    # Tampilkan ringkasan pendaftaran
    print("\n" + "=" * 40)
    print("=== DATA PESERTA ===")
    print("=" * 40)
    print(f"Nama    : {nama}")
    print(f"Umur    : {umur} tahun")
    print(f"Email   : {email}")
    print(f"No HP   : {no_hp}")
    print("-" * 40)
    print("Status  : TERDAFTAR")
    print("=" * 40)
    
    # Konfirmasi akhir
    print("\nTerima kasih telah melakukan registrasi!")


# Jalankan program
if __name__ == "__main__":
    main()