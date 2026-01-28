# 🧮 Advanced Scientific Calculator

A robust, desktop-style scientific calculator built with Python and Tkinter. This application supports standard arithmetic, trigonometric functions, logarithmic calculations, and includes a built-in history tracker.



## ✨ Features

* **Scientific Functions**: Support for `sin`, `cos`, `tan`, `sqrt`, `log`, and constants like `π`.
* **History Sidebar**: Automatically records every calculation performed during the session.
* **Export to Text**: Save your entire calculation history to a `.txt` file with one click.
* **Error Handling**: Built-in validation to prevent crashes during invalid mathematical operations (e.g., division by zero).
* **Clean UI**: A simple, user-friendly interface designed for desktop use.

## 🚀 Getting Started

### Prerequisites
* Python 3.x
* Tkinter (usually comes pre-installed with Python)

### Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/Scientific-Calculator.git](https://github.com/YOUR_USERNAME/Scientific-Calculator.git)

Navigate to the directory:

Bash
cd Scientific-Calculator
Run the application:

Bash
python main.py
📦 Creating a Standalone Executable
To turn this script into a separate .exe (Windows) or .app (macOS), use PyInstaller:

Bash
pip install pyinstaller
pyinstaller --noconsole --onefile main.py
The finished application will be located in the dist/ folder.

🛠️ Built With
Python - The programming language used.

Tkinter - GUI framework.

Math Module - For scientific calculations.
