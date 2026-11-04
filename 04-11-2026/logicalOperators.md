
## 1. Arithmetic operators in Python

| Operator | Name           | What it does                                   |
| -------- | -------------- | ---------------------------------------------- |
| `+`      | Addition       | Adds two numbers                               |
| `-`      | Subtraction    | Subtracts numbers                              |
| `*`      | Multiplication | Multiplies numbers                             |
| `/`      | Division       | Divides and returns a decimal (`float`)        |
| `//`     | Floor division | Divides and rounds down to the nearest integer |
| `%`      | Modulo         | Returns the remainder                          |
| `**`     | Exponentiation | Raises a number to a power                     |

## 2. Understanding `/`, `//` and `%`

These three are particularly important.

Let's use the same numbers for all three:

```
a = 17b = 5print(a / b)print(a // b)print(a % b)
```

Output:

```
3.4
3
2
```

Here's why:

A. `/` Normal division

```
17 / 5
```

\\[ 17 \div 5 = 3.4 \\]

Returns the actual division result.

B. `//` Floor division

```
17 // 5
```

How many complete times does 5 fit into 17?

\\[ 17 \div 5 = 3.4 \\]

Floor division rounds down to the nearest integer (for positive numbers, this means removing the decimal part).

Result: `3`

C. `%` Modulo

```
17 % 5
```

How much is left after dividing 17 into groups of 5?

\\[ 17 = (5 \times 3) + 2 \\]

Result: `2`

## 3. Other arithmetic operators

Exponentiation (`**`)

```
print(2 ** 3)
```

\\[ 2^3 = 2 \times 2 \times 2 = 8 \\]

Multiplication (`*`)

```
print(5 * 4)
```

Output: `20`

Addition and subtraction

```
print(10 + 5)  # 15print(10 - 5)  # 5
```

## 4. Comparison operators

These compare two values and return either `True` or `False`.

| Operator | Meaning               | Example  | Result |
| -------- | --------------------- | -------- | ------ |
| `==`     | Equal to              | `5 == 5` | True   |
| `!=`     | Not equal to          | `5 != 3` | True   |
| `>`      | Greater than          | `5 > 3`  | True   |
| `<`      | Less than             | `5 < 3`  | False  |
| `>=`     | Greater than or equal | `5 >= 5` | True   |
| `<=`     | Less than or equal    | `3 <= 5` | True   |

Important: `=` and `==` are different.

- `=` assigns a value.
- `==` compares two values.

## 5. Assignment operators

These are shortcuts for updating variables.

| Operator  | Equivalent to |
| --------- | ------------- |
| `x += 5`  | `x = x + 5`   |
| `x -= 5`  | `x = x - 5`   |
| `x *= 5`  | `x = x * 5`   |
| `x /= 5`  | `x = x / 5`   |
| `x //= 5` | `x = x // 5`  |
| `x %= 5`  | `x = x % 5`   |
| `x **= 2` | `x = x ** 2`  |

