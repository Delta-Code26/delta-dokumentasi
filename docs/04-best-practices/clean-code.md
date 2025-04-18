
```markdown
# 🧼 Clean Code dalam JavaScript

Menulis kode yang *jalan* itu gampang. Tapi menulis kode yang *enak dibaca* dan *mudah dipelihara*? Nah, itu seninya!

Dokumen ini berisi prinsip dan praktik clean code khusus untuk JavaScript, biar kode kamu gak cuma bisa jalan, tapi juga bikin tim kamu bilang: "**Nicee! Ini baru kode bersih!**"

---

## 🤔 Apa Itu Clean Code?

> Clean code adalah kode yang mudah dibaca, dimengerti, diubah, dan diuji.

Bayangkan kamu baca kode orang lain tanpa stres, atau 6 bulan ke depan kamu buka lagi kode lama kamu dan langsung ngerti — itulah clean code.

---

## 🧠 Prinsip Clean Code

### 1. Gunakan Penamaan yang Jelas

**❌ Hindari:**

```javascript
let a = 10;
function d(x) {
  return x * a;
}
```

**✅ Gunakan:**

```javascript
let baseSalary = 10;
function calculateBonus(multiplier) {
  return multiplier * baseSalary;
}
```

---

### 2. Hindari Kode Berulang (*DRY - Don't Repeat Yourself*)

**❌ Hindari:**

```javascript
function printAdmin() {
  console.log("Role: Admin");
}
function printUser() {
  console.log("Role: User");
}
```

**✅ Gunakan:**

```javascript
function printRole(role) {
  console.log(`Role: ${role}`);
}
```

---

### 3. Fungsi Harus Fokus pada Satu Tugas (*Single Responsibility*)

**❌ Hindari:**

```javascript
function handleUserData(user) {
  saveToDatabase(user);
  sendEmail(user.email);
  updateUI(user);
}
```

**✅ Gunakan:**

```javascript
function saveUser(user) { /*...*/ }
function notifyUser(user) { /*...*/ }
function renderUser(user) { /*...*/ }
```

---

### 4. Hindari Magic Number dan String

**❌ Hindari:**

```javascript
if (status === 2) {
  // Approved
}
```

**✅ Gunakan:**

```javascript
const STATUS_APPROVED = 2;
if (status === STATUS_APPROVED) {
  // Approved
}
```

---

### 5. Jaga Panjang Fungsi & File

- Fungsi idealnya kurang dari 20 baris
- File JavaScript sebaiknya fokus pada 1 topik (modular)

---

## ✍️ Contoh Clean vs Dirty Code

**💩 Dirty Code:**

```javascript
function q(a, b) {
  if (!a || !b) {
    return;
  }
  if (a.length === b.length) {
    return true;
  } else {
    return false;
  }
}
```

**✨ Clean Code:**

```javascript
function hasSameLength(array1, array2) {
  if (!array1 || !array2) return false;
  return array1.length === array2.length;
}
```

---

## 🧪 Tambahkan Comment Saat Perlu (Bukan Pengganti Nama yang Buruk)

```javascript
// ❌ Jangan begini:
let x = 86400; // jumlah detik dalam sehari

// ✅ Lebih baik:
const SECONDS_IN_A_DAY = 86400;
```

---

## 🧰 Gunakan Tools Clean Code

| Tool        | Fungsi                         |
|-------------|--------------------------------|
| ESLint      | Deteksi potensi error dan gaya |
| Prettier    | Auto-format kode               |
| Husky + lint-staged | Cegah commit buruk     |

```bash
npm install eslint prettier --save-dev
```

---

## 📏 Tambahan Tips Clean Code

- **Gunakan async/await**, hindari callback hell
- Gunakan **default parameters**
- Pecah kode ke dalam **modul kecil**
- Gunakan **array methods** seperti `.map()`, `.filter()`, `.reduce()` dibanding for loop kalau memungkinkan

---

## 🧘 Clean Code itu Seni, bukan Aturan Kaku

> "Clean code itu bukan tentang bikin komputer ngerti, tapi bikin developer lain ngerti."

Kamu gak harus 100% sempurna — yang penting terus improve. Sedikit demi sedikit, lama-lama kode kamu bakal makin kece ✨

---

## 📚 Referensi Tambahan

- [Clean Code oleh Robert C. Martin](https://www.goodreads.com/book/show/3735293-clean-code)
- [JavaScript Clean Code (Dev.to)](https://dev.to)
- [Airbnb JavaScript Style Guide](https://github.com/airbnb/javascript)

---

## 🚀 Kesimpulan

Clean code bikin hidup kamu dan tim kamu lebih mudah. Kode yang bersih = lebih sedikit bug, lebih mudah maintenance, dan lebih profesional.

Mulai biasakan dari sekarang! 💪

```
