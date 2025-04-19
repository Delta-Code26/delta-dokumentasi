import os

# Daftar file dan judul
materi = [
    ("01-Pengenalan-Kotlin.md", "Pengenalan bahasa Kotlin dan fitur utamanya."),
    ("02-Instalasi-dan-Setup.md", "Cara instalasi Kotlin dan setup IDE (IntelliJ IDEA)."),
    ("03-Variabel-dan-Tipe-Data.md", "Penjelasan variabel, tipe data, dan konversi tipe di Kotlin."),
    ("04-Percabangan.md", "Cara menggunakan if, when, dan ekspresi kondisional."),
    ("05-Perulangan.md", "Penjelasan tentang perulangan dengan for, while, dan do-while."),
    ("06-Function.md", "Fungsi dasar di Kotlin, parameter, return value, dan lambda."),
    ("07-Kelas-dan-Objek.md", "Pemahaman dasar tentang kelas, objek, dan konstruktor."),
    ("08-Properties-dan-Fields.md", "Menjelaskan properti dan fields dalam Kotlin."),
    ("09-Encapsulation.md", "Membahas tentang enkapsulasi dalam OOP."),
    ("10-Inheritance.md", "Penjelasan tentang pewarisan kelas di Kotlin."),
    ("11-Polymorphism.md", "Polimorfisme pada Kotlin, penggunaan override dan super."),
    ("12-Interface-dan-Abstract-Class.md", "Perbedaan dan penggunaan interface serta abstract class."),
    ("13-Collection.md", "Koleksi di Kotlin, seperti List, Set, dan Map."),
    ("14-Lambda-dan-Higher-Order-Functions.md", "Fungsi lambda dan higher-order functions di Kotlin."),
    ("15-Coroutines.md", "Pengenalan coroutines di Kotlin untuk concurrency."),
    ("16-Null-Safety.md", "Menjelaskan tentang null safety dan penggunaan ?, !!, dan ?:."),
    ("17-Extension-Functions.md", "Cara membuat dan menggunakan extension functions di Kotlin."),
    ("18-Serialization-dan-Deserialization.md", "Penggunaan Gson atau kotlinx.serialization di Kotlin."),
    ("19-Testing-di-Kotlin.md", "Teknik-teknik unit testing di Kotlin, menggunakan JUnit dan Assert."),
    ("20-Multi-Platform-Development.md", "Membahas Kotlin Multiplatform untuk pengembangan aplikasi lintas platform.")
]

# Folder tujuan
base_dir = 'docs/belajar-kotlin'
os.makedirs(base_dir, exist_ok=True)

# Membuat file dan menulis konten dasar
for file_name, description in materi:
    file_path = os.path.join(base_dir, file_name)
    
    with open(file_path, 'w') as f:
        f.write(f"# {file_name.replace('-', ' ').title()}\n\n")
        f.write(f"**Deskripsi:** {description}\n\n")
        f.write("Tuliskan materi di sini.\n")

print("File dokumentasi Kotlin telah dibuat di folder 'docs/belajar-kotlin'.")
