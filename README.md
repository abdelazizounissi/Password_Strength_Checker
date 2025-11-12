# 🔑 Password Strength Checker

A modern, user-friendly password strength checker that analyzes passwords and gives clear, actionable feedback to help users create stronger, safer passwords. Built with Python — works as a CLI tool and can be extended with a GUI.

## ✨ Features

- Strength Classification: Rates passwords (e.g., Weak / Moderate / Strong)
- Actionable Suggestions: Recommends improvements such as increasing length, adding character classes, or avoiding dictionary words
- Detects common weaknesses: short length, repeated characters, sequences, common patterns, and dictionary words
- Optional enhanced checks: support for libraries like zxcvbn for more advanced entropy estimates
- Copy & Paste Friendly: Easily copy suggested strong passwords or corrected examples
- Extensible: Add GUI (Tkinter/Qt) or web frontend with minimal changes

## 📋 Requirements

- Python 3.x
- tkinter (usually comes pre-installed with Python)

## 🚀 Installation & Usage

### Option 1: Run from Source

1. Clone this repository:
```bash
git clone https://github.com/abdelazizounissi/Password_Strength_Checker.git
cd Password_Strength_Checker
```

2. Run the application:
```bash
python pass.py
```

**Note**: Make sure `key.ico` is in the same directory as `pass.py` for the icon to display properly.

### Option 2: Download Pre-Built Application

Download the ready-to-use application:
- **[PasswordChecker_App.zip](PasswordChecker_App.zip)** - Standalone executable application (no Python installation required)

Simply download, extract, and run the application!

## 🎯 How to Use

1. **Enter a password**
2. **Check**: Click the "Check Strength" button to chechk your password
3. **Review the strength rating and suggestions**
4. **Apply suggestions **: You can use 

⚠️ **Note**: You must type a password for the app to work.

## 🖼️ Screenshots

<img width="490" height="408" alt="Screenshot 2025-11-12 114450" src="https://github.com/user-attachments/assets/59a1dc02-9e29-4a68-95f1-1d263a9ec898" />




## 🔒 Security Note

This tool analyzes passwords locally. Do NOT send real, sensitive passwords to third-party services.

## 🛠️ Building Executable (Optional)

If you want to create your own standalone executable:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed --icon=lock.ico password.py
```

## 📝 License

This project is open source and available for personal and educational use.

## 👤 Author

**Abdelaziz Ounissi**

© 2025 Abdelaziz Ounissi

## 🤝 Contributing

Feel free to fork this project and submit pull requests for any improvements!

## 📧 Support

If you encounter any issues or have suggestions, please open an issue on GitHub.

---

**Enjoy making passwords stronger and safer! 🔐**
