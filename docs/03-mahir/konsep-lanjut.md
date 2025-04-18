
# 🚀 Konsep Lanjutan dalam JavaScript

Selamat datang di tingkat akhir dari dokumentasi JavaScript! Di bagian ini, kita akan menyelam lebih dalam ke fitur-fitur lanjutan yang akan memperkuat pemahamanmu sebagai developer JavaScript modern. 

Konsep-konsep ini sering digunakan dalam pengembangan aplikasi kompleks, library besar, atau framework seperti React, Vue, dan lainnya.

---

## 1. 🔁 Closures

Closure adalah kombinasi dari function dan lingkungan leksikalnya.

```js
function luar() {
  let counter = 0;
  return function dalam() {
    counter++;
    console.log(counter);
  };
}

const hitung = luar();
hitung(); // 1
hitung(); // 2
```

Closure bisa **menyimpan state** meski fungsi luar sudah selesai dieksekusi.

---

## 2. 🔒 Encapsulation via Closures

Membuat data "private" di JavaScript menggunakan closure:

```js
function createCounter() {
  let count = 0;
  return {
    increment() {
      count++;
    },
    getCount() {
      return count;
    }
  };
}

const counter = createCounter();
counter.increment();
console.log(counter.getCount()); // 1
```

---

## 3. 🏭 Factory Functions

Fungsi yang mengembalikan objek baru.

```js
function createUser(name) {
  return {
    name,
    greet() {
      console.log(`Halo, ${name}!`);
    }
  };
}

const user = createUser('Marno');
user.greet(); // Halo, Marno!
```

---

## 4. 🧬 Prototypes & Inheritance

JavaScript menggunakan **prototype-based inheritance**, bukan class-based seperti Java.

```js
function User(name) {
  this.name = name;
}

User.prototype.sayHi = function() {
  console.log(`Hi, saya ${this.name}`);
};

const u = new User("Marno");
u.sayHi(); // Hi, saya Marno
```

---

## 5. 🎭 Context (`this`) & Binding

`this` adalah referensi ke konteks saat fungsi dipanggil.

```js
const user = {
  name: "Marno",
  sayHi() {
    console.log(`Hi ${this.name}`);
  }
};

user.sayHi(); // Hi Marno
```

Kalau dipisah:

```js
const greet = user.sayHi;
greet(); // ❌ undefined (karena this-nya hilang)

const boundGreet = user.sayHi.bind(user);
boundGreet(); // ✅ Hi Marno
```

---

## 6. 🔄 Recursion (Rekursif)

Fungsi yang memanggil dirinya sendiri. Berguna untuk struktur data tree atau nested array.

```js
function faktorial(n) {
  if (n === 1) return 1;
  return n * faktorial(n - 1);
}

console.log(faktorial(5)); // 120
```

---

## 7. 🧵 Generator Functions

Fungsi yang bisa "pause" dan "lanjut" dengan `yield`.

```js
function* angka() {
  yield 1;
  yield 2;
  yield 3;
}

const it = angka();
console.log(it.next().value); // 1
console.log(it.next().value); // 2
```

---

## 8. 📥 Lazy Evaluation

Digunakan untuk evaluasi data hanya saat dibutuhkan.

Generator dan async iterators mendukung ini secara natural:

```js
function* infiniteCounter() {
  let i = 0;
  while (true) yield i++;
}
```

---

## 9. 🔧 Proxy & Reflect

Untuk mengintersepsi operasi terhadap objek.

```js
const handler = {
  get(target, prop) {
    return prop in target ? target[prop] : "Ga ada bro!";
  }
};

const obj = new Proxy({ nama: "Marno" }, handler);

console.log(obj.nama); // Marno
console.log(obj.umur); // Ga ada bro!
```

---

## 10. 🧠 Meta Programming

Manipulasi program menggunakan program itu sendiri: biasanya melibatkan `Proxy`, `Reflect`, atau `eval()` (hati-hati yang ini ya).

---

## 11. 🧱 Symbol

Tipe data primitif baru untuk membuat property unik.

```js
const id = Symbol('id');
const user = {
  [id]: 123
};

console.log(user[id]); // 123
```

---

## 12. 🧪 Optional Chaining & Nullish Coalescing

```js
const user = { profile: { name: "Marno" } };

console.log(user.profile?.name); // Marno
console.log(user.address?.street); // undefined

const umur = user.age ?? 20; // Kalau undefined/null, pakai 20
```

---

## Kesimpulan

Konsep-konsep lanjutan ini adalah fondasi dari framework modern dan pattern tingkat tinggi di JavaScript. Walau kelihatan rumit, kalau kamu kuasai ini semua... kamu udah bisa dianggap sebagai **JavaScript Sifu** 😎

| Konsep               | Fungsi                                                                 |
|----------------------|------------------------------------------------------------------------|
| Closure              | Simpan state privat                                                     |
| Factory Function     | Buat objek tanpa `class`                                                |
| Prototypes           | Dasar inheritance di JavaScript                                        |
| `this` & binding     | Konteks eksekusi fungsi                                                 |
| Recursion            | Penyelesaian masalah struktural/nested                                 |
| Generator            | Fungsi yang bisa dihentikan sementara                                  |
| Proxy & Reflect      | Kontrol penuh atas operasi objek                                       |
| Optional Chaining    | Aman akses properti dalam struktur dalam                               |

---

> 🚀 Lanjutkan perjalananmu ke topik-topik seperti testing, performa, dan bahkan TypeScript agar makin lengkap!

```
