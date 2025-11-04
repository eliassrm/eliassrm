# 🖨️ Python `print()` Function & Command-Line Colors Cheat Sheet (with `rich` Examples)

This cheat sheet covers advanced `print()` usage, **ANSI color codes**, and the **`rich` library** for styled command-line output.

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

| Code      | Style         | Example                             |
| --------- | ------------- | ----------------------------------- |
| `\033[1m` | Bold          | `print("\033[1mBold Text\033[0m")`  |
| `\033[3m` | Italic        | `print("\033[3mItalic\033[0m")`     |
| `\033[4m` | Underline     | `print("\033[4mUnderlined\033[0m")` |
| `\033[7m` | Inverted      | `print("\033[7mInverted\033[0m")`   |
| `\033[9m` | Strikethrough | `print("\033[9mDeleted\033[0m")`    |

---

## 🎨 Background Colors

| Code       | Background Color   | Example                              |
| ---------- | ------------------ | ------------------------------------ |
| `\033[41m` | Red background     | `print("\033[41mRed BG\033[0m")`     |
| `\033[42m` | Green background   | `print("\033[42mGreen BG\033[0m")`   |
| `\033[44m` | Blue background    | `print("\033[44mBlue BG\033[0m")`    |
| `\033[45m` | Magenta background | `print("\033[45mMagenta BG\033[0m")` |
| `\033[46m` | Cyan background    | `print("\033[46mCyan BG\033[0m")`    |

---

## 🧩 Combining Colors & Styles

You can combine multiple effects by chaining escape codes:

```python
print("\033[1;32;44mBold Green Text on Blue Background\033[0m")
```

---

## 🧠 Using the `colorama` Library

A cross-platform way to handle colors (especially on Windows).

```python
from colorama import Fore, Back, Style
print(Fore.RED + 'Error!' + Style.RESET_ALL)
```

| Constant                    | Description       |
| --------------------------- | ----------------- |
| `Fore.RED`, `Fore.GREEN`    | Text colors       |
| `Back.BLUE`, `Back.YELLOW`  | Background colors |
| `Style.BRIGHT`, `Style.DIM` | Styles            |

---

## 🌟 Using the `rich` Library for Styled Output

The [`rich`](https://github.com/Textualize/rich) library makes colorful and formatted console printing easy.

### 🔹 Installation

```bash
pip install rich
```

### 🔹 Basic Usage

```python
from rich import print
print("[bold green]Success![/bold green] File uploaded.")
```

### 🔹 Print with Emojis and Styles

```python
from rich import print
print("[yellow]:bulb:[/yellow] [bold cyan]Tip:[/bold cyan] Use f-strings for formatting!")
```

### 🔹 Pretty Tables

```python
from rich.table import Table
from rich.console import Console

console = Console()
table = Table(title="User Data")

table.add_column("Name", style="cyan")
table.add_column("Age", style="magenta")
table.add_row("Alice", "24")
table.add_row("Bob", "30")

console.print(table)
```

### 🔹 Progress Bar Example

```python
from rich.progress import track
import time

for step in track(range(10), description="Processing..."):
    time.sleep(0.2)
```

---

✅ **Tip:** Combine `print()`, ANSI codes, and `rich` to create clear, interactive command-line tools!
