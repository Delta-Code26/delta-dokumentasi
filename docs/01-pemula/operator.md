
# ➗ Operator di JavaScript

Operator digunakan untuk melakukan operasi pada variabel dan nilai. Di JavaScript, ada berbagai jenis operator yang bisa digunakan untuk berbagai keperluan.

---

## 1. Operator Aritmatika

Operator aritmatika digunakan untuk melakukan operasi matematika seperti penjumlahan, pengurangan, perkalian, dan pembagian.

### 🔢 **Penjumlahan (+)**
```js
let a = 5;
let b = 3;
let hasil = a + b;  // 8
console.log(hasil);
```

### ➖ **Pengurangan (-)**
```js
let a = 10;
let b = 4;
let hasil = a - b;  // 6
console.log(hasil);
```

### ✖️ **Perkalian (*)**
```js
let a = 4;
let b = 2;
let hasil = a * b;  // 8
console.log(hasil);
```

### ➗ **Pembagian (/)**
```js
let a = 10;
let b = 2;
let hasil = a / b;  // 5
console.log(hasil);
```

### ➗ **Modulus (%)**
Operator modulus memberikan sisa hasil bagi.
```js
let a = 10;
let b = 3;
let hasil = a % b;  // 1
console.log(hasil);
```

### 🔼 **Pangkatkan (**)**
Operator eksponen digunakan untuk menghitung pangkat.
```js
let a = 2;
let b = 3;
let hasil = a ** b;  // 8 (2^3)
console.log(hasil);
```

---

## 2. Operator Penugasan

Operator penugasan digunakan untuk memberikan nilai pada variabel.

### 📝 **Tugas (=)**
```js
let x = 5;
```

### ➕ Penugasan dengan Penjumlahan (+=)
```js
let x = 10;
x += 5;  // x = x + 5
console.log(x); // Output: 15
```

### ➖ Penugasan dengan Pengurangan (-=)
```js
let x = 10;
x -= 5;  // x = x - 5
console.log(x); // Output: 5
```

### ✖️ Penugasan dengan Perkalian (*=)
```js
let x = 10;
x *= 2;  // x = x * 2
console.log(x); // Output: 20
```

### ➗ Penugasan dengan Pembagian (/=)
```js
let x = 20;
x /= 4;  // x = x / 4
console.log(x); // Output: 5
```

---

## 3. Operator Perbandingan

Operator perbandingan digunakan untuk membandingkan dua nilai dan menghasilkan nilai Boolean (`true` atau `false`).

### 🏆 **Sama dengan (==)**
```js
let a = 5;
let b = 5;
console.log(a == b);  // Output: true
```

### 🛑 **Tidak sama dengan (!=)**
```js
let a = 5;
let b = 3;
console.log(a != b);  // Output: true
```

### 🧑‍🤝‍🧑 **Sama dengan secara tipe dan nilai (===)**
```js
let a = 5;
let b = "5";
console.log(a === b);  // Output: false (tipe berbeda)
```

### ❌ **Tidak sama dengan secara tipe dan nilai (!==)**
```js
let a = 5;
let b = "5";
console.log(a !== b);  // Output: true (tipe berbeda)
```

### 🔼 **Lebih besar dari (>)**
```js
let a = 5;
let b = 3;
console.log(a > b);  // Output: true
```

### 🔽 **Lebih kecil dari (<)**
```js
let a = 3;
let b = 5;
console.log(a < b);  // Output: true
```

### 📏 **Lebih besar atau sama dengan (>=)**
```js
let a = 5;
let b = 5;
console.log(a >= b);  // Output: true
```

### 📏 **Lebih kecil atau sama dengan (<=)**
```js
let a = 3;
let b = 5;
console.log(a <= b);  // Output: true
```

---

## 4. Operator Logika

Operator logika digunakan untuk menggabungkan beberapa kondisi.

### 🟢 **AND (&&)**

Mengevaluasi menjadi `true` jika kedua kondisi benar.

```js
let a = 5;
let b = 10;
console.log(a > 0 && b > 5);  // Output: true
```

### 🔴 **OR (||)**

Mengevaluasi menjadi `true` jika salah satu kondisi benar.

```js
let a = 5;
let b = 3;
console.log(a > 0 || b > 5);  // Output: true
```

### ❌ **NOT (!)**
Mengevaluasi kebalikan dari kondisi.

```js
let a = true;
console.log(!a);  // Output: false
```

---

## 5. Operator Ternary

Operator ternary adalah cara singkat untuk menulis `if`-`else` dalam satu baris.

```js
let usia = 18;
let status = usia >= 18 ? "Dewasa" : "Anak-anak";
console.log(status);  // Output: Dewasa
```

---

## 6. Operator Bitwise (Lanjutan)

Operator bitwise beroperasi pada level bit. Biasanya digunakan untuk optimasi atau manipulasi bit-level dalam aplikasi yang membutuhkan performa tinggi.

Contoh penggunaan:
```js
let a = 5;  // 0101
let b = 3;  // 0011
console.log(a & b);  // Output: 1 (0101 & 0011)
```

---

## 🎯 Kesimpulan

- **Operator Aritmatika**: Digunakan untuk operasi matematika dasar seperti penjumlahan, pengurangan, dll.
- **Operator Penugasan**: Memudahkan kita dalam memberi nilai dan melakukan operasi langsung pada variabel.
- **Operator Perbandingan**: Digunakan untuk membandingkan dua nilai, hasilnya adalah `true` atau `false`.
- **Operator Logika**: Digunakan untuk menggabungkan beberapa kondisi logika.
- **Operator Ternary**: Cara singkat untuk membuat percabangan dengan satu baris kode.

Selanjutnya, kita akan belajar tentang **Struktur Kontrol** (if, switch, loop). Yuk lanjut!
```
