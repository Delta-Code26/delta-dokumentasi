
# 🧮 Tipe Data di JavaScript

Tipe data (atau *data types*) menentukan jenis informasi yang bisa disimpan dalam variabel. Misalnya, apakah itu angka, teks, atau bahkan objek kompleks. Di JavaScript, ada beberapa tipe data yang perlu kamu kenal.

---

## 1. Tipe Data Primitif

Tipe data primitif adalah tipe data dasar yang tidak dapat diubah setelah dideklarasikan. Berikut tipe data primitif di JavaScript:

### 🔢 **Number** (Angka)
Untuk menyimpan angka, baik bulat maupun desimal.

```js
let umur = 25;           // Integer
let harga = 100.50;      // Float
let pi = 3.14159;        // Pi, decimal
```

### 🅰️ **String** (Teks)
Untuk menyimpan teks. String bisa menggunakan tanda kutip ganda (`"`) atau kutip tunggal (`'`).

```js
let nama = "Marno";
let alamat = 'Malaysia';
let kalimat = "Halo, apa kabar?";
```

### ⚖️ **Boolean** (Benar/Salah)
Hanya ada dua nilai: `true` atau `false`.

```js
let isAdmin = true;
let isLoggedIn = false;
```

### 🏆 **Null**
Tipe data ini menunjukkan bahwa variabel sengaja dikosongkan atau tidak memiliki nilai.

```js
let dataKosong = null;
```

### 🔲 **Undefined**
Tipe data ini berarti variabel belum diberi nilai sama sekali.

```js
let belumDitetapkan;
console.log(belumDitetapkan); // Output: undefined
```

### 💥 **Symbol** (ES6)
Digunakan untuk membuat nilai unik. Biasanya digunakan dalam aplikasi yang lebih kompleks.

```js
let id = Symbol("id");
console.log(id); // Output: Symbol(id)
```

### 🧩 **BigInt** (ES11)
Tipe data untuk angka yang sangat besar (lebih besar dari `Number.MAX_SAFE_INTEGER`).

```js
let angkaBesar = 1234567890123456789012345678901234567890n;
console.log(angkaBesar); // Output: 1234567890123456789012345678901234567890n
```

---

## 2. Tipe Data Non-Primitif (Referensi)

Tipe data non-primitif adalah tipe data yang bisa diubah, dan nilainya bisa mengacu ke tempat lain. Contohnya adalah **Object** dan **Array**.

### 📦 **Object**
Digunakan untuk menyimpan pasangan key-value (seperti dictionary).

```js
let person = {
  nama: "Marno",
  umur: 25,
  alamat: "Malaysia"
};

console.log(person.nama); // Output: Marno
console.log(person.umur); // Output: 25
```

### 📚 **Array**
Digunakan untuk menyimpan beberapa nilai dalam satu variabel.

```js
let warna = ["merah", "biru", "hijau"];
console.log(warna[0]); // Output: merah
console.log(warna[1]); // Output: biru
```

---

## 3. Tipe Data Lainnya

### **NaN** (Not a Number)
Tipe data ini muncul ketika operasi yang dilakukan menghasilkan nilai yang tidak valid untuk angka, seperti pembagian dengan nol.

```js
let hasil = 0 / 0;
console.log(hasil); // Output: NaN
```

### **Infinity** dan **-Infinity**
Representasi angka yang lebih besar dari angka terbesar yang bisa ditangani oleh JavaScript (positif atau negatif).

```js
let angkaPositif = 1 / 0;
let angkaNegatif = -1 / 0;

console.log(angkaPositif); // Output: Infinity
console.log(angkaNegatif); // Output: -Infinity
```

---

## 4. Konversi Tipe Data (Type Conversion)

JavaScript bisa otomatis mengonversi tipe data saat diperlukan. Namun, kamu juga bisa melakukan konversi manual:

### 🔄 **String ke Number**
```js
let angka = "123";
let angkaKeNumber = Number(angka);  // Konversi ke Number
console.log(angkaKeNumber); // Output: 123
```

### 🔄 **Number ke String**
```js
let angka = 123;
let angkaKeString = String(angka);  // Konversi ke String
console.log(angkaKeString); // Output: "123"
```

---

## 5. Tips & Best Practice

- **Gunakan tipe data yang tepat**: Pilih `Number` untuk angka, `String` untuk teks, dan `Boolean` untuk kondisi (true/false).
- **Pahami perbedaan antara `null` dan `undefined`**: `null` adalah nilai yang sengaja dihilangkan, sedangkan `undefined` berarti variabel belum diberi nilai.
- **Cek tipe data menggunakan `typeof`**:
  ```js
  console.log(typeof "Hello");   // Output: string
  console.log(typeof 25);        // Output: number
  console.log(typeof true);      // Output: boolean
  ```

---

## 🎯 Kesimpulan

- Tipe data adalah jenis informasi yang disimpan dalam variabel.
- JavaScript memiliki berbagai tipe data, baik yang primitif (Number, String, Boolean) maupun non-primitif (Object, Array).
- Pahami dan gunakan tipe data yang sesuai dengan kebutuhanmu.

Selanjutnya, kita akan bahas tentang **Operator**. Siap untuk operasi matematika dan logika? Yuk lanjut!
```
