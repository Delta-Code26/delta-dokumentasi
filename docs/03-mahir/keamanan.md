
# 🛡️ Keamanan JavaScript di Browser & Frontend

Keamanan dalam JavaScript sangat penting, terutama saat membuat aplikasi web. Walaupun mayoritas tanggung jawab keamanan ada di sisi **backend**, sisi **frontend (JavaScript)** tetap rawan eksploitasi.

Di halaman ini, kita akan bahas ancaman umum dan cara mencegahnya. Biar aplikasi kamu gak jadi target empuk hacker, ya kan?

---

## 1. 🚨 Ancaman Umum di JavaScript

### ⚠️ XSS (Cross-Site Scripting)
XSS adalah serangan di mana hacker menyisipkan JavaScript berbahaya ke halaman web.

**Contoh:**
```html
<input value="<script>alert('Hacked!')</script>" />
```

Jika input ini langsung ditampilkan tanpa disanitasi, boom! Kode jahat akan jalan di browser korban.

**Solusi:**
- Jangan pernah langsung render input user ke HTML tanpa sanitasi.
- Gunakan DOM manipulation API seperti `textContent`, bukan `innerHTML`.

```js
// ❌ Rentan XSS
element.innerHTML = userInput;

// ✅ Aman
element.textContent = userInput;
```

---

### ⚠️ CSRF (Cross-Site Request Forgery)
Serangan di mana user tanpa sadar mengirim request yang berbahaya (biasanya lewat cookie yang udah login).

> Walau mitigasi utama ada di server (CSRF token, SameSite cookie), kamu bisa bantu dengan memastikan frontend hanya mengirim request saat user melakukan aksi nyata (misalnya klik tombol).

---

### ⚠️ Klikjacking
Menipu user agar mengklik sesuatu yang tidak mereka sadari, misalnya tombol tersembunyi di iframe.

**Solusi frontend:**
Tambahkan header `X-Frame-Options: DENY` di backend (tapi kamu bisa bantu validasi iframe juga di frontend).

---

### ⚠️ Leaking Data ke Konsol
Jangan pernah log data sensitif ke console browser! Hacker bisa buka DevTools dan lihat semua data.

```js
// ❌ Jangan lakukan ini di production
console.log(user.password);
```

---

## 2. ✅ Tips Menulis JavaScript yang Aman

### 🧽 1. Escape dan sanitasi input user
Gunakan library seperti:
- `DOMPurify`
- `sanitize-html`

```js
import DOMPurify from 'dompurify';

const cleanInput = DOMPurify.sanitize(userInput);
```

---

### 🔒 2. Validasi di sisi klien DAN server
Frontend itu ibarat pagar bambu—bisa diloncati. Jadi jangan andalkan validasi frontend saja.

---

### 🧯 3. Matikan `eval()`, `Function()`, dan sejenisnya
Fungsi-fungsi ini bisa mengeksekusi string sebagai kode—dan itu horor.

```js
// ❌ Gak aman
eval("alert('Hacked')");

// ✅ Hindari, dan cari alternatif aman
```

---

### 🎭 4. Obfuscate kode JavaScript
Jangan biarkan kode mentah bisa dibaca semua orang. Gunakan tool seperti:
- [Terser](https://github.com/terser/terser)
- [UglifyJS](https://github.com/mishoo/UglifyJS)

Tapi ingat: obfuscation ≠ security. Itu cuma bikin ribet, bukan bikin aman 100%.

---

### 📦 5. Hati-hati dengan dependencies
- Selalu periksa package dengan `npm audit`
- Update library secara rutin
- Hindari menggunakan package dari sumber gak jelas

---

## 3. 🧪 Tools & Praktik Keamanan

- 🔍 [npm audit](https://docs.npmjs.com/cli/v8/commands/npm-audit)
- 🔍 [Snyk](https://snyk.io/) — cek kerentanan dependencies
- 🔍 [Lighthouse Security Checks](https://developers.google.com/web/tools/lighthouse/)
- 🔒 [Helmet.js](https://helmetjs.github.io/) — middleware untuk proteksi HTTP headers

---

## 4. 🔐 Contoh Best Practice

```js
// ✅ Gunakan CSP (Content Security Policy)
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self'">

// ✅ Gunakan HTTPS selalu
if (location.protocol !== 'https:') {
  location.replace(`https:${location.href.substring(location.protocol.length)}`);
}
```

---

## 5. Kesimpulan

| Masalah        | Solusi Frontend                                 |
|----------------|--------------------------------------------------|
| XSS            | Gunakan `textContent`, DOMPurify                |
| CSRF           | Gunakan metode POST + token                     |
| Klikjacking    | Validasi iframe atau header `X-Frame-Options`   |
| Data leak      | Jangan `console.log()` data sensitif            |
| eval()         | Hindari penggunaan                              |
| Dependencies   | Audit rutin dan verifikasi                      |

---

> 🎯 Ingat: **Frontend bukan tempat utama untuk keamanan, tapi bisa jadi pertahanan pertama.** Tugas kamu adalah meminimalkan risiko, bukan jadi superhero — tapi hey, dengan best practices ini, kamu udah layak pakai jubah. 🦸‍♂️

```
