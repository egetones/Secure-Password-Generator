<div align="center">

# 🔐 Secure Password Generator

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Windows-lightgrey)

<p>
  <strong>Generates cryptographically strong passwords directly from your terminal.</strong>
</p>

[Report Bug](https://github.com/your-username/secure-pass-gen/issues) · [Request Feature](https://github.com/your-username/secure-pass-gen/issues)

</div>

---

## 📖 Description

**Secure Password Generator** is a Python-based CLI tool designed to create robust passwords for high-security needs.

Unlike the standard Python `random` library (which is pseudo-random and predictable), this tool utilizes the **`secrets`** module. This ensures that generated passwords are cryptographically strong and suitable for managing sensitive credentials.

### ✨ Key Features

* **🛡️ Cryptographically Secure:** Built on the `secrets` module for unpredictability.
* **⚙️ Highly Customizable:** Define exact length, toggle numbers, and include special symbols.
* **🚀 CLI Focused:** Fast execution via terminal arguments, perfect for piping into other tools.
* **🐧 Cross-Platform:** Works seamlessly on Linux, macOS, and Windows.

---

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/secure-pass-gen.git](https://github.com/your-username/secure-pass-gen.git)
````

2.  **Navigate to the project directory:**
    ```bash
    cd secure-pass-gen
    ```

-----

## 💻 Usage

Run the script using Python. You can customize the password using flags.

**Basic Example:**

```bash
python3 passgen.py -l 20 -s -n
```

### Argument Reference

| Argument | Description | Example |
| :--- | :--- | :--- |
| `-l` / `--length` | Sets the length of the password (default: 12). | `-l 24` |
| `-n` / `--numbers` | Include numbers (0-9) in the password. | `-n` |
| `-s` / `--symbols` | Include special characters (\!@\#$...). | `-s` |
| `-h` / `--help` | Show the help message and exit. | `-h` |

-----

## 🎓 Key Takeaways & Learnings

While developing this project, I focused on mastering the following concepts:

  * **CLI Development:** Learned how to parse command-line arguments efficiently using Python's `argparse` library.
  * **Cryptography Basics:** Understood the critical difference between `random` (pseudo-random) and `secrets` (cryptographically secure) modules in Python.
  * **String Manipulation:** Improved logic for combining and shuffling character sets dynamically.

-----

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.

```
```
