
# 🧠 Pemrograman Fungsional di JavaScript

Pemrograman Fungsional (Functional Programming / FP) adalah paradigma yang berfokus pada penggunaan **fungsi murni** (*pure functions*) dan **penghindaran efek samping**. Gaya ini makin populer karena menghasilkan kode yang:

- Lebih bersih
- Lebih mudah diuji
- Lebih modular dan fleksibel

---

## 1. Apa itu Pemrograman Fungsional?

FP mendorong kita untuk menulis program sebagai kumpulan fungsi kecil dan dapat digunakan ulang. FP menghindari perubahan langsung terhadap data (mutasi), dan lebih suka membuat data baru.

### Ciri-ciri FP:
- 📦 **Pure functions** — hasil hanya bergantung pada input
- 🚫 **No side effects** — tidak mengubah state global / input
- 🔁 **Immutability** — data tidak diubah, tapi disalin
- 🔗 **Function composition** — fungsi digabung seperti lego

---

## 2. Pure Function

Fungsi yang:
1. Tidak mengubah input.
2. Selalu mengembalikan output yang sama untuk input yang sama.

```js
// PURE
function tambah(a, b) {
  return a + b;
}

// TIDAK PURE
let total = 0;
function tambahKeTotal(a) {
  total += a; // efek samping!
}
```

---

## 3. Immutability (Tidak Mengubah Data Asli)

```js
const angka = [1, 2, 3];

// Menggunakan spread operator untuk membuat salinan
const angkaBaru = [...angka, 4];

console.log(angka);      // [1, 2, 3]
console.log(angkaBaru);  // [1, 2, 3, 4]
```

---

## 4. Higher-Order Functions (HOF)

Fungsi yang:
- Menerima fungsi lain sebagai argumen
- atau Mengembalikan fungsi

Contoh:

```js
function kalikan(faktor) {
  return function(angka) {
    return angka * faktor;
  }
}

const kaliDua = kalikan(2);
console.log(kaliDua(5)); // 10
```

---

## 5. Map, Filter, Reduce — Trio FP Legendaris 🔥

### `map()`

```js
const angka = [1, 2, 3];
const hasil = angka.map(x => x * 2); // [2, 4, 6]
```

### `filter()`

```js
const angka = [1, 2, 3, 4];
const genap = angka.filter(x => x % 2 === 0); // [2, 4]
```

### `reduce()`

```js
const angka = [1, 2, 3, 4];
const total = angka.reduce((acc, curr) => acc + curr, 0); // 10
```

---

## 6. Function Composition

Menggabungkan beberapa fungsi kecil jadi satu proses.

```js
const tambah1 = x => x + 1;
const kali2 = x => x * 2;

const gabung = x => kali2(tambah1(x));

console.log(gabung(3)); // (3 + 1) * 2 = 8
```

---

## 7. Currying

Mengubah fungsi dengan banyak argumen menjadi rangkaian fungsi satu argumen.

```js
function kali(a) {
  return function(b) {
    return a * b;
  }
}

const kali3 = kali(3);
console.log(kali3(5)); // 15
```

---

## 8. Kenapa Functional Programming Penting?

✅ Mudah diuji (karena pure)

✅ Tidak tergantung pada state global

✅ Cocok untuk kode paralel/async

✅ Membuat bug lebih sedikit

> JavaScript bukan bahasa FP murni, tapi mendukung gaya ini dengan sangat baik. Kamu bisa menggunakannya saat butuh menulis kode yang clean, predictable, dan reusable.

---

## 9. Library yang Mendukung FP

Kalau kamu makin dalam, bisa cek:
- [Ramda.js](https://ramdajs.com/)
- [Lodash/fp](https://github.com/lodash/lodash/wiki/FP-Guide)
- [RxJS](https://rxjs.dev/) (reaktif programming, cocok buat async event)

---

## 10. Kesimpulan

| Konsep             | Penjelasan                              |
|--------------------|------------------------------------------|
| Pure Function      | Tidak mengubah state eksternal           |
| Immutability       | Data tidak diubah langsung               |
| HOF                | Fungsi yang menerima/mengembalikan fungsi|
| Composition        | Gabungkan fungsi menjadi alur proses     |
| Currying           | Fungsi jadi rantai                       |

---

📚 Selanjutnya kita akan bahas **Object-Oriented Programming (OOP)**—biar kamu bisa bandingkan dan pilih gaya mana yang paling cocok sesuai kebutuhan proyekmu.

```
