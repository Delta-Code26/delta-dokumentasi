
# 🔡 Variabel di JavaScript

Variabel adalah **wadah** untuk menyimpan data. Kayak laci—kita taruh sesuatu di dalamnya, terus kita bisa ambil lagi nanti.

Di JavaScript, kita bisa buat variabel dengan 3 cara:

```js
var
let
const
```

---

## 🧓 `var` — Yang Tua Tapi Masih Ada

```js
var nama = "Marno";
console.log(nama); // Output: Marno
```

### ⚠️ Tapi hati-hati:
- Bisa dideklarasi ulang (`redeclaration`)
- Scope-nya **function**, bukan block
- Kena **hoisting** (naik ke atas)

> 🚫 **Saran**: Hindari `var`, karena sering bikin bug misterius

---

## 🧑‍💻 `let` — Favorit Developer

```js
let umur = 25;
umur = 26; // ✅ bisa diubah
console.log(umur);
```

### ✅ Kelebihan:
- Scope-nya **block** (aman!)
- Tidak bisa dideklarasi ulang dalam scope yang sama

```js
let umur = 25;
let umur = 30; // ❌ error
```

---

## 🔒 `const` — Konstanta, Tetap Selamanya

```js
const negara = "Malaysia";
console.log(negara);
```

### ⚠️ Catatan:
- **Tidak bisa diubah nilainya**
- Tapi kalau isi-nya object atau array, isinya bisa diubah:

```js
const data = [1, 2, 3];
data.push(4);       // ✅ Boleh
data = [1, 2, 3, 4]; // ❌ Error
```

---

## 🔍 Perbandingan Cepat

| Keyword | Bisa diubah | Bisa deklarasi ulang | Scope    | Hoisting |
|--------|--------------|-----------------------|----------|----------|
| `var`  | ✅ Ya         | ✅ Ya                 | Function | ✅ Ya     |
| `let`  | ✅ Ya         | ❌ Tidak              | Block    | ❌ Tidak  |
| `const`| ❌ Tidak      | ❌ Tidak              | Block    | ❌ Tidak  |

---

## 🧠 Tips & Best Practice

✅ Gunakan `const` **by default**  
🔁 Gunakan `let` **jika perlu mengubah nilainya**  
❌ Hindari `var`, kecuali kamu lagi audit kode zaman Majapahit

---

## 🎯 Contoh Real-life

```js
const namaDepan = "Andi";
let saldo = 10000;

saldo += 5000;

console.log(`Halo ${namaDepan}, saldo Anda: Rp${saldo}`);
```

Output:
```
Halo Andi, saldo Anda: Rp15000
```

---

## 💬 Kesimpulan

- Variabel = tempat simpan data
- Gunakan `let` dan `const`, jauhi `var`
- Pahami scope dan mutability (bisa diubah atau tidak)

Selanjutnya kita akan bahas tentang **Tipe Data**. Yuk lanjut!
```
