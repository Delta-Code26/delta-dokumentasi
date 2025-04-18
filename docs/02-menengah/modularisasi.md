
# 🧩 Modularisasi di JavaScript

Modularisasi adalah teknik memecah program besar menjadi bagian-bagian kecil (modul) yang terpisah dan mandiri. Setiap modul memiliki tanggung jawab spesifik dan bisa digunakan kembali. Konsep ini sangat penting untuk menjaga kode tetap rapi, terorganisir, dan mudah dipelihara.

---

## 1. Mengapa Perlu Modularisasi?

Tanpa modularisasi, kode JavaScript bisa jadi seperti mi instan yang kebanyakan bumbu—berantakan dan susah dipisah. Modularisasi membantu:

- Memecah kode menjadi bagian kecil yang terpisah.
- Menghindari penulisan ulang kode (reusability).
- Memudahkan testing, debugging, dan pengembangan tim.
- Meningkatkan keterbacaan dan maintainability.

---

## 2. Modularisasi Tradisional: IIFE & Namespace

Sebelum ES6, kita menggunakan **IIFE** (Immediately Invoked Function Expression) dan objek global sebagai "namespace".

### 📌 IIFE (Immediately Invoked Function Expression)

```js
const MyModule = (function() {
  const privateVar = "Rahasia";

  function privateFunc() {
    console.log("Fungsi private");
  }

  return {
    publicFunc: function() {
      console.log("Fungsi public");
    }
  };
})();

MyModule.publicFunc(); // Fungsi public
```

### 📌 Namespace (Objek Global)

```js
const App = {};
App.sayHello = function(name) {
  console.log(`Hello, ${name}`);
};
App.sayHello("Marno");
```

Kelemahannya: bisa terjadi konflik jika banyak modul memakai nama yang sama di global scope.

---

## 3. Modularisasi Modern dengan ES Modules (ESM)

Sejak ES6, JavaScript mendukung modularisasi native lewat **`import`** dan **`export`**.

### 🛠️ Export

Ada dua jenis export: **named export** dan **default export**.

#### Named Export

```js
// file: math.js
export const PI = 3.14;
export function tambah(a, b) {
  return a + b;
}
```

#### Default Export

```js
// file: greet.js
export default function(name) {
  console.log(`Hello, ${name}`);
}
```

### 📥 Import

#### Import Named

```js
// file: main.js
import { PI, tambah } from './math.js';

console.log(tambah(2, 3)); // 5
```

#### Import Default

```js
// file: main.js
import greet from './greet.js';

greet('Marno'); // Hello, Marno
```

#### Import Semua

```js
import * as MathUtils from './math.js';

console.log(MathUtils.PI);
```

---

## 4. Struktur Proyek Modular

Struktur folder modular sangat membantu dalam skala besar:

```
📦project
 ┣ 📂modules
 ┃ ┣ 📜math.js
 ┃ ┣ 📜user.js
 ┣ 📜main.js
```

Contoh isi `math.js`:

```js
export function tambah(a, b) {
  return a + b;
}

export function kurang(a, b) {
  return a - b;
}
```

Lalu digunakan di `main.js`:

```js
import { tambah, kurang } from './modules/math.js';

console.log(tambah(10, 5)); // 15
```

---

## 5. Modularisasi di Node.js (CommonJS)

Jika kamu menggunakan Node.js, format modul sedikit berbeda (CommonJS).

### 📦 Export

```js
// file: utils.js
const sayHello = (name) => {
  console.log(`Hi, ${name}`);
};

module.exports = { sayHello };
```

### 📥 Import

```js
// file: index.js
const { sayHello } = require('./utils');
sayHello('Marno');
```

> Catatan: CommonJS masih dominan di banyak proyek Node.js, tapi bisa diganti ke ES Module (`"type": "module"` di `package.json`) jika dibutuhkan.

---

## 6. Tips Modularisasi

- 💡 Satu file, satu tanggung jawab. Jangan gabung semua fungsi dalam satu file.
- 📁 Gunakan folder untuk memisahkan domain aplikasi.
- ✨ Gunakan `index.js` untuk ekspor ulang semua modul dari folder.

Contoh:

```js
// file: modules/index.js
export * from './math.js';
export * from './user.js';
```

---

## 7. Kesimpulan

Modularisasi bikin hidup (dan ngoding) lebih damai. Dengan memecah kode jadi bagian-bagian kecil dan terpisah, kita bisa:

- Bekerja lebih cepat
- Menulis kode lebih bersih
- Mengelola proyek besar tanpa stres

Mulai biasakan diri untuk menulis kode yang modular, karena ini jadi fondasi utama dalam membangun aplikasi modern, baik di frontend maupun backend.

---

> 📚 Selanjutnya kita akan belajar tentang `NPM` dan cara menggunakan package pihak ketiga untuk memperkuat modul kita layaknya upgrade karakter di game RPG. Stay tuned!
```
