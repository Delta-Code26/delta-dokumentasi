
```markdown
# 🧪 Testing di JavaScript: Biar Nggak Cuma "Feeling Aman"

Testing bukan cuma buat developer perfeksionis. Ini *senjata rahasia* buat memastikan kode kamu jalan sesuai harapan — **dan tetap jalan walau udah dioprek-oprek orang satu tim**. Kalau kamu pernah nambah fitur terus tiba-tiba bagian lain rusak, berarti kamu udah kenal si "regression bug". Testing bisa jadi tamengmu. 🛡️

---

## 📌 Kenapa Perlu Testing?

- Pastikan kode **berfungsi dengan benar**
- Lindungi dari **bug tersembunyi**
- Bantu proses **refactor tanpa takut**
- Jadi dokumentasi hidup
- Bikin kamu terlihat profesional di mata tech lead 😎

---

## 🧬 Jenis-Jenis Testing

| Jenis                | Fokus                                                             |
|----------------------|-------------------------------------------------------------------|
| Unit Test            | Fungsi/unit terkecil (biasanya 1 fungsi)                          |
| Integration Test     | Beberapa fungsi/module bekerja bareng                             |
| End-to-End (E2E) Test| Simulasi interaksi user dari awal sampai akhir                    |
| Snapshot Test        | Membandingkan output sekarang dengan output sebelumnya            |

---

## 🔧 Alat Testing Populer

| Tool        | Keterangan                              |
|-------------|------------------------------------------|
| Jest        | Paling populer untuk unit test           |
| Mocha + Chai| Alternatif fleksibel                     |
| Vitest      | Cepat dan modern, mirip Jest             |
| Cypress     | Untuk end-to-end testing berbasis browser|
| Playwright  | Mirip Cypress, tapi kuat buat testing multi-browser |

---

## 🚀 Contoh Unit Test dengan Jest

### 1. Fungsi yang Diuji

```javascript
// utils/math.js
function tambah(a, b) {
  return a + b;
}
module.exports = tambah;
```

### 2. File Testing-nya

```javascript
// __tests__/math.test.js
const tambah = require('../utils/math');

test('menjumlahkan 2 + 3 harusnya 5', () => {
  expect(tambah(2, 3)).toBe(5);
});
```

### 3. Jalankan Test

```bash
npx jest
```

---

## ⚙️ Setup Jest (Manual)

```bash
npm init -y
npm install --save-dev jest
```

Di `package.json`, tambahkan:

```json
"scripts": {
  "test": "jest"
}
```

---

## 🤖 Contoh Test Lain

### Test Fungsi Asynchronous

```javascript
// asyncFunction.js
function getUser(id) {
  return Promise.resolve({ id, name: 'Marno' });
}

module.exports = getUser;
```

```javascript
// asyncFunction.test.js
const getUser = require('../utils/asyncFunction');

test('ambil user by id', async () => {
  const user = await getUser(10);
  expect(user.name).toBe('Marno');
});
```

---

## 🧼 Best Practice Testing

- Gunakan nama test yang jelas
- Jangan test hal yang gak penting (kayak `2 + 2 = 4`)
- Pisahkan test dari logic (misal: folder `__tests__` atau `tests`)
- Gunakan coverage untuk cek sejauh mana kode kamu dites

```bash
npx jest --coverage
```

---

## 🧠 TDD vs BDD

| Istilah | Penjelasan                                                                 |
|--------|-----------------------------------------------------------------------------|
| TDD    | Test-Driven Development → tulis test dulu, baru implementasi kodenya       |
| BDD    | Behavior-Driven Development → fokus ke perilaku aplikasi yang diharapkan   |

---

## 🤓 Testing Frontend DOM

Misal kamu punya tombol:

```html
<button id="klik">Klik aku!</button>
<p id="output"></p>
```

Dan script:

```javascript
document.getElementById("klik").addEventListener("click", () => {
  document.getElementById("output").textContent = "Sudah diklik!";
});
```

Dengan tool seperti **Jest + jsdom**, kamu bisa test manipulasi DOM-nya.

---

## 🎯 Kesimpulan

Testing bukan buang-buang waktu. Justru hemat waktu dari masa depan yang penuh bug dan lembur. Bahkan kalau kamu kerja solo, testing itu seperti ngasih jaminan ke diri sendiri:

> "Kalau rusak, aku tahu kenapa."  
> — Kamu yang masa depan ✨

Mulailah dari unit test, perlahan ke integration, dan kalau udah pede, masuk ke E2E. Yang penting: **tes itu investasi, bukan beban** 💸

---

## ✅ Checklist Testing

| Kegiatan                        | Status |
|---------------------------------|--------|
| Setup Jest / Vitest             | ✅     |
| Buat minimal 1 unit test        | ✅     |
| Jalankan `npm test` rutin       | ✅     |
| Gunakan coverage                | ✅     |
| Simulasikan edge-case           | ✅     |
| Tambahkan test saat refactor    | ✅     |
```

---

Dokumentasi best practices udah lengkap nih bro! Kalau mau lanjut, bisa kita tambahkan:

- Halaman "FAQ JavaScript"
- Panduan kontribusi (`CONTRIBUTING.md`)
- Panduan deploy ke GitHub Pages lagi
- Atau bikin PDF export dari MkDocs

Mau lanjut ke mana dulu? 😎📘