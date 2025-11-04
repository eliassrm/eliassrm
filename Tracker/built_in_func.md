# 🐍 Python Built-in Functions Cheat Sheet (with Examples)

A quick reference of commonly used Python built-in functions, organized by category and formatted in tables.

---

## 🔢 Numeric Functions

| Function                          | Description                                      | Example                    |
| --------------------------------- | ------------------------------------------------ | -------------------------- |
| `abs(x)`                          | Returns the absolute value of x                  | `abs(-5) → 5`              |
| `round(x, n)`                     | Rounds x to n decimal places                     | `round(3.14159, 2) → 3.14` |
| `pow(x, y[, z])`                  | Returns x raised to the power y (mod z optional) | `pow(2, 3) → 8`            |
| `divmod(a, b)`                    | Returns (a // b, a % b)                          | `divmod(10, 3) → (3, 1)`   |
| `sum(iterable[, start])`          | Returns the sum of elements                      | `sum([1,2,3]) → 6`         |
| `min(iterable)` / `max(iterable)` | Return smallest/largest value                    | `min([5,1,8]) → 1`         |

---

## 📋 Sequence and Collection Functions

| Function                             | Description                     | Example                                          |
| ------------------------------------ | ------------------------------- | ------------------------------------------------ |
| `len(s)`                             | Returns the length of an object | `len('Python') → 6`                              |
| `sorted(iterable[, key][, reverse])` | Returns a new sorted list       | `sorted([3,1,2]) → [1,2,3]`                      |
| `reversed(seq)`                      | Returns reversed iterator       | `list(reversed('abc')) → ['c','b','a']`          |
| `enumerate(iterable, start=0)`       | Returns (index, value) pairs    | `list(enumerate(['a','b'])) → [(0,'a'),(1,'b')]` |
| `zip(*iterables)`                    | Combines multiple iterables     | `list(zip([1,2],["a","b"])) → [(1,'a'),(2,'b')]` |
| `any(iterable)`                      | True if any element is true     | `any([0, False, 5]) → True`                      |
| `all(iterable)`                      | True if all elements are true   | `all([1, True, 3]) → True`                       |
| `range(start, stop[, step])`         | Generates numbers in a range    | `list(range(1,5)) → [1,2,3,4]`                   |

---

## 🔤 String and Character Functions

| Function                       | Description                           | Example                           |
| ------------------------------ | ------------------------------------- | --------------------------------- |
| `str(obj)`                     | Converts object to string             | `str(123) → '123'`                |
| `chr(i)`                       | Returns character from Unicode code   | `chr(65) → 'A'`                   |
| `ord(c)`                       | Returns Unicode code of character     | `ord('A') → 65`                   |
| `format(value[, format_spec])` | Formats a value                       | `format(3.14159, '.2f') → '3.14'` |
| `repr(obj)`                    | Printable representation of an object | `repr('hi') → "'hi'"`             |

---

## 🧱 Type and Object Functions

| Function                     | Description                  | Example                        |
| ---------------------------- | ---------------------------- | ------------------------------ |
| `type(obj)`                  | Returns object type          | `type(3) → <class 'int'>`      |
| `isinstance(obj, classinfo)` | Checks object instance       | `isinstance(5, int) → True`    |
| `issubclass(cls, classinfo)` | Checks subclass relationship | `issubclass(bool, int) → True` |
| `id(obj)`                    | Memory address of object     | `id(5)`                        |
| `hash(obj)`                  | Returns hash value           | `hash('python')`               |

---

## 🧮 Conversion Functions

| Function                | Description            | Example                       |
| ----------------------- | ---------------------- | ----------------------------- |
| `int(x[, base])`        | Converts x to integer  | `int('10') → 10`              |
| `float(x)`              | Converts x to float    | `float('3.14') → 3.14`        |
| `complex(real[, imag])` | Creates complex number | `complex(2,3) → (2+3j)`       |
| `bool(x)`               | Converts x to Boolean  | `bool('') → False`            |
| `list(iterable)`        | Converts to list       | `list('abc') → ['a','b','c']` |
| `tuple(iterable)`       | Converts to tuple      | `tuple([1,2,3]) → (1,2,3)`    |
| `set(iterable)`         | Converts to set        | `set([1,2,2]) → {1,2}`        |
| `dict(mapping)`         | Creates dictionary     | `dict(a=1, b=2)`              |
| `bytes(iterable)`       | Converts to bytes      | `bytes('Hi','utf-8')`         |

---

## 📦 Input/Output Functions

| Function                             | Description           | Example                                |
| ------------------------------------ | --------------------- | -------------------------------------- |
| `print(*objects, sep=' ', end='\n')` | Prints objects        | `print('Hello','World') → Hello World` |
| `input(prompt)`                      | Reads line from input | `name = input('Name: ')`               |
| `open(file, mode)`                   | Opens a file object   | `open('file.txt','r')`                 |

---

## ⚙️ Functional Programming Tools

| Function                 | Description                     | Example                                          |
| ------------------------ | ------------------------------- | ------------------------------------------------ |
| `map(func, iterable)`    | Applies a function to all items | `list(map(str.upper, ['a','b'])) → ['A','B']`    |
| `filter(func, iterable)` | Filters elements                | `list(filter(lambda x: x>2, [1,2,3,4])) → [3,4]` |
| `lambda args: expr`      | Anonymous function              | `(lambda x: x*x)(3) → 9`                         |

---

## 🧩 Object Introspection and Attributes

| Function                        | Description                    | Example                        |
| ------------------------------- | ------------------------------ | ------------------------------ |
| `dir([object])`                 | Returns list of attributes     | `dir([])`                      |
| `vars([object])`                | Returns `__dict__` of object   | `vars()`                       |
| `help([object])`                | Displays help text             | `help(str)`                    |
| `getattr(obj, name[, default])` | Gets attribute value           | `getattr(str, 'upper')`        |
| `setattr(obj, name, value)`     | Sets attribute value           | `setattr(obj, 'x', 10)`        |
| `delattr(obj, name)`            | Deletes attribute              | `delattr(obj, 'x')`            |
| `hasattr(obj, name)`            | Checks if object has attribute | `hasattr(str, 'lower') → True` |

---

## 🪄 Utility and Misc Functions

| Function                                | Description                       | Example                      |
| --------------------------------------- | --------------------------------- | ---------------------------- |
| `eval(expression[, globals[, locals]])` | Evaluates an expression           | `eval('3+2') → 5`            |
| `exec(object[, globals[, locals]])`     | Executes Python code              | `exec('x=5')`                |
| `compile(source, filename, mode)`       | Compiles code to a code object    | `compile('x=5', '', 'exec')` |
| `globals()` / `locals()`                | Return current scope dictionaries | `globals()`                  |
| `callable(obj)`                         | Checks if callable                | `callable(len) → True`       |

---
### Escape Sequences in Strings

In Python (and many other programming languages), a backslash `\` followed by a character represents an **escape sequence**.

Below are some common escape characters:

| Escape Sequence | Meaning |
|-----------------|---------|
| `\n`            | New line |
| `\t`            | Tab (8 spaces) |
| `\\`            | Backslash (`\`) |
| `\'`            | Single quote (`'`) |
| `\"`            | Double quote (`"`) |
  
   



---
✅ **Tip:** List all built-in functions using:

```python
import builtins
print(dir(builtins))
```
