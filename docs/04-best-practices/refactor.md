
```markdown
# 🔧 Refactoring JavaScript: Biar Kode Gak Kayak Mie Kusut

Refactoring adalah seni memperbaiki struktur kode tanpa mengubah fungsinya. Bukan cuma biar "keliatan rapi", tapi biar lebih **mudah dibaca, di-debug, di-maintain, dan di-scale**. Coding itu bukan lomba cepat-cepetan, tapi lomba siapa yang bikin kode bisa dinikmati developer lain — termasuk kamu sendiri di masa depan 😄

---

## 🤔 Kenapa Perlu Refactor?

- Kode sulit dibaca & dimengerti
- Banyak pengulangan (DRY dong!)
- Fungsi terlalu panjang
- Nama variabel gak jelas (`x`, `data1`, `temp`??)
- Struktur tidak konsisten
- Performa bisa ditingkatkan
- Waktu revisit project, kamu pengen nangis

---

## 🪚 Prinsip Refactoring

| Prinsip         | Makna                                                                 |
|------------------|-----------------------------------------------------------------------|
| DRY              | Don’t Repeat Yourself – Hindari duplikasi kode                       |
| KISS             | Keep It Simple, Stupid – Sederhanakan logika                         |
| SRP              | Single Responsibility Principle – Satu fungsi = satu tugas           |
| YAGNI            | You Aren’t Gonna Need It – Jangan overengineering                    |
| Meaningful Names | Gunakan nama variabel dan fungsi yang menjelaskan maksudnya          |

---

## 🛠️ Contoh Refactor

### 1. Nama Variabel & Fungsi yang Buruk

❌ Sebelum:

```javascript
function a(d) {
  return d * 12.5 / 100;
}
```

✅ Sesudah:

```javascript
function hitungDiskon(persen) {
  return persen * 12.5 / 100;
}
```

---

### 2. Duplikasi Kode

❌ Sebelum:

```javascript
if (role === 'admin') {
  console.log('Hai admin!');
}
if (role === 'admin') {
  aksesAdmin();
}
```

✅ Sesudah:

```javascript
if (role === 'admin') {
  console.log('Hai admin!');
  aksesAdmin();
}
```

---

### 3. Fungsi Panjang

❌ Fungsi terlalu panjang:

```javascript
function prosesUser(user) {
  // validasi
  if (!user.nama) throw 'Nama wajib';
  if (!user.email) throw 'Email wajib';
  // format data
  user.nama = user.nama.toUpperCase();
  user.email = user.email.toLowerCase();
  // simpan
  saveToDB(user);
}
```

✅ Dipecah jadi fungsi kecil:

```javascript
function validasiUser(user) {
  if (!user.nama) throw 'Nama wajib';
  if (!user.email) throw 'Email wajib';
}

function formatUser(user) {
  return {
    ...user,
    nama: user.nama.toUpperCase(),
    email: user.email.toLowerCase()
  };
}

function prosesUser(user) {
  validasiUser(user);
  const dataSiap = formatUser(user);
  saveToDB(dataSiap);
}
```

---

### 4. Refactor IF/ELSE Menjadi Object Lookup

❌ Banyak if-else:

```javascript
if (status === 'aktif') {
  return 'User aktif';
} else if (status === 'nonaktif') {
  return 'User nonaktif';
} else if (status === 'banned') {
  return 'User diblokir';
}
```

✅ Pakai object lookup:

```javascript
const statusMap = {
  aktif: 'User aktif',
  nonaktif: 'User nonaktif',
  banned: 'User diblokir'
};

return statusMap[status] || 'Status tidak dikenal';
```

---

## 🧪 Tips Refactor Aman

1. **Unit Test itu wajib** sebelum refactor!
2. Refactor perlahan, satu bagian kecil dulu
3. Jangan refactor sambil nambah fitur baru
4. Gunakan formatter otomatis (Prettier, ESLint)
5. Commit kecil per perubahan, jangan 1 commit besar

---

## 🔥 Tools Bantu Refactoring

- [ESLint](https://eslint.org/) → untuk deteksi potensi masalah kode
- [Prettier](https://prettier.io/) → auto format kode
- [Jest](https://jestjs.io/) → untuk testing
- VSCode Refactor tools (`F2`, `Ctrl+Shift+R`, dsb)

---

## 🚀 Kesimpulan

Refactoring itu kaya bebersih rumah. Emang capek di awal, tapi bikin nyaman dan enak ditinggali lama-lama.

> "Refactor itu bukan tentang mengubah kode, tapi bikin kode jadi punya masa depan." — Dev bijak ✨

Rutin refactor = kode sehat + developer waras = tim produktif 💪
```
