# 📊 NumPy Cheat Sheet (with Examples)

A concise reference for NumPy functions and concepts — formatted in tables and ready for copy-paste.

---

## 🔧 Array Creation

| Function                             | Description                              | Example                                          |
| ------------------------------------ | ---------------------------------------- | ------------------------------------------------ |
| `np.array(object)`                   | Creates a NumPy array from list or tuple | `np.array([1, 2, 3])`                            |
| `np.zeros(shape)`                    | Creates array of zeros                   | `np.zeros((2, 3))` → `[[0. 0. 0.], [0. 0. 0.]]`  |
| `np.ones(shape)`                     | Creates array of ones                    | `np.ones(4)` → `[1. 1. 1. 1.]`                   |
| `np.full(shape, fill_value)`         | Creates array filled with a value        | `np.full((2,2), 5)` → `[[5 5],[5 5]]`            |
| `np.arange(start, stop[, step])`     | Creates evenly spaced values             | `np.arange(0, 10, 2)` → `[0 2 4 6 8]`            |
| `np.linspace(start, stop, num)`      | Creates num evenly spaced values         | `np.linspace(0, 1, 5)` → `[0. 0.25 0.5 0.75 1.]` |
| `np.eye(n)`                          | Identity matrix                          | `np.eye(3)`                                      |
| `np.random.rand(n)`                  | Random floats (0–1)                      | `np.random.rand(3)` → `[0.2 0.7 0.9]`            |
| `np.random.randint(low, high, size)` | Random integers                          | `np.random.randint(0,10,(2,2))`                  |

---

## 🧮 Array Operations

| Function                  | Description                 | Example                                   |
| ------------------------- | --------------------------- | ----------------------------------------- |
| `a + b`                   | Element-wise addition       | `np.array([1,2])+np.array([3,4]) → [4 6]` |
| `a - b`                   | Element-wise subtraction    | `np.array([5,4])-np.array([2,1]) → [3 3]` |
| `a * b`                   | Element-wise multiplication | `np.array([1,2])*2 → [2 4]`               |
| `a / b`                   | Element-wise division       | `np.array([4,2])/2 → [2. 1.]`             |
| `np.dot(a, b)`            | Dot product                 | `np.dot([1,2],[3,4]) → 11`                |
| `np.sum(a)`               | Sum of all elements         | `np.sum([1,2,3]) → 6`                     |
| `np.mean(a)`              | Mean value                  | `np.mean([1,2,3]) → 2.0`                  |
| `np.median(a)`            | Median value                | `np.median([1,3,2]) → 2.0`                |
| `np.std(a)`               | Standard deviation          | `np.std([1,2,3]) → 0.82`                  |
| `np.var(a)`               | Variance                    | `np.var([1,2,3]) → 0.67`                  |
| `np.min(a)` / `np.max(a)` | Minimum/Maximum             | `np.max([1,5,2]) → 5`                     |

---

## 📐 Array Shape and Reshape

| Function                  | Description                        | Example                                         |
| ------------------------- | ---------------------------------- | ----------------------------------------------- |
| `a.shape`                 | Returns array dimensions           | `np.array([[1,2],[3,4]]).shape → (2,2)`         |
| `a.reshape(new_shape)`    | Reshapes array                     | `np.arange(6).reshape(2,3)`                     |
| `a.ravel()`               | Flattens array                     | `np.array([[1,2],[3,4]]).ravel() → [1 2 3 4]`   |
| `a.T`                     | Transpose                          | `np.array([[1,2],[3,4]]).T → [[2,1],[4,3]]`     |
| `np.expand_dims(a, axis)` | Adds new axis                      | `np.expand_dims([1,2,3], axis=0)` → `[[1 2 3]]` |
| `np.squeeze(a)`           | Removes single-dimensional entries | `np.squeeze([[1],[2],[3]]) → [1 2 3]`           |

---

## 🔍 Indexing & Slicing

| Function               | Description             | Example                  |
| ---------------------- | ----------------------- | ------------------------ |
| `a[i]`                 | Access element          | `a[0]` → first element   |
| `a[start:stop:step]`   | Slice array             | `a[1:4:2]`               |
| `a[:, i]`              | Column selection        | `a[:, 0]` → first column |
| `a[i, :]`              | Row selection           | `a[1, :]` → second row   |
| `a[a > 5]`             | Conditional filtering   | `a[a>5] → elements >5`   |
| `np.where(cond, x, y)` | Conditional replacement | `np.where(a>5, a, 0)`    |

---

## 🔢 Linear Algebra

| Function           | Description                | Example            |
| ------------------ | -------------------------- | ------------------ |
| `np.dot(a, b)`     | Dot product                | `np.dot(A, B)`     |
| `np.matmul(a, b)`  | Matrix multiplication      | `np.matmul(A,B)`   |
| `np.linalg.inv(a)` | Inverse of matrix          | `np.linalg.inv(A)` |
| `np.linalg.det(a)` | Determinant                | `np.linalg.det(A)` |
| `np.linalg.eig(a)` | Eigenvalues & eigenvectors | `np.linalg.eig(A)` |
| `np.trace(a)`      | Trace of matrix            | `np.trace(A)`      |

---

## 🧩 Miscellaneous Functions

| Function                      | Description             | Example                                     |
| ----------------------------- | ----------------------- | ------------------------------------------- |
| `np.unique(a)`                | Returns unique elements | `np.unique([1,1,2,3]) → [1 2 3]`            |
| `np.sort(a)`                  | Sort array              | `np.sort([3,1,2]) → [1 2 3]`                |
| `np.concatenate((a,b), axis)` | Join arrays             | `np.concatenate(([1,2],[3,4])) → [1 2 3 4]` |
| `np.vstack((a,b))`            | Stack vertically        | `np.vstack(([1,2],[3,4]))`                  |
| `np.hstack((a,b))`            | Stack horizontally      | `np.hstack(([1,2],[3,4]))`                  |
| `np.split(a, n)`              | Split array into parts  | `np.split(np.arange(6), 3)`                 |

---

✅ **Tip:** Import NumPy conventionally using:

```python
import numpy as np
```
