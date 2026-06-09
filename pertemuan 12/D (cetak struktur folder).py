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

def tampilkan_tree(folder: dict, nama: str = "root", level: int = 0):
    indent = "  " * level
    print(f"{indent}📁 {nama}")

    for item, isi in folder.items():
        if isinstance(isi, dict):
            # Folder — rekursi dengan level+1
            tampilkan_tree(isi, item, level + 1)
        else:
            # File — cetak dengan indentasi level+1
            file_indent = "  " * (level + 1)
            print(f"{file_indent}📄 {item} ({isi} KB)")

tampilkan_tree(struktur, "Skripsi_Aqil")


    
