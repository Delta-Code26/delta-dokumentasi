import os

# Base folder tujuan
base_path = r"D:\dokumentasi\dokumentasi-javascript-dari-nol\docs\belajar-java"

# Daftar isi
judul_bab = [
    # Dasar-dasar Java
    "Pengenalan Java",
    "Instalasi dan Setup Java",
    "Program Pertama di Java",
    "Struktur Dasar Program Java",
    "Tipe Data dan Variabel",
    "Operator di Java",
    "Percabangan (if, switch)",
    "Perulangan (for, while, do-while)",
    "Array di Java",
    "String dan Manipulasi String",

    # OOP
    "Konsep OOP di Java",
    "Class dan Object",
    "Package dan Import",
    "Constructor dan Overloading",
    "Inheritance (Pewarisan)",
    "Polymorphism",
    "Encapsulation",
    "Abstraksi dan Interface",
    "This dan Super Keyword",
    "Access Modifiers",
    "Static vs Non-Static",
    "Final Keyword dan Konstanta",

    # Struktur Data & Koleksi
    "ArrayList, LinkedList, HashSet, TreeSet",
    "HashMap, TreeMap",
    "Iterator dan For-Each",
    "Generic di Java",

    # Exception Handling
    "Try, Catch, Finally",
    "Multiple Catch dan Nested Try",
    "Throw dan Throws",
    "Custom Exception",

    # I/O
    "Scanner dan BufferedReader",
    "Menulis dan Membaca File",
    "Serialization dan Deserialization",

    # Multithreading
    "Thread Class dan Runnable Interface",
    "Synchronized dan Lock",
    "Thread Pool & ExecutorService",
    "Deadlock dan Race Condition",

    # Networking
    "Pengenalan Networking di Java",
    "Socket Programming",
    "Membuat Client-Server Sederhana",
    "HTTP Request dengan Java",

    # Tools & Testing
    "Debugging di IDE",
    "Unit Testing dengan JUnit",
    "Logging dan Error Handling Best Practices",
    "Profiling dan Performance Optimization",

    # GUI
    "Pengenalan Swing dan AWT",
    "Membuat Frame dan Layout",
    "Button, TextField, Label, dll",
    "Event Handling",
    "Proyek GUI Sederhana",

    # Android
    "Apa itu Android dan Hubungannya dengan Java",
    "Struktur Proyek Android Studio",
    "Activity dan Layout",
    "Java untuk Android Development",
    "Membuat Aplikasi Kalkulator",
    "Aplikasi Manajemen Data Mahasiswa",
    "To-Do List dengan GUI",
    "Mini CRUD dengan File",
    "Sistem Login Sederhana",

    # Best Practices
    "Java Design Patterns (Factory, Singleton, dll)",
    "Clean Code dengan Java",
    "Refactoring dan Maintainability",
    "Style Guide dan Konvensi Penamaan",
    "Maven & Gradle untuk Manajemen Proyek",
    "Java 8 Features (Lambda, Stream API)",
    "Java 17 dan Versi Terbaru (Record, Sealed Classes, dll)",
    "Secure Coding dan SQL Injection",
    "JDBC dan Koneksi Database"
]

# Buat semua file dengan nama rapi
for i, judul in enumerate(judul_bab, start=1):
    # Format nomor bab dan nama file
    nomor = str(i).zfill(2)
    nama_file = f"{nomor}-{judul.replace(' ', '-').replace('(', '').replace(')', '').replace('&', 'dan').replace('/', '-')}.md"
    path_file = os.path.join(base_path, nama_file)

    # Isi awal setiap file
    isi = f"# {nomor}. {judul}\n\n_Tuliskan materi lengkap di sini._\n"

    # Buat file markdown
    os.makedirs(os.path.dirname(path_file), exist_ok=True)
    with open(path_file, "w", encoding="utf-8") as f:
        f.write(isi)

    print(f"✅ {nama_file} berhasil dibuat!")

print("\n🎉 Semua file berhasil digenerate!")
