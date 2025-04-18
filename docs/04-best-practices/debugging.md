
```markdown
# 🐛 Debugging JavaScript: Cara Ngejar Bug Tanpa Bikin Emosi

Debugging itu bagian dari hidup developer. Kode error? Tenang, bukan kamu aja yang ngalamin. Yang penting kamu tahu cara ngejar bug kayak detektif JavaScript. 🔍

---

## 🤯 Apa Itu Debugging?

> Debugging adalah proses menemukan dan memperbaiki bug (kesalahan logika, runtime error, dsb.) dalam kode program.

Intinya: bikin kode kamu *berjalan sebagaimana mestinya*, bukan *bertingkah aneh pas dijalankan* 😅

---

## 🛠 Tools Wajib Debugging

### 1. `console.log()` — Sahabat Setia

Gunakan ini untuk melihat isi variabel, jalannya fungsi, atau nge-track flow:

```javascript
function hitungDiskon(harga, diskon) {
  console.log("Harga Awal:", harga);
  console.log("Diskon:", diskon);
  return harga - (harga * diskon);
}
```

**Tips:** Gunakan `console.table()` untuk array atau objek biar lebih rapi.

---

### 2. Developer Tools (DevTools) di Browser

Hampir semua browser modern punya DevTools bawaan (buka dengan `F12` atau klik kanan → Inspect).

✅ Fitur penting:
- **Console:** lihat log & error
- **Sources → Breakpoints:** pause eksekusi kode
- **Network:** cek request API
- **Performance:** analisis kecepatan

---

### 3. Breakpoint dan Step-By-Step Debugging

1. Buka tab `Sources`
2. Klik baris kode untuk set breakpoint
3. Reload halaman
4. Eksekusi berhenti di titik tersebut
5. Gunakan tombol `Step over`, `Step into`, `Step out` untuk menelusuri

---

### 4. Gunakan Linter (ESLint)

Linting bisa bantu kamu deteksi error bahkan sebelum dijalankan.

```bash
npm install eslint --save-dev
npx eslint script.js
```

---

### 5. Debugging di Node.js

Jalankan dengan mode debug:

```bash
node inspect script.js
```

Atau gunakan VS Code debugger yang powerful banget!

---

## ⚠️ Tips & Trik Debugging yang Efektif

### 1. Reproduksi Bug

- **Coba ulangi** langkah-langkah yang menyebabkan bug
- Buat test case kecil kalau bisa

### 2. Gunakan `console.trace()`

Lihat *stack trace* langsung dari mana fungsi dipanggil:

```javascript
function test() {
  console.trace("Trace dari sini");
}
```

### 3. Isolasi Masalah

Pecah kode menjadi bagian-bagian kecil. Coba blok mana yang ngaco.

### 4. Baca Pesan Error-nya!

Error JavaScript sekarang cukup informatif. Baca baik-baik bagian seperti:
- **Uncaught TypeError**
- **SyntaxError**
- **ReferenceError**

---

## ❌ Contoh Bug Umum

```javascript
let x;
console.log(x.length); // ❌ TypeError: Cannot read property 'length' of undefined
```

**Solusi:**

```javascript
if (x) {
  console.log(x.length);
}
```

---

## 💥 Debugging Asynchronous Code

Debugging `setTimeout`, `Promise`, `fetch`, dan `async/await` bisa tricky.

**Gunakan log chain** atau **catch error dengan try-catch**:

```javascript
async function getUser() {
  try {
    const res = await fetch('/user');
    const data = await res.json();
    console.log(data);
  } catch (error) {
    console.error("Gagal ambil user:", error);
  }
}
```

---

## 🧩 Teknik Lain yang Bisa Dicoba

- **Unit testing:** Tangkap bug sejak dini
- **Code review:** Bug kadang ketemu saat didiskusikan
- **Rubber duck debugging:** Jelaskan masalah ke... boneka (atau teman 😅)
- **Comment sebagian kode:** Untuk sempitkan pencarian bug

---

## 🚀 Kesimpulan

Debugging emang bisa nyebelin. Tapi kalau kamu ngerti caranya, itu jadi skill super power yang bikin kamu jadi dev yang dicari banyak perusahaan. Serius.

> “Programming is like being a detective in a crime movie where you are also the murderer.” — Filipe Fortes 😈

Keep calm & trace the bug. Kamu pasti bisa 💪

```
