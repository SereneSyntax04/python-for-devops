# Bitwise Operators
> Story: Imagine you’re flipping switches on a control panel — ON or OFF. Computers think in just 1s and 0s. Bitwise operators let you work directly with those binary-level values. Sounds nerdy? Yep. But also powerful.

Bitwise operators are used to perform operations on the individual bits of integer values. These operators treat numbers as sequences of binary digits (0s and 1s), enabling low-level manipulation often used in areas like performance optimization, encryption, hardware control, etc.

## List of Bitwise Operators
| Operator | Name        | Description                                      |                                                 |
| -------- | ----------- | ------------------------------------------------ | ----------------------------------------------- |
| `&`      | Bitwise AND | Returns 1 if **both** corresponding bits are 1.  |                                                 |
| \`       | \`          | Bitwise OR                                       | Returns 1 if **either** corresponding bit is 1. |
| `^`      | Bitwise XOR | Returns 1 if bits are **different**.             |                                                 |
| `~`      | Bitwise NOT | Inverts all the bits. In Python, gives `-(n+1)`. |                                                 |
| `<<`     | Left Shift  | Shifts bits to the left (multiplies by 2ⁿ).      |                                                 |
| `>>`     | Right Shift | Shifts bits to the right (divides by 2ⁿ, floor). |                                                 |


## 📝 Key Points to Remember
- Bitwise operations only work on integers.
- These are useful for performance-critical or hardware-interfacing tasks.
- Python stores integers with signed bits, so the result of ~ (bitwise NOT) might seem confusing:
  ~n = -(n + 1)

  [example]()
