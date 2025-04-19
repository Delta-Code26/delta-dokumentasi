import os

# Ganti ini dengan path folder yang ingin kamu baca
folder_path = 'D:/dokumentasi/dokumentasi-javascript-dari-nol/docs/JAVA'

# Cek apakah folder ada
if not os.path.exists(folder_path):
    print("Folder tidak ditemukan!")
    exit()

# Ambil semua file di folder (tanpa subfolder)
file_names = [
    name for name in os.listdir(folder_path)
    if os.path.isfile(os.path.join(folder_path, name))
]

# Tulis hasil ke file teks
output_path = os.path.join(folder_path, 'daftar_file.txt')

with open(output_path, 'w', encoding='utf-8') as f:
    for name in sorted(file_names):
        f.write(name + '\n')

print(f"Berhasil menyimpan {len(file_names)} file ke: {output_path}")
