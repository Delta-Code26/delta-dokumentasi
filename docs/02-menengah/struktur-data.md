
# 🧱 Struktur Data di JavaScript

Struktur data adalah cara menyimpan dan mengorganisasi data agar mudah digunakan secara efisien. JavaScript menyediakan beberapa struktur data bawaan yang penting untuk dipahami—terutama saat membangun aplikasi yang lebih kompleks.

Di level ini, kita akan bahas:

- Array
- Object
- Set
- Map
- WeakSet & WeakMap (bonus buat yang suka deep dive)

---

## 1. Array Revisit 🔁

Kita udah kenalan sama array di level pemula, tapi sekarang kita bahas fitur-fitur lanjutannya.

### Metode Penting Array:

| Method        | Fungsi                                      |
|---------------|---------------------------------------------|
| `push()`      | Menambah elemen di akhir array              |
| `pop()`       | Menghapus elemen terakhir dari array        |
| `shift()`     | Menghapus elemen pertama                    |
| `unshift()`   | Menambah elemen di awal array               |
| `slice()`     | Mengambil sebagian array (tidak merusak asli) |
| `splice()`    | Menambah/menghapus elemen (modifikasi array) |
| `map()`       | Membuat array baru dari setiap elemen       |
| `filter()`    | Menyaring elemen                            |
| `reduce()`    | Menggabungkan nilai                        |

### Contoh:

```js
const angka = [1, 2, 3, 4, 5];
const hasil = angka.map(num => num * 2); // [2, 4, 6, 8, 10]
```

---

## 2. Object Revisit 🧰

Object menyimpan data dalam bentuk pasangan key-value.

```js
const user = {
  nama: "Marno",
  umur: 22,
  alamat: "Kebun Sawit"
};

console.log(user["nama"]);     // Marno
console.log(user.umur);        // 22
```

### Fitur Modern:

- **Destructuring**: memecah object jadi variabel
- **Optional Chaining**: akses properti dengan aman
- **Spread Operator**: menggabungkan atau menyalin object

```js
const { nama, umur } = user;
console.log(nama); // Marno
```

---

## 3. Set 🧺

`Set` adalah koleksi nilai unik. Gak ada elemen duplikat.

```js
const buah = new Set(["apel", "mangga", "apel"]);
console.log(buah); // Set { 'apel', 'mangga' }
```

### Metode Set:

- `add()`
- `delete()`
- `has()`
- `size`

---

## 4. Map 🗺️

`Map` mirip object, tapi key-nya bisa tipe data apapun dan teratur berdasarkan urutan penambahan.

```js
const myMap = new Map();
myMap.set("nama", "Marno");
myMap.set(123, "Nomor ID");

console.log(myMap.get("nama")); // Marno
```

### Keunggulan Map:

- Bisa pakai object atau tipe data lain sebagai key
- Lebih konsisten performanya daripada object jika digunakan sebagai dictionary

---

## 5. WeakSet & WeakMap (Advanced Stuff) 🧠

- `WeakSet` hanya bisa menyimpan object dan tidak dapat di-loop.
- `WeakMap` hanya menerima object sebagai key dan memiliki memory management otomatis (GC friendly).

Contoh:

```js
let obj = { nama: "Marno" };
const ws = new WeakSet();
ws.add(obj);

const wm = new WeakMap();
wm.set(obj, "data rahasia");
```

> Catatan: Umumnya digunakan untuk caching dan pengelolaan data internal library/framework.

---

## 6. Kapan Menggunakan Apa?

| Kebutuhan                        | Struktur Data       |
|----------------------------------|---------------------|
| Daftar elemen urut & duplikat    | `Array`             |
| Key-value data biasa             | `Object`            |
| Kumpulan nilai unik              | `Set`               |
| Key-value dengan key fleksibel   | `Map`               |
| Caching atau private storage     | `WeakMap`, `WeakSet`|

---

## 7. Kesimpulan

Struktur data bukan cuma sekadar "cara nyimpan data", tapi fondasi dalam menulis program yang:

- 🔄 Lebih efisien
- 🧹 Lebih rapi
- 🚀 Lebih scalable

> Pahami struktur data = punya kekuatan untuk membuat program yang cepat dan powerful.

---

🧠 **Selanjutnya** kita akan masuk ke dunia yang lebih dalam lagi, seperti *OOP* dan bagaimana cara bikin class kayak di Java atau Python. Yuk, gas terus belajar JS sampai level dewa!
```
