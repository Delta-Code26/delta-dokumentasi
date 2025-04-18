
# 🔄 Memahami Event Loop di JavaScript

Event Loop adalah salah satu konsep paling penting (dan kadang paling bikin pusing) dalam JavaScript, terutama karena JavaScript **single-threaded** tapi bisa menangani **operasi async** seperti HTTP request, setTimeout, dan lainnya.

> Kalau kamu pernah bingung kenapa `console.log("A")` muncul duluan padahal ada `setTimeout(..., 0)`, itu kerjaan si **Event Loop**.

---

## 1. JavaScript itu Single-threaded

Artinya, hanya satu instruksi yang bisa dijalankan dalam satu waktu. Tapi… kok bisa jalanin banyak hal sekaligus kayak fetch data, timer, dan animasi?

Jawabannya: karena JavaScript punya **Event Loop** yang bekerja bareng **Call Stack** dan **Web APIs / Callback Queue** (jika di browser) atau **libuv** (jika di Node.js).

---

## 2. Komponen Penting

### 🧠 Call Stack
Tempat eksekusi kode sinkron. Modelnya LIFO (Last In, First Out).

### 🕸️ Web APIs
Disediakan oleh browser (atau libuv di Node.js) untuk handle async seperti:
- `setTimeout`
- `fetch`
- `DOM events`

### 📩 Callback Queue (Task Queue)
Menampung callback yang siap dieksekusi setelah Call Stack kosong.

### 🔁 Event Loop
Yang ngecek terus: "Eh, Call Stack kosong gak? Kalau kosong, ayo masukin callback dari Queue!"

---

## 3. Ilustrasi Sederhana

```js
console.log("A");

setTimeout(() => {
  console.log("B");
}, 0);

console.log("C");
```

### Output:
```
A
C
B
```

Kenapa B terakhir padahal 0ms?

Karena:
1. `setTimeout` didaftarkan ke Web API.
2. `console.log("C")` lanjut dieksekusi.
3. Setelah Call Stack kosong, callback `setTimeout` dimasukkan ke Queue.
4. Event Loop mengeksekusinya setelah semua sync selesai.

---

## 4. Microtask Queue vs Callback Queue

Selain **Callback Queue**, ada juga **Microtask Queue**. Ini lebih prioritas dan diisi oleh:
- `Promise.then()`
- `MutationObserver`

```js
console.log("Start");

setTimeout(() => console.log("Timeout"), 0);

Promise.resolve().then(() => console.log("Promise"));

console.log("End");
```

### Output:
```
Start
End
Promise
Timeout
```

> Promise punya prioritas lebih tinggi dibanding `setTimeout`. Mereka masuk ke Microtask Queue.

---

## 5. Visualisasi Event Loop

```
📦 Code masuk ke → Call Stack
⏱ Async call dikirim ke → Web API
✅ Selesai? Callback dikirim ke → Task Queue
🌀 Call Stack kosong? Event Loop → Masukkan callback ke Call Stack
```

---

## 6. Debugging Event Loop (Tips Dev)

- Gunakan `console.log()` untuk lacak urutan eksekusi.
- Gunakan browser DevTools tab “Performance” untuk lihat event loop dan call stack.
- Tools seperti [Loupe](http://latentflip.com/loupe/) bisa bantu visualisasi event loop.

---

## 7. Kesimpulan

| Konsep         | Penjelasan Singkat                          |
|----------------|----------------------------------------------|
| Single-threaded | JavaScript cuma punya 1 jalur eksekusi       |
| Web API         | Jalur khusus buat ngatur operasi async       |
| Event Loop      | Jembatan antara async dan eksekusi utama     |
| Task vs Microtask | Microtask punya prioritas lebih tinggi     |

---

> 🔁 **Event Loop** bukan cuma teori, tapi dasar dari semua hal async di JavaScript. Pahami ini dan kamu bakal bisa nge-handle `async/await`, `fetch`, `Promise`, dan sejenisnya kayak ninja!

---

📚 Selanjutnya: kita akan menyelami dunia **`async/await`** dan bagaimana menulis kode async yang kelihatan kayak sync—biar hidupmu sebagai dev jadi lebih damai.
```
