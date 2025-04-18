
# 🧱 Object-Oriented Programming (OOP) di JavaScript

Walaupun JavaScript awalnya bukan bahasa OOP seperti Java atau C++, JS mendukung paradigma **Object-Oriented Programming** melalui object literals, prototype, dan `class`. Konsep OOP ini sangat berguna untuk membangun aplikasi skala besar yang modular dan reusable.

---

## 🧠 Apa Itu OOP?

OOP adalah pendekatan pemrograman berbasis objek. Setiap objek berisi:
- **Properties** (data)
- **Methods** (fungsi untuk melakukan aksi)

---

## 🧬 Empat Pilar OOP

### 1. **Encapsulation**
Menyembunyikan detail internal dan hanya mengekspos apa yang perlu digunakan.

```js
class User {
  constructor(name) {
    this._name = name;
  }

  get name() {
    return this._name;
  }

  set name(namaBaru) {
    this._name = namaBaru;
  }
}
```

---

### 2. **Abstraction**
Menyederhanakan kompleksitas dengan hanya menampilkan fitur penting.

```js
class MesinATM {
  tarikTunai(jumlah) {
    this.#verifikasiKartu();
    console.log(`Menarik Rp${jumlah}`);
  }

  #verifikasiKartu() {
    console.log("Kartu diverifikasi");
  }
}

const atm = new MesinATM();
atm.tarikTunai(500000);
// atm.#verifikasiKartu(); ❌ Error, method ini private
```

---

### 3. **Inheritance**
Mewarisi properti dan metode dari class lain.

```js
class Kendaraan {
  constructor(merk) {
    this.merk = merk;
  }

  jalan() {
    console.log(`${this.merk} berjalan`);
  }
}

class Mobil extends Kendaraan {
  klakson() {
    console.log("Tin tin!");
  }
}

const avanza = new Mobil("Avanza");
avanza.jalan();   // Avanza berjalan
avanza.klakson(); // Tin tin!
```

---

### 4. **Polymorphism**
Objek bisa punya banyak bentuk (method override).

```js
class Hewan {
  suara() {
    console.log("Hewan bersuara");
  }
}

class Kucing extends Hewan {
  suara() {
    console.log("Meong");
  }
}

const h = new Hewan();
const k = new Kucing();

h.suara(); // Hewan bersuara
k.suara(); // Meong (override)
```

---

## 🏗️ Membuat Class di JavaScript

### Sintaks Dasar

```js
class Person {
  constructor(nama, umur) {
    this.nama = nama;
    this.umur = umur;
  }

  sapa() {
    console.log(`Hai, saya ${this.nama}, umur ${this.umur}`);
  }
}

const orang = new Person("Marno", 20);
orang.sapa();
```

---

## ⚙️ Inheritance (Pewarisan)

Gunakan `extends` untuk membuat subclass:

```js
class Pegawai extends Person {
  constructor(nama, umur, jabatan) {
    super(nama, umur); // panggil constructor parent
    this.jabatan = jabatan;
  }

  kerja() {
    console.log(`${this.nama} sedang bekerja sebagai ${this.jabatan}`);
  }
}
```

---

## 🔒 Private Fields & Methods

JavaScript mendukung properti dan method private dengan prefix `#`:

```js
class Bank {
  #saldo = 1000;

  lihatSaldo() {
    console.log(`Saldo: Rp${this.#saldo}`);
  }
}
```

---

## 🛠️ Static Method & Property

Tidak perlu buat instance untuk mengaksesnya.

```js
class MathTools {
  static tambah(a, b) {
    return a + b;
  }
}

console.log(MathTools.tambah(2, 3)); // 5
```

---

## 🧰 Object Literal vs Class

```js
// Object literal
const motor = {
  merk: "Yamaha",
  nyalakan() {
    console.log("Motor nyala");
  }
};

// Class
class Motor {
  constructor(merk) {
    this.merk = merk;
  }
  nyalakan() {
    console.log("Motor nyala");
  }
}
```

---

## 🔄 Prototype di Balik Layar

Class di JavaScript hanyalah "sintaks manis" (syntactic sugar) dari sistem prototype.

```js
function Orang(nama) {
  this.nama = nama;
}
Orang.prototype.sapa = function () {
  console.log(`Halo, saya ${this.nama}`);
};

const o = new Orang("Marno");
o.sapa();
```

---

## 🧪 Perbandingan OOP vs Functional

| Aspek             | OOP                            | Functional                           |
|-------------------|----------------------------------|---------------------------------------|
| Paradigma         | Objek dan class                 | Fungsi sebagai unit utama             |
| State             | Mutable                         | Immutable                             |
| Komposisi         | Lewat inheritance               | Lewat fungsi-fungsi kecil             |
| Contoh cocok      | Aplikasi UI, Game, ERP          | Manipulasi data, logika bisnis        |

---

## 🚀 Kapan Gunakan OOP?

✅ Cocok untuk:
- Struktur data kompleks
- Banyak entitas/aktor (User, Kendaraan, Produk, dll)
- Aplikasi berbasis komponen

---

## 🧠 Kesimpulan

Dengan OOP, kamu bisa membuat aplikasi yang:
- Lebih terstruktur
- Lebih mudah dipelihara
- Lebih scalable

Tapi ingat: **OOP bukan satu-satunya cara**. Kadang fungsional lebih ringkas dan aman.

> 🎯 Pilih alat yang tepat untuk kebutuhanmu. Tapi menguasai OOP akan membuka pintu ke banyak framework besar seperti React, Angular, dan Vue.

```
