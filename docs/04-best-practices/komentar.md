
# 💬 Panduan Menulis Komentar yang Baik di JavaScript

Komentar itu kayak bumbu masakan. Kalau pas, bikin enak. Kalau kebanyakan... malah bikin pusing. 🍜

Tujuan komentar:
- Menjelaskan *kenapa*, bukan *apa*.
- Memberi konteks untuk logika yang kompleks.
- Membantu developer lain (atau diri sendiri 6 bulan kemudian 😅).

---

## 🧠 Komentar Bukan Pengganti Kode yang Jelas

```javascript
// ❌ Komentar nggak perlu
// Menambahkan 1 ke nilai i
i = i + 1;
```

Kode di atas udah cukup jelas. Komentar kayak gitu malah mubazir dan bikin penuh layar.

---

## ✅ Komentar yang Bagus Itu...

### 1. Menjelaskan Alasan di Balik Kode

```javascript
// Menghindari bug Safari saat parsing JSON besar
const data = JSON.parse(jsonString);
```

---

### 2. Memberi Konteks untuk Logika Kompleks

```javascript
// Menghitung gaji prorata jika karyawan masuk pertengahan bulan
const proratedSalary = (baseSalary / daysInMonth) * daysWorked;
```

---

### 3. Menandai Hal Penting

Gunakan tag seperti:

- `TODO:` ➜ yang harus dikerjakan nanti
- `FIXME:` ➜ ada yang salah, perlu dibenerin
- `HACK:` ➜ solusi darurat yang belum ideal
- `NOTE:` ➜ catatan penting

```javascript
// TODO: Tambahkan validasi untuk input kosong
// FIXME: Crash kalau data kosong
// HACK: Pakai delay manual karena bug dari API
```

---

## ❌ Komentar yang Harus Dihindari

### 1. Menjelaskan Kode yang Jelas

```javascript
// Mengatur x menjadi 10
let x = 10;
```

### 2. Komentar Redundant

```javascript
// Fungsi ini menambahkan dua angka
function tambah(a, b) {
  return a + b;
}
```

Kalo kamu merasa perlu komentar kayak gitu, coba ubah nama fungsi jadi lebih jelas aja.

---

## ✨ Tips Menulis Komentar

- **Tulis sejelas mungkin.** Hindari singkatan aneh atau bahasa alien.
- **Gunakan bahasa yang konsisten.** Kalau dokumentasimu pakai bahasa Indonesia, jangan tiba-tiba pakai bahasa Klingon.
- **Letakkan komentar di atas kode yang dijelaskan**, bukan di samping.

```javascript
// Menghindari NaN jika nilai kosong
const nilai = parseFloat(input) || 0;
```

---

## 📌 Komentar vs Dokumentasi

Gunakan komentar untuk:
- Penjelasan cepat
- Catatan penting dalam kode

Gunakan dokumentasi terpisah (seperti ini!) untuk:
- Penjelasan lengkap fungsi
- Tutorial penggunaan modul
- Panduan best practice

---

## 🧘‍♀️ Zen of Komentar

> "Kode yang bagus butuh sedikit komentar. Tapi komentar yang bagus bisa menyelamatkan proyek."  
> — Seorang developer yang trauma debug jam 3 pagi 😵‍💫

---

## 🎯 Kesimpulan

Komentar bukan tempat curhat. Tapi dia bisa jadi penyelamat di saat genting.  
Gunakan dengan bijak, dan ingat: **komentar yang baik = tim yang bahagia** 🫶

```

---

Kalau kamu mau, kita juga bisa bikin *template* komentar atau style guide komentar internal. Mau dibuatkan? 😄