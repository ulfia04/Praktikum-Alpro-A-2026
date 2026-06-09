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


def total_ukuran(folder: dict) -> int:
    total = 0
    for key, value in folder.items():
        if isinstance(value, dict):
            total += total_ukuran(value)
        else:
            total += value
    return total

ukuran_total = total_ukuran(struktur)
print(f"Total_ukuran(folder: dict): {ukuran_total} KB")
