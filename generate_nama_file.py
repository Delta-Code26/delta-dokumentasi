import os

def get_all_files_in_directory(directory_path):
    try:
        files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
        return files
    except FileNotFoundError:
        print(f"Folder '{directory_path}' tidak ditemukan.")
        return []
    except PermissionError:
        print(f"Tidak memiliki izin untuk mengakses folder '{directory_path}'.")
        return []

def save_files_to_txt(files, output_file, prefix=''):
    with open(output_file, 'w') as file:
        for filename in files:
            file.write(f"{prefix}{filename}\n")
    print(f"Nama file berhasil disimpan di '{output_file}' dengan prefix '{prefix}'")

# Gunakan raw string untuk path
directory = r'docs\belajar-java'
output_file = 'output_file_list.txt'
prefix = 'belajar-java/'

files = get_all_files_in_directory(directory)

if files:
    save_files_to_txt(files, output_file, prefix)
else:
    print("Tidak ada file untuk disimpan.")
