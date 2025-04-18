
# 🔧 Fungsi di JavaScript

Fungsi adalah sekumpulan kode yang bisa digunakan kembali untuk melakukan tugas tertentu. Fungsi bisa menerima input (parameter) dan mengembalikan hasil (output). Fungsi membantu membuat kode lebih terstruktur, modular, dan lebih mudah dipelihara.

---

## 1. Deklarasi Fungsi

Fungsi bisa dideklarasikan dengan menggunakan kata kunci `function`, diikuti dengan nama fungsi, parameter (opsional), dan blok kode yang berisi logika fungsi.

### 📝 Sintaks Fungsi:
```js
function namaFungsi(parameter1, parameter2) {
  // Blok kode
  return hasil;  // Optional, tergantung kebutuhan
}
```

### 📌 Contoh Fungsi Sederhana
```js
function sapa() {
  console.log("Halo, selamat datang!");
}

sapa();  // Output: Halo, selamat datang!
```

---

## 2. Fungsi dengan Parameter

Parameter adalah input yang diberikan ke dalam fungsi. Fungsi bisa menerima lebih dari satu parameter.

### 📝 Contoh Fungsi dengan Parameter
```js
function tambah(a, b) {
  return a + b;
}

let hasil = tambah(5, 3);  // Memanggil fungsi dengan argumen 5 dan 3
console.log(hasil);         // Output: 8
```

---

## 3. Fungsi dengan Return Value

Fungsi dapat mengembalikan (return) nilai setelah melakukan operasi. Nilai yang dikembalikan bisa disimpan dalam variabel atau langsung digunakan.

### 📝 Contoh Fungsi dengan Return
```js
function kali(a, b) {
  return a * b;
}

let hasil = kali(4, 5);  // Memanggil fungsi dan menyimpan hasilnya
console.log(hasil);       // Output: 20
```

---

## 4. Fungsi Anonim (Anonymous Function)

Fungsi anonim adalah fungsi yang tidak memiliki nama dan sering digunakan di tempat-tempat yang membutuhkan fungsi sementara, seperti dalam event handler atau callback.

### 📝 Contoh Fungsi Anonim
```js
let salam = function() {
  console.log("Halo, dunia!");
};

salam();  // Output: Halo, dunia!
```

---

## 5. Fungsi Arrow (Arrow Function) — ES6

Fungsi arrow (fungsi panah) adalah sintaks yang lebih ringkas untuk mendeklarasikan fungsi, dan memiliki `this` yang berbeda dengan fungsi biasa.

### 📝 Sintaks Arrow Function
```js
const namaFungsi = (parameter1, parameter2) => {
  // Blok kode
  return hasil;
}
```

### 📌 Contoh Arrow Function
```js
const kurang = (a, b) => a - b;

let hasil = kurang(9, 4);
console.log(hasil);  // Output: 5
```

### 📝 Arrow Function Tanpa Parameter
```js
const sapa = () => console.log("Selamat pagi!");
sapa();  // Output: Selamat pagi!
```

---

## 6. Fungsi sebagai Parameter (Callback)

Kamu bisa mengirimkan fungsi sebagai parameter ke fungsi lain. Fungsi ini sering disebut **callback function**.

### 📝 Contoh Fungsi Callback
```js
function prosesAngka(angka, operasi) {
  return operasi(angka);
}

let hasil1 = prosesAngka(5, function(num) {
  return num * num;  // Memanggil fungsi anonim untuk mengkuadratkan angka
});

let hasil2 = prosesAngka(10, num => num - 2);  // Menggunakan arrow function
console.log(hasil1);  // Output: 25
console.log(hasil2);  // Output: 8
```

---

## 7. Fungsi dengan Parameter Default (Default Parameters) — ES6

Kadang kita ingin memberi nilai default pada parameter fungsi jika tidak ada argumen yang diberikan. Ini bisa dilakukan dengan **default parameter**.

### 📝 Contoh Default Parameter
```js
function sapa(nama = "Guest") {
  console.log("Halo, " + nama);
}

sapa();         // Output: Halo, Guest
sapa("Marno");  // Output: Halo, Marno
```

---

## 8. Fungsi Rekursif

Fungsi rekursif adalah fungsi yang memanggil dirinya sendiri untuk menyelesaikan masalah. Fungsi ini biasanya digunakan untuk menyelesaikan masalah yang memiliki struktur yang bersifat berulang, seperti menghitung faktorial atau fibonacci.

### 📝 Contoh Fungsi Rekursif: Faktorial
```js
function faktorial(n) {
  if (n === 0) {  // Basis dari rekursi
    return 1;
  }
  return n * faktorial(n - 1);  // Rekursi
}

console.log(faktorial(5));  // Output: 120
```

---

## 9. Fungsi dengan Rest Parameter (Rest Parameters) — ES6

Rest parameter memungkinkan kita untuk mengumpulkan parameter fungsi yang tidak terbatas jumlahnya menjadi sebuah array.

### 📝 Contoh Rest Parameter
```js
function hitungTotal(...angka) {
  return angka.reduce((total, num) => total + num, 0);
}

console.log(hitungTotal(1, 2, 3, 4));  // Output: 10
```

---

## 🎯 Kesimpulan

- **Fungsi** adalah blok kode yang dapat digunakan kembali untuk menyelesaikan tugas tertentu.
- Fungsi dapat memiliki **parameter** untuk menerima input dan **mengembalikan nilai** (menggunakan `return`).
- Ada beberapa tipe fungsi seperti **fungsi anonim**, **arrow function**, dan **fungsi rekursif**.
- **Rest parameter** memungkinkan kita untuk menangani jumlah parameter yang fleksibel.

Selanjutnya, kita akan belajar tentang **Struktur Kontrol** seperti `if`, `switch`, dan `loop`. Siap untuk mulai percabangan dan perulangan? Yuk lanjut!
```
