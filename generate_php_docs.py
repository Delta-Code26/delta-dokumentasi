import os

base_path = r"D:\dokumentasi\dokumentasi-javascript-dari-nol\docs\PHP"

struktur_dokumen = {
    "01-pemula": [
        "01-Pengenalan-PHP.md",
        "02-Instalasi-dan-Setup.md",
        "03-Struktur-Dasar-Program-PHP.md",
        "04-Tipe-Data-dan-Variabel.md",
        "05-Operator.md",
        "06-Struktur-Kontrol.md",
        "07-Perulangan.md",
        "08-Fungsi.md",
        "09-Array.md",
        "10-Superglobal.md",
        "11-Form-Handling.md",
        "12-Include-dan-Require.md"
    ],
    "02-menengah": [
        "13-String-dan-Regex.md",
        "14-File-Handling.md",
        "15-Session-Cookie.md",
        "16-Upload-File.md",
        "17-Validasi-Data.md",
        "18-MySQL-Koneksi.md",
        "19-CRUD-MySQL.md",
        "20-Modularisasi-Kode.md",
        "21-Error-Handling.md"
    ],
    "03-mahir": [
        "22-OOP-di-PHP.md",
        "23-Constructor-Inheritance.md",
        "24-Interface-Abstract.md",
        "25-Trait.md",
        "26-Namespace-Autoloading.md",
        "27-Composer.md",
        "28-Design-Pattern.md",
        "29-REST-API.md",
        "30-JSON-HTTP.md",
        "31-Middleware.md"
    ],
    "04-best-practices": [
        "32-Clean-Code.md",
        "33-Struktur-Folder.md",
        "34-Validasi-Sanitasi.md",
        "35-Keamanan.md",
        "36-Password-Hashing.md",
        "37-Env-File.md",
        "38-Code-Style.md",
        "39-Unit-Testing.md",
        "40-Logging-Debugging.md"
    ],
    "05-mini-proyek": [
        "41-Login-Sederhana.md",
        "42-CRUD-Mahasiswa.md",
        "43-Sistem-Voting.md",
        "44-Galeri-Foto.md",
        "45-Catatan-Harian.md",
        "46-Pemesanan-Tiket.md",
        "47-Blog-Sederhana.md",
        "48-REST-API-Mobile.md"
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
