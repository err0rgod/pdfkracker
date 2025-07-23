# 🔐 PDF Password Cracker

A lightweight Python tool to **brute-force crack password-protected PDF files** using a wordlist.

> 📂 Supports both user-provided wordlists and a default fallback.  
> 🛠️ Uses `pikepdf` for fast, silent password attempts.

---

## 🚀 Features

- ✅ Attempts to unlock PDF using a wordlist (brute-force style)
- ⚡ Fast and simple — just point to a file and wordlist
- 🧠 Automatically skips empty/blank lines in wordlists
- 🔒 Clean failure handling for wrong passwords
- 📜 Works with encrypted PDFs (user-password protected)

---

## 📦 Installation

### 🔹 Auto install (with `setup.sh`)

```bash
chmod +x setup.sh
./setup.sh
```

### 🔹 Manual install

```bash
pip install -r requirements.txt
```

---

## ⚙️ Usage

```bash
python crackpdf.py -p <pdf_file> -w <wordlist>
```

### 🧪 Examples

#### 🔹 Crack with custom wordlist:
```bash
python crackpdf.py -p secret.pdf -w rockyou.txt
```

#### 🔹 Use default `passwords.txt`:
```bash
python crackpdf.py -p secret.pdf
```

> The tool checks each password and prints the correct one when found.

---

## 📁 Project Structure

```
pdf-cracker/
├── crackpdf.py          # Main password cracker script
├── requirements.txt     # Contains pikepdf
├── setup.sh             # Installs dependencies
├── passwords.txt        # (Optional) default wordlist file
└── README.md
```

---

## 📜 Sample Output

```
Password found: letmein123
```

If the password is not in the wordlist:

```
Password not found in the provided wordlist.
```

---

##  Legal Disclaimer

This tool is for **educational and authorized use only**.  
Do **not** use this on documents you do not have permission to access.

---

##  Author

**err0rgod**  
> _"If it’s locked by a password, it’s still just code."_
