import os

# Daftar file dan judul
materi_sql = [
    ("01-Pengenalan-SQL.md", "Pengenalan tentang SQL, tujuan dan kegunaannya."),
    ("02-Instalasi-dan-Setup.md", "Cara instalasi MySQL atau PostgreSQL dan setup DBMS."),
    ("03-Dasar-Dasar-SQL.md", "Dasar-dasar SQL, termasuk sintaks dasar dan query SELECT."),
    ("04-SELECT-Statement.md", "Penggunaan SELECT untuk mengambil data dari database."),
    ("05-Clauses-SQL.md", "Penjelasan tentang WHERE, ORDER BY, GROUP BY, dan HAVING."),
    ("06-JOIN.md", "Menggabungkan tabel menggunakan INNER JOIN, LEFT JOIN, RIGHT JOIN, dan FULL JOIN."),
    ("07-Subquery.md", "Penggunaan subquery dalam SQL."),
    ("08-Insert-Update-Delete.md", "Cara menambah, memperbarui, dan menghapus data menggunakan INSERT, UPDATE, dan DELETE."),
    ("09-Constraints.md", "Penjelasan tentang constraints seperti PRIMARY KEY, FOREIGN KEY, UNIQUE, dan CHECK."),
    ("10-Tipe-Data-SQL.md", "Jenis-jenis tipe data yang digunakan di SQL seperti INT, VARCHAR, DATE, dll."),
    ("11-Index.md", "Penggunaan dan keuntungan index dalam query SQL."),
    ("12-Views.md", "Penjelasan tentang views di SQL dan cara menggunakannya."),
    ("13-Stored-Procedures.md", "Cara membuat dan menggunakan stored procedures dalam SQL."),
    ("14-Transactions.md", "Pengenalan transaksi SQL, ACID, dan penggunaan COMMIT dan ROLLBACK."),
    ("15-Performance-Tuning.md", "Tips dan trik untuk optimasi query SQL."),
    ("16-SQL-Functions.md", "Penggunaan built-in functions seperti COUNT, AVG, SUM, dll."),
    ("17-Data-Integrity.md", "Menjaga integritas data menggunakan SQL (constraints, referential integrity)."),
    ("18-Backup-dan-Restore.md", "Cara melakukan backup dan restore database."),
    ("19-Database-Design.md", "Konsep dasar desain database dan normalisasi."),
    ("20-Advanced-Queries.md", "Query lanjutan seperti UNION, CASE, dan analitik lainnya."),
]

# Folder tujuan
base_dir_sql = 'docs/belajar-sql'
os.makedirs(base_dir_sql, exist_ok=True)

# Membuat file dan menulis konten dasar
for file_name, description in materi_sql:
    file_path = os.path.join(base_dir_sql, file_name)
    
    with open(file_path, 'w') as f:
        f.write(f"# {file_name.replace('-', ' ').title()}\n\n")
        f.write(f"**Deskripsi:** {description}\n\n")
        f.write("Tuliskan materi di sini.\n")

print("File dokumentasi SQL telah dibuat di folder 'docs/belajar-sql'.")
