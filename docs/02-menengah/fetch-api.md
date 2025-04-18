
# 🌐 Fetch API di JavaScript

**Fetch API** adalah cara modern untuk melakukan permintaan HTTP (seperti GET, POST, PUT, DELETE) ke server. Fetch menggantikan metode lama seperti `XMLHttpRequest` dan memberikan cara yang lebih bersih dan mudah dibaca untuk menangani permintaan dan respons HTTP secara asinkronus. Fetch API juga mengembalikan **Promise**, yang memungkinkan kita untuk menangani hasil permintaan HTTP dengan menggunakan `then()` atau `async/await`.

---

## 1. Apa itu Fetch API?

**Fetch API** menyediakan antarmuka untuk melakukan permintaan HTTP dan mengambil respons dari server. Dengan menggunakan **Promise**, Fetch memungkinkan kita untuk bekerja dengan kode asinkron dengan cara yang lebih elegan.

### 📌 Fetch API dan Promise

- **`fetch()`**: Metode utama dari Fetch API yang digunakan untuk membuat permintaan HTTP.
- **`then()`**: Digunakan untuk menangani respons yang diterima setelah permintaan selesai.
- **`catch()`**: Digunakan untuk menangani error yang terjadi selama permintaan.

---

## 2. Sintaks Dasar `fetch()`

Berikut adalah sintaks dasar dari `fetch()`:

```js
fetch(url, options)
  .then(response => response.json())  // Mengonversi respons menjadi format JSON
  .then(data => console.log(data))     // Menampilkan data yang diterima
  .catch(error => console.log(error)); // Menangani error jika ada
```

- **`url`**: URL tempat kita mengirim permintaan.
- **`options`**: (Opsional) Opsi tambahan untuk permintaan seperti metode HTTP, headers, body, dll.

### 📌 Contoh Penggunaan `fetch()`

```js
fetch("https://jsonplaceholder.typicode.com/posts")
  .then(response => response.json())  // Mengonversi respons JSON
  .then(data => console.log(data))     // Menampilkan data yang diterima
  .catch(error => console.log(error)); // Menangani error
```

Pada contoh ini, kita mengirimkan permintaan GET ke URL `https://jsonplaceholder.typicode.com/posts` dan menampilkan data yang diterima dalam format JSON.

---

## 3. Metode HTTP di Fetch API

**Fetch API** mendukung berbagai metode HTTP seperti `GET`, `POST`, `PUT`, `DELETE`, dan lainnya. Kita bisa menambahkan metode ini melalui opsi `method` dalam objek `options`.

### 📌 Contoh Permintaan GET

Permintaan **GET** digunakan untuk mengambil data dari server.

```js
fetch("https://jsonplaceholder.typicode.com/posts")
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.log(error));
```

### 📌 Contoh Permintaan POST

Permintaan **POST** digunakan untuk mengirimkan data ke server. Biasanya digunakan saat mengirim formulir atau data dalam format JSON.

```js
const postData = {
  title: "Post Baru",
  body: "Ini adalah konten dari post baru.",
  userId: 1
};

fetch("https://jsonplaceholder.typicode.com/posts", {
  method: "POST", // Menggunakan metode POST
  headers: {
    "Content-Type": "application/json"  // Menyatakan bahwa data yang dikirimkan adalah JSON
  },
  body: JSON.stringify(postData)  // Mengonversi data menjadi format JSON
})
  .then(response => response.json())  // Mengonversi respons menjadi JSON
  .then(data => console.log(data))     // Menampilkan data yang diterima
  .catch(error => console.log(error)); // Menangani error
```

Di sini, kita mengirimkan data JSON menggunakan metode **POST** ke server.

### 📌 Contoh Permintaan PUT

Permintaan **PUT** digunakan untuk memperbarui data yang ada di server.

```js
const updateData = {
  title: "Post Diperbarui",
  body: "Ini adalah konten post yang telah diperbarui.",
  userId: 1
};

fetch("https://jsonplaceholder.typicode.com/posts/1", {
  method: "PUT", // Menggunakan metode PUT
  headers: {
    "Content-Type": "application/json"  // Menyatakan bahwa data yang dikirimkan adalah JSON
  },
  body: JSON.stringify(updateData)  // Mengonversi data menjadi format JSON
})
  .then(response => response.json())  // Mengonversi respons menjadi JSON
  .then(data => console.log(data))     // Menampilkan data yang diterima
  .catch(error => console.log(error)); // Menangani error
```

### 📌 Contoh Permintaan DELETE

Permintaan **DELETE** digunakan untuk menghapus data dari server.

```js
fetch("https://jsonplaceholder.typicode.com/posts/1", {
  method: "DELETE", // Menggunakan metode DELETE
})
  .then(response => {
    if (response.ok) {
      console.log("Data berhasil dihapus");
    } else {
      console.log("Gagal menghapus data");
    }
  })
  .catch(error => console.log(error)); // Menangani error
```

---

## 4. Menangani Respons

Setelah permintaan selesai, kita perlu menangani respons yang diterima dari server. Respons dari `fetch()` bukanlah data yang langsung bisa digunakan, tetapi sebuah objek `Response` yang perlu diproses lebih lanjut.

### 📌 Respons Status dan Status Code

Sebelum kita memproses data, kita bisa memeriksa status dari respons menggunakan properti `ok` atau `status` dari objek `Response`.

```js
fetch("https://jsonplaceholder.typicode.com/posts")
  .then(response => {
    if (response.ok) {
      return response.json(); // Mengonversi ke format JSON jika respons berhasil
    } else {
      throw new Error("Gagal mendapatkan data");
    }
  })
  .then(data => console.log(data))
  .catch(error => console.log(error)); // Menangani error
```

Di sini, kita memeriksa apakah respons berhasil dengan memeriksa properti `response.ok`. Jika respons berhasil, kita mengonversinya menjadi JSON.

---

## 5. Menggunakan Async/Await dengan Fetch

Selain menggunakan `then()` untuk menangani `Promise`, kita juga bisa menggunakan **async/await** untuk menulis kode yang lebih bersih dan mudah dibaca.

### 📌 Contoh Async/Await dengan Fetch

```js
async function fetchData() {
  try {
    const response = await fetch("https://jsonplaceholder.typicode.com/posts");
    if (!response.ok) {
      throw new Error("Gagal mendapatkan data");
    }
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.log(error);
  }
}

fetchData();
```

Dengan **async/await**, kita menulis kode yang lebih mirip dengan kode synchronous meskipun masih menangani operasi asinkronus.

---

## 6. Menangani Error dalam Fetch API

Jika terjadi kesalahan selama permintaan HTTP, kita bisa menangani error menggunakan **`catch()`** atau dengan menggunakan blok **`try/catch`** ketika menggunakan async/await.

### 📌 Error yang Dapat Terjadi

- **Kesalahan jaringan**: Jika ada masalah dengan koneksi internet atau server tidak dapat dijangkau.
- **Status HTTP yang tidak berhasil**: Jika server mengembalikan status selain 2xx, seperti 404 atau 500.

### 📌 Contoh Error Handling

```js
fetch("https://jsonplaceholder.typicode.com/invalid-url")
  .then(response => {
    if (!response.ok) {
      throw new Error("Gagal mendapatkan data");
    }
    return response.json();
  })
  .then(data => console.log(data))
  .catch(error => console.log("Terjadi error: ", error)); // Menangani error
```

---

## 🎯 Kesimpulan

- **Fetch API** adalah cara modern untuk melakukan permintaan HTTP dan menangani respons di JavaScript.
- Menggunakan **`fetch()`**, kita bisa mengirimkan permintaan HTTP dengan metode seperti GET, POST, PUT, dan DELETE.
- Respons dari `fetch()` perlu diproses lebih lanjut untuk mengonversi data menjadi format yang dapat digunakan.
- Dengan menggunakan **async/await**, kita bisa menulis kode yang lebih bersih dan mudah dipahami.
- **Error handling** sangat penting untuk menangani masalah yang terjadi selama permintaan HTTP.

Dengan memahami Fetch API, kamu bisa berinteraksi dengan server secara asinkronus dan mengambil atau mengirim data dengan cara yang efisien dan terstruktur. Selanjutnya, kita akan bahas tentang **AJAX** dan bagaimana cara mengirim permintaan HTTP menggunakan teknik yang lebih lama namun masih banyak digunakan di banyak aplikasi web.
```
