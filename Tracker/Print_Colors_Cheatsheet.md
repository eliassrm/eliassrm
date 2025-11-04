# 🖨️ Python `print()` Function & Command-Line Colors Cheat Sheet

This cheat sheet covers advanced `print()` usage and how to add **colors and formatting** to your command-line output.

---

## 🧾 `print()` Function Basics

| Example                            | Description                                        |
| ---------------------------------- | -------------------------------------------------- |
| `print("Hello World")`             | Prints text to the console.                        |
| `print("A", "B", sep=", ")`        | Custom separator (default: space).                 |
| `print("Line 1", end=" ")`         | Custom end character (default: `\n`).              |
| `print(f"Sum: {2 + 3}")`           | f-string formatting.                               |
| `print("{:>10}".format("right"))`  | Right-align text with `format()`.                  |
| `print("{:^10}".format("center"))` | Center-align text.                                 |
| `print("{:.2f}".format(3.14159))`  | Format float to 2 decimal places.                  |
| `print(*[1,2,3], sep=" - ")`       | Print list elements separated by custom character. |
| `print("Error!", file=sys.stderr)` | Print to error stream instead of stdout.           |

---

## 🌈 Command-Line Colors (ANSI Escape Codes)

Use **ANSI escape sequences** to colorize text in the terminal.

| Code       | Color           | Example                       |
| ---------- | --------------- | ----------------------------- |
| `\033[0m`  | Reset (default) | `print("\033[0mReset")`       |
| `\033[30m` | Black           | `print("\033[30mBlack Text")` |
| `\033[31m` | Red             | `print("\033[31mError!")`     |
| `\033[32m` | Green           | `print("\033[32mSuccess!")`   |
| `\033[33m` | Yellow          | `print("\033[33mWarning!")`   |
| `\033[34m` | Blue            | `print("\033[34mInfo")`       |
| `\033[35m` | Magenta         | `print("\033[35mNotice")`     |
| `\033[36m` | Cyan            | `print("\033[36mData")`       |
| `\033[37m` | White           | `print("\033[37mPlain Text")` |

✅ Example:

```python
print("\033[32mSuccess:\033[0m File uploaded successfully!")
```

---

## 🖌️ Text Styles

| Code      | Style                 | Example                             |
| --------- | --------------------- | ----------------------------------- |
| `\033[1m` | Bold                  | `print("\033[1mBold Text\033[0m")`  |
| `\033[2m` | Dim                   | `print("\033[2mDim Text\033[0m")`   |
| `\033[3m` | Italic                | `print("\033[3mItalic\033[0m")`     |
| `\033[4m` | Underline             | `print("\033[4mUnderlined\033[0m")` |
| `\033[7m` | Inverted (swap bg/fg) | `print("\033[7mInverted\033[0m")`   |
| `\033[9m` | Strikethrough         | `print("\033[9mDeleted\033[0m")`    |

---

## 🎨 Background Colors

| Code       | Background Color   | Example                              |
| ---------- | ------------------ | ------------------------------------ |
| `\033[40m` | Black background   | `print("\033[40mBlack BG\033[0m")`   |
| `\033[41m` | Red background     | `print("\033[41mRed BG\033[0m")`     |
| `\033[42m` | Green background   | `print("\033[42mGreen BG\033[0m")`   |
| `\033[43m` | Yellow background  | `print("\033[43mYellow BG\033[0m")`  |
| `\033[44m` | Blue background    | `print("\033[44mBlue BG\033[0m")`    |
| `\033[45m` | Magenta background | `print("\033[45mMagenta BG\033[0m")` |
| `\033[46m` | Cyan background    | `print("\033[46mCyan BG\033[0m")`    |
| `\033[47m` | White background   | `print("\033[47mWhite BG\033[0m")`   |

---

## 🧩 Combining Colors & Styles

You can combine multiple effects by chaining escape codes:

```python
print("\033[1;32;44mBold Green Text on Blue Background\033[0m")
```

---

## 💡 Tips

* Always end color sequences with `\033[0m` to reset formatting.
* Works in most terminals (Linux, macOS, Windows 10+ with ANSI support).
* For advanced styling, consider using the **`colorama`** or **`rich`** libraries.

✅ Example with `colorama`:

```python
from colorama import Fore, Back, Style
print(Fore.RED + 'Error!' + Style.RESET_ALL)
```

---

✨ **Pro Tip:** You can create reusable color constants:

```python
RED = "\033[31m"
RESET = "\033[0m"
print(f"{RED}Error!{RESET}")
```
