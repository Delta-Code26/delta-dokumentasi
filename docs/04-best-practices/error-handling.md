
```markdown
# 🚨 Penanganan Error di JavaScript: Jangan Panik, Tangani!

Error dalam pemrograman itu bukan musuh, tapi sinyal bahwa "Hey, ada yang perlu diperbaiki di sini!". Kalau kamu bisa tangani error dengan baik, maka kamu bukan cuma ngoding, tapi ngoding dengan **profesionalisme level dewa** ⚔️

---

## 😵‍💫 Apa Itu Error?

> Error adalah kondisi saat program tidak bisa berjalan sebagaimana mestinya karena ada kesalahan di dalam kode atau input.

Error bisa muncul dari:
- Kesalahan sintaks (typo, kurung kurang, dll)
- Akses ke variabel yang belum dideklarasi
- Operasi yang tidak valid (bagi 0? oof.)
- Masalah jaringan/API
- dll.

---

## 🧪 Jenis-jenis Error di JavaScript

| Jenis Error        | Penjelasan                                  |
|--------------------|----------------------------------------------|
| `SyntaxError`      | Salah penulisan kode                         |
| `ReferenceError`   | Akses variabel yang belum dideklarasi        |
| `TypeError`        | Akses method atau properti yang gak valid    |
| `RangeError`       | Nilai di luar jangkauan                      |
| `EvalError`        | Terkait dengan penggunaan `eval()`           |
| `URIError`         | URI tidak valid (`decodeURIComponent`, dll) |

Contoh:

```javascript
console.log(x); // ❌ ReferenceError: x is not defined
```

---

## ✅ Teknik Dasar Menangani Error

### 1. `try...catch`

```javascript
try {
  let result = riskyFunction();
  console.log(result);
} catch (error) {
  console.error("Terjadi error:", error.message);
}
```

### 2. `try...catch...finally`

```javascript
try {
  console.log("Mulai...");
  riskyFunction();
} catch (e) {
  console.error("Oops!", e);
} finally {
  console.log("Cleanup jalan terus, error atau tidak.");
}
```

---

## 🔄 Menangani Error Asynchronous (Promise & Async/Await)

### Promise

```javascript
fetch('/api/data')
  .then(res => res.json())
  .then(data => console.log(data))
  .catch(err => console.error("Fetch error:", err));
```

### Async/Await

```javascript
async function getData() {
  try {
    const res = await fetch('/api/data');
    const data = await res.json();
    console.log(data);
  } catch (err) {
    console.error("Async error:", err);
  }
}
```

---

## 🚧 Custom Error: Bikin Error Sendiri

```javascript
class ValidationError extends Error {
  constructor(message) {
    super(message);
    this.name = "ValidationError";
  }
}

function validateData(data) {
  if (!data.name) {
    throw new ValidationError("Nama harus diisi.");
  }
}
```

Gunakan `instanceof` untuk mengecek jenis error:

```javascript
try {
  validateData({});
} catch (err) {
  if (err instanceof ValidationError) {
    console.warn("Input tidak valid:", err.message);
  } else {
    throw err;
  }
}
```

---

## 👮 Best Practice Error Handling

✅ Gunakan `try/catch` untuk blok kode yang rawan error  
✅ Log dengan jelas — pakai `console.error()` atau sistem logging  
✅ Hindari swallow error (nangkap error tapi gak ngapa-ngapain)  
✅ Buat error sejelas mungkin untuk debugging  
✅ Tangani error dari `fetch`, API, parsing, dan I/O

---

## 🧼 Hindari Ini!

```javascript
try {
  // kode
} catch (e) {
  // kosong, jangan gini!
}
```

Gak ada log, gak ada tindakan. Ini bikin debugging jadi mimpi buruk. Minimal log error-nya!

---

## 🧠 Bonus: Global Error Handler (Browser)

Tangkap semua error JS yang gak ditangani:

```javascript
window.onerror = function(message, source, lineno, colno, error) {
  console.error("Global error handler:", message);
};
```

---

## 📦 Logging Lebih Serius (Opsional)

Untuk aplikasi besar:
- Gunakan tool seperti [Sentry](https://sentry.io/)
- Atau logging ke server via API

---

## 🚀 Kesimpulan

Penanganan error yang baik = kode yang stabil, mudah debug, dan tahan banting. Jangan takut error — peluk mereka, tangani dengan lembut, dan log dengan cerdas.

> “Good error handling turns you from a junior coder into a pro dev.” — Gen Z Dev 😎

Stay safe, happy debugging! 💪
```
