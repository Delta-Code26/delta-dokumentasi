
# 🏗️ Higher-Order Functions di JavaScript

Fungsi tingkat tinggi (**Higher-Order Functions**) adalah fungsi yang menerima satu atau lebih fungsi sebagai argumen atau mengembalikan fungsi sebagai hasil. Ini adalah konsep dasar dalam pemrograman fungsional dan digunakan secara luas dalam JavaScript untuk menangani koleksi data, manipulasi fungsi, dan banyak lagi.

---

## 1. Apa itu Higher-Order Functions?

Fungsi disebut **higher-order** jika:
- Fungsi tersebut menerima satu atau lebih fungsi sebagai argumen.
- Fungsi tersebut mengembalikan fungsi lain.

Konsep ini memungkinkan kita untuk membuat kode lebih modular dan terstruktur, serta membuat fungsi lebih fleksibel dan dapat digunakan kembali.

### 📌 Contoh Fungsi Tingkat Tinggi

Berikut adalah contoh fungsi yang menerima fungsi sebagai argumen:

```js
function greet(name, callback) {
  return `Hello, ${name}. ${callback()}`;
}

function sayGoodbye() {
  return "Goodbye!";
}

console.log(greet("John", sayGoodbye)); // Output: Hello, John. Goodbye!
```

Di sini, fungsi `greet()` adalah fungsi tingkat tinggi karena menerima fungsi `sayGoodbye()` sebagai argumen.

---

## 2. Fungsi yang Mengembalikan Fungsi

Selain menerima fungsi sebagai argumen, fungsi tingkat tinggi juga bisa mengembalikan fungsi sebagai hasil. Berikut adalah contoh sederhana fungsi yang mengembalikan fungsi:

```js
function multiplyBy(factor) {
  return function(number) {
    return number * factor;
  };
}

const multiplyBy2 = multiplyBy(2);
console.log(multiplyBy2(5)); // Output: 10
```

Fungsi `multiplyBy()` mengembalikan fungsi lain yang kemudian digunakan untuk mengalikan angka dengan faktor yang ditentukan.

---

## 3. Fungsi-fungsi Tingkat Tinggi dalam JavaScript

JavaScript memiliki banyak metode built-in yang merupakan contoh dari **higher-order functions**. Beberapa di antaranya adalah metode array seperti **map()**, **filter()**, dan **reduce()**.

### 📌 `map()`

Metode `map()` digunakan untuk membuat array baru dengan hasil pemanggilan fungsi pada setiap elemen dalam array.

```js
const numbers = [1, 2, 3, 4];
const doubled = numbers.map(num => num * 2);
console.log(doubled); // Output: [2, 4, 6, 8]
```

Fungsi yang diberikan pada `map()` dipanggil pada setiap elemen array, menghasilkan array baru dengan nilai yang dimodifikasi.

### 📌 `filter()`

Metode `filter()` digunakan untuk membuat array baru yang hanya berisi elemen-elemen yang memenuhi kriteria yang ditentukan dalam fungsi.

```js
const numbers = [1, 2, 3, 4, 5];
const evenNumbers = numbers.filter(num => num % 2 === 0);
console.log(evenNumbers); // Output: [2, 4]
```

Di sini, fungsi yang diberikan pada `filter()` akan menyaring elemen-elemen yang genap dari array.

### 📌 `reduce()`

Metode `reduce()` digunakan untuk mengakumulasi nilai array menjadi satu nilai tunggal berdasarkan fungsi yang diberikan.

```js
const numbers = [1, 2, 3, 4];
const sum = numbers.reduce((acc, num) => acc + num, 0);
console.log(sum); // Output: 10
```

Fungsi yang diberikan pada `reduce()` menerima dua argumen: akumulator (`acc`) dan elemen saat ini (`num`). Setiap iterasi, nilai akumulator akan diperbarui dengan hasil fungsi tersebut.

---

## 4. Membuat Fungsi Tingkat Tinggi Sendiri

Kita bisa membuat fungsi tingkat tinggi yang lebih kompleks, seperti fungsi yang menggabungkan beberapa fungsi atau fungsi yang memodifikasi perilaku fungsi lain.

### 📌 Contoh: Fungsi `once()`

Fungsi `once()` memastikan bahwa fungsi yang diberikan hanya akan dipanggil satu kali, tidak lebih.

```js
function once(fn) {
  let called = false;
  return function() {
    if (!called) {
      fn();
      called = true;
    }
  };
}

const sayHelloOnce = once(() => console.log("Hello!"));
sayHelloOnce(); // Output: Hello!
sayHelloOnce(); // Tidak ada output
```

Fungsi `once()` adalah contoh dari fungsi tingkat tinggi yang mengembalikan fungsi lain, yang hanya dapat dipanggil sekali.

---

## 5. Fungsi `bind()`, `call()`, dan `apply()`

Metode `bind()`, `call()`, dan `apply()` adalah contoh fungsi tingkat tinggi yang sering digunakan untuk mengubah konteks eksekusi suatu fungsi.

### 📌 `bind()`

Metode `bind()` mengembalikan fungsi baru yang memiliki konteks tertentu (nilai `this`).

```js
const person = {
  name: "Alice",
  greet() {
    console.log(`Hello, ${this.name}`);
  }
};

const greetAlice = person.greet.bind(person);
greetAlice(); // Output: Hello, Alice
```

Dengan `bind()`, kita dapat mengikat fungsi ke objek tertentu.

### 📌 `call()` dan `apply()`

Metode `call()` dan `apply()` digunakan untuk memanggil fungsi dengan konteks tertentu, tetapi cara pengoperasian argumen berbeda.

```js
function greet(greeting, punctuation) {
  console.log(`${greeting}, ${this.name}${punctuation}`);
}

const person = { name: "Bob" };

greet.call(person, "Hello", "!"); // Output: Hello, Bob!
greet.apply(person, ["Hello", "!"]); // Output: Hello, Bob!
```

Kedua metode ini memungkinkan kita untuk mengubah konteks (`this`) dan memanggil fungsi dengan parameter yang ditentukan.

---

## 6. Keuntungan dan Kelemahan Fungsi Tingkat Tinggi

### ✅ Keuntungan

- **Modularitas**: Fungsi tingkat tinggi memungkinkan kita untuk memecah masalah besar menjadi bagian-bagian kecil yang lebih mudah dikelola.
- **Reusable**: Fungsi yang menerima atau mengembalikan fungsi lain dapat digunakan kembali di berbagai tempat.
- **Mempermudah Asinkronus**: Fungsi tingkat tinggi sering digunakan dalam penanganan asinkronus seperti callback, promise, dan async/await.

### ❌ Kelemahan

- **Kompleksitas**: Terlalu banyak penggunaan fungsi tingkat tinggi bisa membuat kode menjadi lebih sulit dimengerti.
- **Performa**: Jika tidak digunakan dengan bijak, fungsi tingkat tinggi bisa berdampak pada performa, terutama dalam operasi berulang pada data besar.

---

## 7. Kesimpulan

Fungsi tingkat tinggi (Higher-Order Functions) adalah konsep penting dalam pemrograman JavaScript yang memungkinkan kita untuk menulis kode yang lebih modular dan fleksibel. Dengan menggunakan fungsi-fungsi seperti `map()`, `filter()`, dan `reduce()`, kita bisa lebih mudah menangani koleksi data. Memahami cara kerja fungsi tingkat tinggi adalah keterampilan yang sangat berharga dalam menulis kode yang efisien dan terstruktur.

Sekarang, kita telah membahas tentang fungsi tingkat tinggi di JavaScript. Selanjutnya, kita akan melihat bagaimana konsep-konsep ini digunakan dalam berbagai pustaka dan framework JavaScript.
```
