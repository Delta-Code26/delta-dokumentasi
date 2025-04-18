
# 🛠️ Struktur Kontrol di JavaScript

Struktur kontrol adalah cara untuk menentukan jalannya eksekusi program berdasarkan kondisi tertentu atau mengulangi operasi. Di JavaScript, ada beberapa jenis struktur kontrol seperti percabangan dan perulangan.

---

## 1. Percabangan (Conditional Statements)

Percabangan memungkinkan kita untuk mengevaluasi kondisi dan mengeksekusi kode berdasarkan hasil evaluasi tersebut.

### 📌 **If Statement**
`if` digunakan untuk mengevaluasi sebuah kondisi. Jika kondisi tersebut benar (true), maka kode di dalam blok `if` akan dieksekusi.

```js
let angka = 10;
if (angka > 5) {
  console.log("Angka lebih besar dari 5");
}
```

### 📌 **If-Else Statement**
`if-else` memungkinkan kita untuk mengevaluasi kondisi dan memberikan alternatif jika kondisi tersebut tidak benar (false).

```js
let angka = 3;
if (angka > 5) {
  console.log("Angka lebih besar dari 5");
} else {
  console.log("Angka tidak lebih besar dari 5");
}
```

### 📌 **If-Else If-Else Statement**
Jika kamu memiliki lebih dari dua kondisi yang perlu dievaluasi, kamu bisa menggunakan `else if` untuk memeriksa kondisi lain.

```js
let angka = 7;
if (angka > 10) {
  console.log("Angka lebih besar dari 10");
} else if (angka > 5) {
  console.log("Angka lebih besar dari 5 tapi kurang dari atau sama dengan 10");
} else {
  console.log("Angka kurang dari atau sama dengan 5");
}
```

---

## 2. Operator Logika untuk Percabangan

Operator logika sering digunakan dalam kondisi `if` untuk mengevaluasi beberapa kondisi sekaligus.

### 📌 **AND (&&)**
`&&` digunakan untuk memastikan semua kondisi dalam `if` bernilai `true`.

```js
let a = 5;
let b = 10;
if (a > 0 && b > 5) {
  console.log("Kedua kondisi benar");
}
```

### 📌 **OR (||)**
`||` digunakan untuk memastikan salah satu kondisi dalam `if` bernilai `true`.

```js
let a = 3;
let b = 10;
if (a > 0 || b > 5) {
  console.log("Salah satu kondisi benar");
}
```

### 📌 **NOT (!)**
`!` digunakan untuk membalikkan nilai dari kondisi.

```js
let a = true;
if (!a) {
  console.log("Kondisi a adalah false");
} else {
  console.log("Kondisi a adalah true");
}
```

---

## 3. Switch Statement

`switch` digunakan untuk memeriksa nilai dari suatu ekspresi terhadap beberapa kemungkinan nilai yang disebut dengan *case*. Jika nilai ekspresi cocok dengan salah satu `case`, maka kode dalam blok `case` tersebut akan dieksekusi.

### 📌 **Sintaks Switch**
```js
let warna = "merah";
switch (warna) {
  case "merah":
    console.log("Ini adalah warna merah");
    break;
  case "biru":
    console.log("Ini adalah warna biru");
    break;
  default:
    console.log("Warna tidak dikenali");
}
```

### 📌 **Penjelasan:**
- **`case`**: Mengecek apakah ekspresi cocok dengan nilai tersebut.
- **`break`**: Menghentikan eksekusi setelah menemukan kecocokan.
- **`default`**: Jika tidak ada yang cocok dengan `case`, maka blok kode di `default` yang akan dieksekusi.

---

## 4. Perulangan (Loops)

Perulangan digunakan untuk mengulangi eksekusi kode beberapa kali berdasarkan kondisi tertentu.

### 📌 **For Loop**
`for` digunakan ketika kita tahu jumlah iterasi yang pasti. Biasanya digunakan untuk perulangan dengan angka yang terstruktur.

```js
for (let i = 0; i < 5; i++) {
  console.log(i);  // Output: 0 1 2 3 4
}
```

### 📌 **While Loop**
`while` digunakan ketika kita tidak tahu berapa kali perulangan yang akan dilakukan, tapi ingin melanjutkan selama kondisi tertentu terpenuhi.

```js
let i = 0;
while (i < 5) {
  console.log(i);  // Output: 0 1 2 3 4
  i++;
}
```

### 📌 **Do-While Loop**
`do-while` mirip dengan `while`, tetapi perbedaan utamanya adalah kode di dalam blok `do` akan dijalankan setidaknya sekali, bahkan jika kondisinya salah.

```js
let i = 0;
do {
  console.log(i);  // Output: 0 1 2 3 4
  i++;
} while (i < 5);
```

---

## 5. Break dan Continue

`break` dan `continue` adalah dua perintah yang dapat digunakan untuk mengontrol alur perulangan.

### 📌 **Break**
`break` digunakan untuk keluar dari perulangan, meskipun kondisi perulangan masih memenuhi.

```js
for (let i = 0; i < 5; i++) {
  if (i === 3) {
    break;  // Menghentikan perulangan saat i = 3
  }
  console.log(i);  // Output: 0 1 2
}
```

### 📌 **Continue**
`continue` digunakan untuk melewati sisa iterasi saat kondisi tertentu dipenuhi dan melanjutkan ke iterasi berikutnya.

```js
for (let i = 0; i < 5; i++) {
  if (i === 3) {
    continue;  // Melewati iterasi saat i = 3
  }
  console.log(i);  // Output: 0 1 2 4
}
```

---

## 🎯 Kesimpulan

- **Percabangan**: Gunakan `if`, `else if`, dan `else` untuk mengevaluasi kondisi dan membuat keputusan.
- **Switch**: Digunakan untuk memilih antara banyak kondisi dengan cara yang lebih terstruktur.
- **Perulangan**: Gunakan `for`, `while`, atau `do-while` untuk mengulangi kode berdasarkan kondisi.
- **Break dan Continue**: Kontrol alur perulangan dengan `break` (keluar dari perulangan) dan `continue` (melanjutkan ke iterasi berikutnya).

Sekarang, kamu sudah siap untuk mulai mengendalikan alur program menggunakan percabangan dan perulangan! Selanjutnya, kita akan belajar tentang **Array** dan bagaimana cara menyimpan dan mengelola data dalam JavaScript.
```

---

Itu dia, penjelasan lengkap tentang **Control Flow** di JavaScript! Kalau sudah oke, aku siap untuk lanjut ke materi berikutnya, atau kalau ada bagian yang perlu diubah atau ditambah, tinggal kasih tahu!