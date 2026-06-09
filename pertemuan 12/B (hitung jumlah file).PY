struktur = {
    "Skripsi_Aqil": {
        "Bab_1": {
            "pendahuluan.docx": 45,
            "latar_belakang.docx": 62
        },
        "Bab_2": {
            "landasan_teori.docx": 118,
            "referensi": {
                "paper_A.pdf": 340,
                "paper_B.pdf": 210
            }
        },
        "Bab_3": {
            "metodologi.docx": 89,
            "diagram": {
                "flowchart.png": 512,
                "er_diagram.png": 278,
                "arsitektur": {
                    "sistem.png": 430
            }
            }
        }
    },
    "sidang": {
        "presentasi.pptx": 2048,
        "catatan_revisi.txt": 15
     },
    "README.txt": 8
    }

def hitung_file(folder: dict) -> int:
    total = 0
    for key, value in folder.items():
        if isinstance(value, dict):
            total += hitung_file(value)
        else:
            total += 1
    return total

jumlah_file = hitung_file(struktur)
print(f"Jumlah file: {jumlah_file } file")