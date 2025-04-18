
```markdown
# 🎨 Panduan Gaya Penulisan Kode JavaScript (Style Guide)

Nulis kode itu kayak ngelukis: beda orang, beda gaya. Tapi kalau kerjanya bareng-bareng, kita butuh **aturan main** biar nggak kayak hasil karya anak TK yang nyampur crayon. 🎨

Style guide bikin kode kita:
- Konsisten
- Mudah dibaca
- Gampang dipelihara
- Dan yang pasti... bikin reviewer senyum-senyum 😏

---

## 🧱 Dasar-Dasar Penulisan

### 1. Gunakan `const` dan `let` — hindari `var`

```javascript
// ❌ Jangan
var nama = "Marno";

// ✅ Lebih baik
const nama = "Marno"; // untuk nilai yang tidak berubah
let umur = 25;         // untuk nilai yang bisa berubah
```

---

### 2. Gunakan Semicolon (`;`) Secara Konsisten

```javascript
// ✅ Gunakan
const angka = 10;
```

> JavaScript kadang "ngerti-ngertiin", tapi jangan biarkan parser nebak-nebak. Pakai semicolon!

---

### 3. Indentasi 2 Spasi (atau 4 spasi, yang penting konsisten)

```javascript
function sapa() {
  console.log("Halo!");
}
```

---

## ✨ Penamaan yang Jelas

| Jenis              | Gaya          | Contoh                |
|--------------------|---------------|------------------------|
| Variabel/fungsi    | `camelCase`   | `jumlahBuah`, `tambahData()` |
| Class              | `PascalCase`  | `UserModel`, `PanenRekap` |
| Konstanta global   | `UPPER_SNAKE` | `MAX_LIMIT`, `API_URL` |

```javascript
const MAX_RETRIES = 3;
class DataFetcher { ... }
```

---

## 🧼 Struktur dan Format

### 1. Satu Statement per Baris

```javascript
// ❌ Jangan
let a = 1; let b = 2;

// ✅ Lebih baik
let a = 1;
let b = 2;
```

---

### 2. Spasi Itu Penting!

```javascript
// ❌ Jangan
if(x===10){console.log("yes");}

// ✅ Lebih baik
if (x === 10) {
  console.log("yes");
}
```

---

### 3. Jangan Gunakan Magic Number

```javascript
// ❌ Jangan
if (umur > 17) {...}

// ✅ Lebih baik
const MINIMUM_UMUR = 17;
if (umur > MINIMUM_UMUR) {...}
```

---

## 🧠 Fungsi dan Logika

### 1. Satu Fungsi, Satu Tugas

```javascript
// ❌ Jangan
function prosesDataDanSimpanKeDatabase() {...}

// ✅ Lebih baik
function prosesData() {...}
function simpanKeDatabase() {...}
```

---

### 2. Hindari Fungsi Terlalu Panjang

Jika fungsi udah panjang kayak sinetron, itu tandanya perlu dipotong jadi episode-episode alias subfungsi.

---

## 📂 Struktur Folder dan File

```plaintext
.
├── src/
│   ├── components/
│   │   └── Button.js
│   ├── utils/
│   │   └── formatDate.js
│   ├── pages/
│   │   └── Home.js
└── index.js
```

Pisahkan fungsi, komponen, dan halaman sesuai peranannya.

---

## ✅ Kapan Gunakan ESLint dan Prettier?

Kalau kamu ingin otomatisasi gaya penulisan, install:

```bash
npm install eslint prettier --save-dev
```

Lalu setup `.eslintrc.js` dan `.prettierrc`

Contoh config:

```js
// .eslintrc.js
module.exports = {
  env: {
    browser: true,
    es2021: true
  },
  extends: ['eslint:recommended'],
  parserOptions: {
    ecmaVersion: 'latest',
    sourceType: 'module'
  },
  rules: {
    semi: ['error', 'always'],
    quotes: ['error', 'single']
  }
};
```

```json
// .prettierrc
{
  "semi": true,
  "singleQuote": true,
  "tabWidth": 2
}
```

---

## 🔥 Bonus Tips

- Komentar → hanya jika benar-benar perlu.
- Jangan komentar "kode yang jelas". Tapi jelaskan *kenapa*, bukan *apa*.

```javascript
// ❌ Buruk
// Mengatur variabel i menjadi 0
let i = 0;

// ✅ Baik
// Memulai dari indeks pertama untuk iterasi user
let i = 0;
```

---

## 🧘‍♂️ Zen of JavaScript Style

> "Kode itu dibaca lebih sering daripada ditulis."

Kalau kamu pusing lihat kode sendiri seminggu kemudian... saatnya ubah gaya nulismu, bestie.

---

## 🎯 Kesimpulan

Style guide bukan aturan ketat, tapi **pedoman hidup** buat bikin proyek kamu sehat, kolaboratif, dan scalable. Mau nulis sendiri atau tim besar, patuhi style guide seperti kamu patuhi rambu lalu lintas. 🚦

> Konsistensi > Gaya pribadi  
> Bikin kode indah, biar yang baca juga bahagia ✨

```

---

Kalau kamu mau, kita bisa buatkan file `.eslintrc.js` dan `.prettierrc` juga biar tinggal pakai di proyekmu. Mau sekalian dibikinin? 😎