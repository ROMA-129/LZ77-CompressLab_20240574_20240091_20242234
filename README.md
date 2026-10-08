# 🗜️ LZ77 Compression & Decompression Tool

A crisp, lightweight Python implementation of the **LZ77 Lossless Data Compression Algorithm**, featuring sliding-window pattern matching, automated tag generation, decompression, and a clean Tkinter Graphical User Interface (GUI). 

Developed as a group project for the **Information Theory & Data Compression** course.

---

## ✨ Features

* **Sliding Window Matching:** Efficiently parses input text using dynamic Search and Lookahead buffers.
* **Tag Generation:** Converts repetitive patterns into `(Offset, Length, Next Symbol)` tags.
* **Lossless Reconstruction:** Accurately reconstructs original files from tag files without data loss.
* **Special Character Handling:** Robust encoding/decoding for whitespace, newlines (`\n`), tabs (`\t`), and commas.
* **User-Friendly GUI:** Clean, dark-themed Tkinter interface with High-DPI support for crisp rendering on modern screens.

---

## 👥 Team Members

| Name | Academic ID |
| :--- | :--- |
| **Mariam Said Hanafy** | 20240574 |
| **Omnia Ramadan** | 20240091 |
| **Amr Tariq Hawash** | 20242234 |

---

## 🛠️ Project Structure

```text
├── Compression.py      # Core LZ77 compression & sliding window logic
├── Decompression.py    # Reconstructs original text from generated tags
├── Matching.py         # Pattern matching helper utilities
├── Main.py             # Desktop GUI interface (Tkinter)
└── README.md           # Project documentation
