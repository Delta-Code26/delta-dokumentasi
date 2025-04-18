
# 🖱️ DOM Events di JavaScript

**DOM Events** adalah salah satu fitur terpenting dalam pengembangan web interaktif. Ketika pengguna berinteraksi dengan halaman web (misalnya mengklik tombol, menggulir halaman, atau mengisi formulir), **event** akan terpicu. JavaScript memungkinkan kita untuk menangani event tersebut agar aplikasi kita lebih dinamis dan responsif.

---

## 1. Apa itu DOM Events?

**DOM (Document Object Model)** adalah representasi struktur HTML dalam bentuk objek yang dapat dimanipulasi dengan JavaScript. **DOM Events** adalah kejadian atau interaksi yang terjadi pada elemen-elemen di dalam dokumen HTML, seperti klik, input data, atau perubahan status elemen.

Contoh **event**: `click`, `keydown`, `submit`, `mouseover`, dan banyak lagi.

---

## 2. Jenis-jenis Event di JavaScript

Berikut adalah beberapa contoh event yang sering digunakan di JavaScript:

- **click**: Terjadi ketika elemen di klik.
- **keydown**: Terjadi ketika tombol pada keyboard ditekan.
- **keyup**: Terjadi ketika tombol pada keyboard dilepaskan.
- **submit**: Terjadi ketika formulir disubmit.
- **mouseover**: Terjadi ketika pointer mouse berada di atas elemen.
- **mouseout**: Terjadi ketika pointer mouse meninggalkan elemen.

---

## 3. Menambahkan Event Listener

Untuk menangani event, kita dapat menggunakan metode **`addEventListener()`**. Metode ini memungkinkan kita untuk mendengarkan (listen) event yang terjadi pada elemen tertentu dan menjalankan fungsi callback ketika event tersebut dipicu.

### 📌 Sintaks `addEventListener()`

```js
element.addEventListener(event, callback, useCapture);
```

- **event**: Nama event yang ingin didengarkan (misalnya `click`, `keydown`).
- **callback**: Fungsi yang akan dijalankan ketika event terjadi.
- **useCapture**: (Opsional) Parameter ini menentukan apakah event harus ditangani pada fase capture atau bubbling. Default-nya adalah `false` (bubbling).

### 📌 Contoh Penggunaan `addEventListener`

```html
<button id="myButton">Klik Saya!</button>

<script>
  const button = document.getElementById("myButton");
  
  button.addEventListener("click", function() {
    alert("Tombol diklik!");
  });
</script>
```

Di atas, kita mendengarkan event `click` pada tombol dengan ID `myButton`. Ketika tombol tersebut diklik, fungsi callback yang menampilkan alert akan dijalankan.

---

## 4. Event Bubbling dan Capturing

**Event Bubbling** dan **Event Capturing** adalah dua fase yang terjadi ketika event dipicu. Pada default-nya, event menggunakan **bubbling**.

### 📌 Event Bubbling

Pada **bubbling**, event dimulai dari elemen yang paling dalam (target) dan menyebar ke elemen-elemen luar (parent).

Contoh:

```html
<div id="outer">
  <button id="inner">Klik Saya!</button>
</div>

<script>
  const outerDiv = document.getElementById("outer");
  const innerButton = document.getElementById("inner");
  
  outerDiv.addEventListener("click", function() {
    alert("Outer div diklik!");
  });
  
  innerButton.addEventListener("click", function() {
    alert("Button diklik!");
  });
</script>
```

Pada contoh ini, ketika tombol diklik, akan muncul dua alert:
1. "Button diklik!"
2. "Outer div diklik!"

Ini terjadi karena event **bubbling** dari tombol menyebar ke elemen induk `div`.

### 📌 Event Capturing

Pada **capturing**, event dimulai dari elemen paling luar dan menyebar ke elemen paling dalam. Untuk menggunakan capturing, kamu harus mengatur parameter ketiga pada `addEventListener()` menjadi `true`.

```js
outerDiv.addEventListener("click", function() {
  alert("Outer div diklik pada fase capturing!");
}, true);
```

---

## 5. Menghapus Event Listener

Jika kita tidak lagi membutuhkan event listener, kita bisa menghapusnya menggunakan **`removeEventListener()`**.

### 📌 Sintaks `removeEventListener()`

```js
element.removeEventListener(event, callback);
```

### 📌 Contoh Menghapus Event Listener

```html
<button id="myButton">Klik Saya!</button>

<script>
  const button = document.getElementById("myButton");

  function handleClick() {
    alert("Tombol diklik!");
  }

  button.addEventListener("click", handleClick);

  // Hapus event listener setelah 3 detik
  setTimeout(function() {
    button.removeEventListener("click", handleClick);
    alert("Event listener dihapus!");
  }, 3000);
</script>
```

Pada contoh ini, event listener untuk tombol akan dihapus setelah 3 detik. Jadi, tombol hanya bisa diklik satu kali dalam waktu 3 detik.

---

## 6. Event Object

Saat sebuah event terjadi, objek event yang berisi informasi terkait dengan event tersebut akan diteruskan ke fungsi callback. Dengan menggunakan objek ini, kita bisa mendapatkan data seperti elemen yang memicu event, posisi mouse, key yang ditekan, dan banyak lagi.

### 📌 Contoh Penggunaan Event Object

```html
<button id="myButton">Klik Saya!</button>

<script>
  const button = document.getElementById("myButton");

  button.addEventListener("click", function(event) {
    alert("Tombol diklik pada posisi X: " + event.clientX + ", Y: " + event.clientY);
  });
</script>
```

Pada contoh ini, objek event memberikan informasi mengenai posisi mouse saat tombol diklik (`event.clientX` dan `event.clientY`).

---

## 7. Event Delegation

**Event delegation** adalah teknik untuk menangani event pada elemen-elemen yang baru ditambahkan atau banyak elemen yang serupa, dengan menggunakan event listener pada elemen induk. Ini sangat efisien karena kita hanya perlu menambahkan satu listener pada elemen induk dan menangani event untuk semua elemen anak.

### 📌 Contoh Event Delegation

```html
<ul id="list">
  <li>Item 1</li>
  <li>Item 2</li>
  <li>Item 3</li>
</ul>

<script>
  const list = document.getElementById("list");

  list.addEventListener("click", function(event) {
    if (event.target.tagName === "LI") {
      alert("Item " + event.target.textContent + " diklik!");
    }
  });
</script>
```

Pada contoh ini, kita mendengarkan event `click` pada elemen `ul` (induk). Ketika item `li` diklik, kita menggunakan **event delegation** untuk menangani klik tersebut.

---

## 🎯 Kesimpulan

- **DOM Events** memungkinkan kita untuk menangani interaksi pengguna dengan elemen HTML.
- Dengan **`addEventListener()`**, kita bisa menambahkan event listener untuk berbagai jenis event.
- **Event Bubbling** dan **Capturing** adalah dua fase yang terjadi saat event dipicu.
- **Event Object** memberikan informasi terkait event yang terjadi.
- **Event Delegation** memungkinkan kita menangani event pada banyak elemen dengan menambahkan satu event listener pada elemen induk.

Dengan memahami dan menguasai DOM Events, aplikasi web kamu akan menjadi lebih interaktif dan dinamis! Selanjutnya, kita akan membahas lebih lanjut mengenai **AJAX** dan bagaimana cara mengirim permintaan HTTP secara asynchronous.
```
