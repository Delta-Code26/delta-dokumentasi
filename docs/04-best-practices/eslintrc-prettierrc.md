
## 🧠 File `.eslintrc.js`

```js
module.exports = {
  env: {
    browser: true,
    es2021: true,
    node: true,
  },
  extends: [
    "eslint:recommended",
    "prettier", // Integrasi biar gak tabrakan sama Prettier
  ],
  parserOptions: {
    ecmaVersion: "latest",
    sourceType: "module",
  },
  rules: {
    // 🚨 Gaya koding konsisten
    indent: ["error", 2],
    quotes: ["error", "single"],
    semi: ["error", "always"],
    "no-unused-vars": ["warn"],
    "no-console": ["warn"],
    "no-debugger": ["error"],

    // ✨ Optional tambahan
    "prefer-const": ["error"],
    "eqeqeq": ["error", "always"],
    "no-var": ["error"],
  },
};
```

---

## 🎨 File `.prettierrc`

```json
{
  "semi": true,
  "singleQuote": true,
  "printWidth": 80,
  "tabWidth": 2,
  "useTabs": false,
  "trailingComma": "es5",
  "bracketSpacing": true,
  "arrowParens": "avoid"
}
```

---

## 🧩 Opsional: Tambahkan Script di `package.json`

Kalau kamu pake Node.js dan punya `package.json`, tambahin:

```json
"scripts": {
  "lint": "eslint .",
  "format": "prettier --write ."
}
```

---

## 🚀 Bonus: Auto-fix pas save (di VSCode)

1. Install extensions:
   - ESLint
   - Prettier – Code formatter

2. Lalu tambahkan ke `settings.json` VSCode:

```json
{
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.fixAll": true,
    "source.fixAll.eslint": true
  },
  "eslint.validate": ["javascript"],
  "prettier.enable": true
}
```
