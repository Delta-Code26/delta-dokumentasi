import os

base_path = r"D:\dokumentasi\dokumentasi-javascript-dari-nol\docs\belajar-javascript"

struktur_dokumen = {
    "01-pemula": [
        "01-Pengenalan-JavaScript.md",
        "02-Syntax-dasar.md",
        "03-Variabel.md",
        "04-Tipe-Data.md",
        "05-Operator.md",
        "06-Kondisi-If-Else.md",
        "07-Perulangan.md",
        "08-Array.md",
        "09-Function.md",
        "10-Object.md",
        "11-Scope-dan-Hoisting.md",
        "12-Callback.md"
    ],
    "02-menengah": [
        "13-Fetch-API.md",
        "14-Higher-Order-Function.md",
        "15-Modularisasi.md",
        "16-Struktur-Data.md"
    ],
    "03-mahir": [
        "17-Event-Loop.md",
        "18-Functional-Programming.md",
        "19-Keamanan.md",
        "20-Konsep-Lanjutan.md",
        "21-OOP.md",
        "22-Tools-Bundler-Linter.md"
    ],
    "04-best-practices": [
        "23-Clean-Code.md",
        "24-Debugging.md",
        "25-Error-Handling.md",
        "26-Performance.md",
        "27-Refactor.md",
        "28-Testing.md",
        "29-Style-Guide.md",
        "30-Komentar.md"
    ],
    "05-mini-proyek": [
        "31-Kalkulator.md",
        "32-ToDo-List.md",
        "33-Gallery.md",
        "34-Pencarian-Film.md",
        "35-Quiz-App.md"
    ]
}

for folder, files in struktur_dokumen.items():
    folder_path = os.path.join(base_path, folder)
    os.makedirs(folder_path, exist_ok=True)
    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        if not os.path.exists(file_path):
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(f"# {file_name.replace('-', ' ').replace('.md', '')}\n")
            print(f"[✓] Created: {file_path}")
        else:
            print(f"[!] Already exists: {file_path}")
