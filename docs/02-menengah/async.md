
# ⏳ Async Programming di JavaScript

Di JavaScript, beberapa operasi seperti pengambilan data dari server atau pembacaan file tidak dapat dilakukan secara langsung karena memerlukan waktu. Untuk itu, JavaScript menawarkan cara untuk menangani operasi-operasi tersebut secara **asynchronous**. Ini memungkinkan aplikasi tetap responsif dan tidak terblokir saat menjalankan operasi berat.

---

## 1. Apa itu Asynchronous Programming?

**Asynchronous programming** memungkinkan kode untuk dieksekusi secara non-blokir, yang berarti kode berikutnya dapat berjalan tanpa menunggu operasi yang sedang berlangsung selesai. Ini sangat penting ketika kita berurusan dengan tugas-tugas yang memakan waktu seperti membaca file, mengakses API, atau query database.

### 📌 **Synchronous vs Asynchronous**

- **Synchronous**: Proses yang dilakukan satu per satu. Kode akan menunggu operasi selesai sebelum melanjutkan ke operasi berikutnya.
- **Asynchronous**: Proses yang dapat berjalan secara bersamaan, memungkinkan operasi berikutnya untuk dijalankan tanpa menunggu operasi sebelumnya selesai.

### 📌 Contoh Synchronous

```js
console.log("Mulai");
console.log("Proses 1 selesai");
console.log("Proses 2 selesai");
```

### 📌 Contoh Asynchronous

```js
console.log("Mulai");

setTimeout(() => {
  console.log("Proses 1 selesai");
}, 2000);  // Proses ini terjadi setelah 2 detik

console.log("Proses 2 selesai");
```

Pada contoh di atas, meskipun ada `setTimeout` yang memerlukan waktu 2 detik, JavaScript tidak menunggu dan langsung menjalankan `console.log("Proses 2 selesai")`.

---

## 2. Callback Functions

Callback adalah fungsi yang diberikan sebagai argumen kepada fungsi lain dan dijalankan setelah operasi asynchronous selesai.

### 📌 Contoh Callback

```js
function ambilData(callback) {
  setTimeout(() => {
    callback("Data berhasil diambil");
  }, 2000);
}

ambilData((message) => {
  console.log(message);  // Output: "Data berhasil diambil"
});
```

Di sini, `ambilData` adalah fungsi yang menerima sebuah callback yang akan dijalankan setelah 2 detik.

---

## 3. Promises

**Promise** adalah objek yang mewakili penyelesaian atau kegagalan dari sebuah operasi asynchronous. Promise memiliki tiga keadaan:

1. **Pending**: Janji belum diselesaikan.
2. **Fulfilled**: Janji berhasil diselesaikan (resolved).
3. **Rejected**: Janji gagal diselesaikan.

### 📌 Membuat Promise

```js
let promise = new Promise((resolve, reject) => {
  let success = true;
  
  if (success) {
    resolve("Operasi berhasil");
  } else {
    reject("Operasi gagal");
  }
});

promise.then((message) => {
  console.log(message);  // Output: "Operasi berhasil"
}).catch((message) => {
  console.log(message);  // Jika terjadi error, tampilkan "Operasi gagal"
});
```

- **`resolve()`** digunakan ketika operasi berhasil.
- **`reject()`** digunakan ketika operasi gagal.

### 📌 Menggunakan .then() dan .catch()

`then()` digunakan untuk menangani hasil yang berhasil, sementara `catch()` digunakan untuk menangani error.

```js
let promise = new Promise((resolve, reject) => {
  let success = false;
  
  if (success) {
    resolve("Data berhasil diambil");
  } else {
    reject("Data gagal diambil");
  }
});

promise
  .then((data) => {
    console.log(data);  // Output jika resolve
  })
  .catch((error) => {
    console.log(error);  // Output jika reject
  });
```

---

## 4. Async/Await

`async/await` adalah cara modern untuk menangani operasi asynchronous di JavaScript dengan cara yang lebih mudah dibaca dan ditulis. `async` digunakan untuk mendeklarasikan fungsi yang akan mengembalikan sebuah **Promise**, dan `await` digunakan untuk menunggu penyelesaian dari sebuah Promise sebelum melanjutkan ke kode berikutnya.

### 📌 Menggunakan async/await

```js
async function ambilData() {
  let result = await new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve("Data berhasil diambil");
    }, 2000);
  });

  console.log(result);  // Output: "Data berhasil diambil"
}

ambilData();
```

- `await` hanya bisa digunakan di dalam fungsi yang dideklarasikan dengan `async`.
- `await` menunggu sampai Promise selesai sebelum melanjutkan ke baris kode berikutnya.

---

## 5. Error Handling dengan try/catch

Ketika menggunakan `async/await`, kita dapat menangani error dengan menggunakan blok `try/catch`.

### 📌 Contoh Penggunaan try/catch

```js
async function ambilData() {
  try {
    let result = await new Promise((resolve, reject) => {
      let success = false;  // Simulasikan error
      setTimeout(() => {
        if (success) {
          resolve("Data berhasil diambil");
        } else {
          reject("Data gagal diambil");
        }
      }, 2000);
    });

    console.log(result);
  } catch (error) {
    console.log("Error:", error);  // Output: "Error: Data gagal diambil"
  }
}

ambilData();
```

Dengan `try/catch`, kita dapat menangani error yang mungkin terjadi selama proses asynchronous.

---

## 6. Menggunakan Multiple Async Functions

Jika kamu memiliki beberapa operasi asynchronous yang perlu dijalankan secara bersamaan, kamu bisa menggunakan `Promise.all()` untuk menunggu semua Promise selesai.

### 📌 Contoh Promise.all

```js
async function ambilData() {
  let promise1 = new Promise((resolve) => setTimeout(() => resolve("Data 1 selesai"), 2000));
  let promise2 = new Promise((resolve) => setTimeout(() => resolve("Data 2 selesai"), 3000));
  
  let result = await Promise.all([promise1, promise2]);
  console.log(result);  // Output: ["Data 1 selesai", "Data 2 selesai"]
}

ambilData();
```

`Promise.all()` akan menunggu hingga semua Promise dalam array selesai sebelum melanjutkan eksekusi.

---

## 🎯 Kesimpulan

- **Asynchronous Programming**: Menangani operasi yang memerlukan waktu, seperti pengambilan data atau operasi IO, tanpa memblokir eksekusi program.
- **Callback**: Fungsi yang diberikan kepada fungsi lain dan dieksekusi setelah operasi asynchronous selesai.
- **Promise**: Representasi dari sebuah operasi asynchronous yang bisa berhasil atau gagal.
- **async/await**: Cara modern untuk menulis kode asynchronous dengan cara yang lebih mudah dibaca dan ditulis.
- **Error Handling**: Gunakan `try/catch` untuk menangani error yang terjadi pada operasi asynchronous.

Dengan memahami konsep **Async Programming**, kamu bisa menulis kode JavaScript yang lebih efisien dan mudah dipahami. Selanjutnya, kita akan bahas tentang **Event Loop** dan bagaimana JavaScript mengelola operasi asynchronous di bawah tenda.
```
