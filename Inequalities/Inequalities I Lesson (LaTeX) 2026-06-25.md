# Inequalities I — Detailed Lesson (LaTeX)

## 1. AM-GM (Arithmetic Mean $\geq$ Geometric Mean)

### Statement

For nonnegative real numbers $a_1, a_2, \dots, a_n$:

$$\frac{a_1 + a_2 + \cdots + a_n}{n} \geq \sqrt[n]{a_1 a_2 \cdots a_n}$$

Equality holds iff $a_1 = a_2 = \cdots = a_n$.

### Two-variable case

$$\frac{a + b}{2} \geq \sqrt{ab} \quad\Longleftrightarrow\quad a + b \geq 2\sqrt{ab}$$

### Three-variable case

$$\frac{a + b + c}{3} \geq \sqrt[3]{abc} \quad\Longleftrightarrow\quad a + b + c \geq 3\sqrt[3]{abc}$$

### Key idea

If the product of your terms is constant, AM-GM gives the minimum of their sum. If the sum is constant, it gives the maximum of their product.

### Worked Example 1
Find the minimum of $x + \frac{4}{x}$ for $x > 0$.

Apply AM-GM to $x$ and $\frac{4}{x}$:

$$\frac{x + \frac{4}{x}}{2} \geq \sqrt{x \cdot \frac{4}{x}} = \sqrt{4} = 2$$

So $x + \frac{4}{x} \geq 4$. Equality when $x = \frac{4}{x} \Rightarrow x^2 = 4 \Rightarrow x = 2$.

### Worked Example 2
Find the minimum of $3x + \frac{12}{x^2}$ for $x > 0$.

Split $3x$ as $\frac{3x}{2} + \frac{3x}{2}$ and apply AM-GM to $\frac{3x}{2}, \frac{3x}{2}, \frac{12}{x^2}$:

$$\frac{\frac{3x}{2} + \frac{3x}{2} + \frac{12}{x^2}}{3} \geq \sqrt[3]{\frac{3x}{2} \cdot \frac{3x}{2} \cdot \frac{12}{x^2}} = \sqrt[3]{\frac{9x^2}{4} \cdot \frac{12}{x^2}} = \sqrt[3]{27} = 3$$

So $3x + \frac{12}{x^2} \geq 9$. Equality when $\frac{3x}{2} = \frac{12}{x^2} \Rightarrow x^3 = 8 \Rightarrow x = 2$.

### Key technique: splitting terms

When you have $kx$, split it into $k$ copies of $x$ (or equal parts) so the variable cancels when multiplied with other terms.

---

## 2. Cauchy-Schwarz Inequality

### Statement

For any real numbers $a_1, \dots, a_n$, $b_1, \dots, b_n$:

$$(a_1^2 + a_2^2 + \cdots + a_n^2)(b_1^2 + b_2^2 + \cdots + b_n^2) \geq (a_1 b_1 + a_2 b_2 + \cdots + a_n b_n)^2$$

Equality when $(a_1, \dots, a_n)$ is proportional to $(b_1, \dots, b_n)$, i.e. $\frac{a_1}{b_1} = \frac{a_2}{b_2} = \cdots = \frac{a_n}{b_n}$.

### Two-variable form

$$(a^2 + b^2)(x^2 + y^2) \geq (ax + by)^2$$

### Three-variable form

$$(a^2 + b^2 + c^2)(x^2 + y^2 + z^2) \geq (ax + by + cz)^2$$

### How to use it

Use Cauchy when you have a sum of squares multiplied by another sum of squares, and you want to bound a sum of products.

### Worked Example 3
For positive $x, y$ with $x + 2y = 6$, find the minimum of $x^2 + y^2$.

Apply Cauchy: $(x^2 + y^2)(1^2 + 2^2) \geq (x \cdot 1 + y \cdot 2)^2 = (x + 2y)^2 = 36$

So $(x^2 + y^2)(5) \geq 36 \Rightarrow x^2 + y^2 \geq \frac{36}{5}$.

Equality when $\frac{x}{1} = \frac{y}{2} \Rightarrow y = 2x$. Then $x + 4x = 6 \Rightarrow x = \frac{6}{5},\; y = \frac{12}{5}$.

### Worked Example 4
For $a, b, c > 0$ with $a + b + c = 1$, find the minimum of $a^2 + b^2 + c^2$.

$$(a^2 + b^2 + c^2)(1^2 + 1^2 + 1^2) \geq (a + b + c)^2 = 1$$

So $3(a^2 + b^2 + c^2) \geq 1 \Rightarrow a^2 + b^2 + c^2 \geq \frac{1}{3}$.

Equality when $a = b = c = \frac{1}{3}$.

---

## 3. Engel Form (Titu's Lemma)

### Statement

For $b_1, b_2, \dots, b_n > 0$:

$$\frac{a_1^2}{b_1} + \frac{a_2^2}{b_2} + \cdots + \frac{a_n^2}{b_n} \geq \frac{(a_1 + a_2 + \cdots + a_n)^2}{b_1 + b_2 + \cdots + b_n}$$

Equality when $\frac{a_1}{b_1} = \frac{a_2}{b_2} = \cdots = \frac{a_n}{b_n}$.

This is a direct corollary of Cauchy-Schwarz (take $a_i/\sqrt{b_i}$ and $\sqrt{b_i}$).

### Worked Example 5
For $x, y > 0$ with $x + y = 1$, find the minimum of $\frac{1}{x} + \frac{1}{y}$.

$$\frac{1^2}{x} + \frac{1^2}{y} \geq \frac{(1 + 1)^2}{x + y} = \frac{4}{1} = 4$$

So $\frac{1}{x} + \frac{1}{y} \geq 4$. Equality when $\frac{1}{x} = \frac{1}{y} \Rightarrow x = y = \frac{1}{2}$.

### Worked Example 6
For $a, b, c > 0$, prove $(a + b + c)\left(\frac{1}{a} + \frac{1}{b} + \frac{1}{c}\right) \geq 9$.

$$\frac{1}{a} + \frac{1}{b} + \frac{1}{c} = \frac{1^2}{a} + \frac{1^2}{b} + \frac{1^2}{c} \geq \frac{(1+1+1)^2}{a+b+c} = \frac{9}{a+b+c}$$

So $(a+b+c)\left(\frac{1}{a} + \frac{1}{b} + \frac{1}{c}\right) \geq (a+b+c) \cdot \frac{9}{a+b+c} = 9$.

Equality when $a = b = c$.

---

## 4. Strategy Guide

| Problem looks like | Try |
|---|---|
| Sum of terms, product is constant | AM-GM |
| Sum of squares $\times$ sum of squares | Cauchy-Schwarz |
| Sum of fractions $\frac{\square^2}{\square}$ | Engel Form |
| Sum of reciprocals with fixed sum | Engel or AM-GM |
| Minimize sum given fixed sum of squares | Cauchy (or QM-AM) |
| Product of sums | AM-GM or Cauchy |

---

## 5. Checking Equality Conditions

A proof is incomplete without verifying equality is attainable.

Example: To show $\min(x + \frac{4}{x}) = 4$ for $x > 0$, we must find $x$ such that $x = \frac{4}{x}$ and $x > 0$. This gives $x = 2$, which is valid. The bound is tight.

If equality leads to a contradiction (e.g., negative value when variables must be positive), your application is wrong.

---

## 6. Common Mistakes Checklist

- [ ] Variables nonnegative when using AM-GM?
- [ ] Equality case achievable (with given constraints)?
- [ ] Inequality direction correct? (AM $\geq$ GM, not GM $\geq$ AM)
- [ ] Applied to the right expression? (e.g., Engel requires squares in numerator)
- [ ] All terms accounted for after splitting?
- [ ] Multiplying both sides by something that could be negative?
