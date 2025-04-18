
# 🗃️ Array dan Object di JavaScript

Di JavaScript, **Array** dan **Object** adalah tipe data yang digunakan untuk menyimpan koleksi data. **Array** adalah struktur data yang menyimpan beberapa nilai dalam satu variabel, sementara **Object** menyimpan data dalam bentuk pasangan key-value. Keduanya sering digunakan untuk mengelola dan memanipulasi data dalam aplikasi.

---

## 1. Array

Array adalah koleksi dari elemen-elemen yang terurut, dan setiap elemen dapat diakses dengan menggunakan indeks. Indeks array dimulai dari angka `0`.

### 📌 Membuat Array

Array dapat dibuat menggunakan tanda kurung siku `[]` dan dipisahkan dengan koma.

```js
let angka = [1, 2, 3, 4, 5];
let warna = ["merah", "biru", "hijau"];
```

### 📌 Mengakses Elemen Array

Untuk mengakses elemen di dalam array, kita menggunakan indeks.

```js
let angka = [1, 2, 3, 4, 5];
console.log(angka[0]);  // Output: 1
console.log(angka[3]);  // Output: 4
```

### 📌 Mengubah Elemen Array

Kamu bisa mengubah nilai elemen array dengan mengakses indeks tertentu dan memberi nilai baru.

```js
let warna = ["merah", "biru", "hijau"];
warna[1] = "kuning";  // Mengubah elemen kedua (indeks 1)
console.log(warna);    // Output: ["merah", "kuning", "hijau"]
```

### 📌 Menambahkan Elemen ke Array

Gunakan metode `push()` untuk menambahkan elemen di akhir array.

```js
let warna = ["merah", "biru"];
warna.push("hijau");
console.log(warna);  // Output: ["merah", "biru", "hijau"]
```

Untuk menambahkan elemen di awal array, gunakan `unshift()`.

```js
let warna = ["biru", "hijau"];
warna.unshift("merah");
console.log(warna);  // Output: ["merah", "biru", "hijau"]
```

### 📌 Menghapus Elemen dari Array

Untuk menghapus elemen dari akhir array, gunakan metode `pop()`.

```js
let warna = ["merah", "biru", "hijau"];
warna.pop();
console.log(warna);  // Output: ["merah", "biru"]
```

Untuk menghapus elemen dari awal array, gunakan `shift()`.

```js
let warna = ["merah", "biru", "hijau"];
warna.shift();
console.log(warna);  // Output: ["biru", "hijau"]
```

### 📌 Array Length

Kamu bisa mendapatkan jumlah elemen dalam array dengan menggunakan properti `length`.

```js
let warna = ["merah", "biru", "hijau"];
console.log(warna.length);  // Output: 3
```

---

## 2. Object

Object adalah tipe data yang digunakan untuk menyimpan data dalam bentuk pasangan **key-value**. Setiap **key** berfungsi sebagai identifikasi dan **value** adalah data yang terkait dengan key tersebut.

### 📌 Membuat Object

Object dapat dibuat menggunakan tanda kurung kurawal `{}` dan pasangan key-value dipisahkan dengan tanda titik dua `:`.

```js
let mobil = {
  merek: "Toyota",
  model: "Corolla",
  tahun: 2020
};
```

### 📌 Mengakses Nilai dalam Object

Untuk mengakses nilai dalam object, kamu bisa menggunakan **dot notation** atau **bracket notation**.

#### **Dot Notation**
```js
console.log(mobil.merek);  // Output: "Toyota"
console.log(mobil.tahun);  // Output: 2020
```

#### **Bracket Notation**
```js
console.log(mobil["merek"]);  // Output: "Toyota"
console.log(mobil["model"]);  // Output: "Corolla"
```

### 📌 Menambah atau Mengubah Properti Object

Untuk menambah atau mengubah properti, kamu bisa menggunakan **dot notation** atau **bracket notation**.

```js
mobil.warna = "Hitam";  // Menambahkan properti warna
mobil["harga"] = 20000; // Menambahkan properti harga
console.log(mobil);
```

Jika properti sudah ada, maka nilainya akan diubah.

```js
mobil.merek = "Honda";  // Mengubah nilai properti merek
console.log(mobil.merek);  // Output: "Honda"
```

### 📌 Menghapus Properti Object

Untuk menghapus properti dalam object, kamu bisa menggunakan operator `delete`.

```js
delete mobil.tahun;
console.log(mobil);  // Output: { merek: "Honda", model: "Corolla", warna: "Hitam", harga: 20000 }
```

### 📌 Mengakses Semua Key dan Value dalam Object

Untuk mendapatkan semua **key** dari object, kamu bisa menggunakan `Object.keys()`. Sedangkan untuk mendapatkan semua **value**, gunakan `Object.values()`.

```js
let mobil = {
  merek: "Honda",
  model: "Civic",
  tahun: 2021
};

console.log(Object.keys(mobil));  // Output: ["merek", "model", "tahun"]
console.log(Object.values(mobil));  // Output: ["Honda", "Civic", 2021]
```

---

## 3. Array of Objects

Seringkali kita bekerja dengan array yang berisi objek-objek, terutama dalam situasi di mana kita perlu menyimpan koleksi data kompleks, seperti daftar pengguna, produk, atau entitas lainnya.

### 📌 Contoh Array of Objects
```js
let users = [
  { id: 1, nama: "John", usia: 30 },
  { id: 2, nama: "Jane", usia: 25 },
  { id: 3, nama: "Bob", usia: 35 }
];

console.log(users[1].nama);  // Output: "Jane"
```

---

## 🎯 Kesimpulan

- **Array**: Digunakan untuk menyimpan daftar data yang terurut. Elemen-elemen array diakses menggunakan indeks, dimulai dari `0`.
- **Object**: Digunakan untuk menyimpan data dalam bentuk pasangan key-value, yang memungkinkan kita untuk mengakses nilai menggunakan key.
- **Array of Objects**: Sering digunakan untuk menyimpan koleksi objek dengan struktur yang lebih kompleks, seperti daftar pengguna atau produk.

Dengan memahami cara kerja Array dan Object, kamu akan lebih mudah mengelola data dalam aplikasi JavaScript! Sekarang, kita akan lanjut ke pembahasan tentang **Fungsi Array** dan berbagai metode untuk memanipulasi array.
```
