# Inequalities I — Detailed Lesson

## 1. AM-GM (Arithmetic Mean ≥ Geometric Mean)

### Statement

For nonnegative real numbers a₁, a₂, ..., aₙ:

(a₁ + a₂ + ... + aₙ)/n ≥ (a₁ · a₂ · ... · aₙ)^(1/ⁿ)

Equality holds iff a₁ = a₂ = ... = aₙ.

### Two-variable case

(a + b)/2 ≥ √(ab)  ⇔  a + b ≥ 2√(ab)

### Three-variable case

(a + b + c)/3 ≥ ³√(abc)  ⇔  a + b + c ≥ 3·³√(abc)

### How to use it

The key idea: if the product of your terms is constant, AM-GM gives you the minimum of their sum. If the sum is constant, it gives you the maximum of their product.

### Worked Example 1
Find the minimum of x + 4/x for x > 0.

Apply AM-GM to x and 4/x:
(x + 4/x)/2 ≥ √(x · 4/x) = √4 = 2
So x + 4/x ≥ 4.
Equality when x = 4/x ⇒ x² = 4 ⇒ x = 2 (since x > 0).

### Worked Example 2
Find the minimum of 3x + 12/x² for x > 0.

We need the product to be constant. Write as x + x + x + 12/x² and apply AM-GM to the four terms x, x, x, 12/x²:

(x + x + x + 12/x²)/4 ≥ (x · x · x · 12/x²)^(1/4) = (12x³/x²)^(1/4) = (12x)^(1/4)

That doesn't give a constant. Bad split.

Try: split 3x as (3x/2) + (3x/2) and pair with 12/x².
(3x/2 + 3x/2 + 12/x²)/3 ≥ ((3x/2)(3x/2)(12/x²))^(1/3) = (9x²/4 · 12/x²)^(1/3) = (27)^(1/3) = 3
So 3x + 12/x² ≥ 9.
Equality when 3x/2 = 12/x² ⇒ 3x³ = 24 ⇒ x³ = 8 ⇒ x = 2.

### Key technique: splitting terms

When a single term like kx appears, split it into k copies of x (or into equal parts) so that when multiplied with other terms, the variable cancels.

---

## 2. Cauchy-Schwarz Inequality

### Statement

For any real numbers a₁, ..., aₙ, b₁, ..., bₙ:

(a₁² + a₂² + ... + aₙ²)(b₁² + b₂² + ... + bₙ²) ≥ (a₁b₁ + a₂b₂ + ... + aₙbₙ)²

Equality when (a₁, ..., aₙ) is proportional to (b₁, ..., bₙ), i.e. a₁/b₁ = a₂/b₂ = ... = aₙ/bₙ.

### Two-variable form

(a² + b²)(x² + y²) ≥ (ax + by)²

### Three-variable form

(a² + b² + c²)(x² + y² + z²) ≥ (ax + by + cz)²

### How to use it

Use Cauchy when you have a sum of squares multiplied by another sum of squares, and you want to bound a sum of products.

### Worked Example 3
For positive x, y with x + 2y = 6, find the minimum of x² + y².

Apply Cauchy: (x² + y²)(1² + 2²) ≥ (x·1 + y·2)² = (x + 2y)² = 36
So (x² + y²)(5) ≥ 36 ⇒ x² + y² ≥ 36/5.
Equality when x/1 = y/2 ⇒ y = 2x. Then x + 4x = 6 ⇒ x = 6/5, y = 12/5.

### Worked Example 4
For a, b, c > 0 with a + b + c = 1, find the minimum of a² + b² + c².

Take (a² + b² + c²)(1² + 1² + 1²) ≥ (a + b + c)² = 1
So 3(a² + b² + c²) ≥ 1 ⇒ a² + b² + c² ≥ 1/3.
Equality when a = b = c = 1/3.

---

## 3. Engel Form (Titu's Lemma / Cauchy-Schwarz in Engel Form)

### Statement

For b₁, b₂, ..., bₙ > 0:

a₁²/b₁ + a₂²/b₂ + ... + aₙ²/bₙ ≥ (a₁ + a₂ + ... + aₙ)²/(b₁ + b₂ + ... + bₙ)

Equality when a₁/b₁ = a₂/b₂ = ... = aₙ/bₙ.

### How to use it

Use Engel when you have a sum of fractions with squares (or any squares) in the numerator and positive terms in the denominator.

### Worked Example 5
For x, y > 0 with x + y = 1, find the minimum of 1/x + 1/y.

Rewrite as 1²/x + 1²/y. By Engel:
1²/x + 1²/y ≥ (1 + 1)²/(x + y) = 4/1 = 4.
So 1/x + 1/y ≥ 4.
Equality when 1/x = 1/y ⇒ x = y = 1/2.

### Worked Example 6
For a, b, c > 0, prove (a + b + c)(1/a + 1/b + 1/c) ≥ 9.

1/a + 1/b + 1/c = 1²/a + 1²/b + 1²/c ≥ (1+1+1)²/(a+b+c) = 9/(a+b+c)
So (a+b+c)(1/a+1/b+1/c) ≥ 9.
Equality when a = b = c.

---

## 4. Strategy Guide

| Problem looks like | Try |
|---|---|
| Sum of terms, product is constant | AM-GM |
| Sum of squares times sum of squares | Cauchy-Schwarz |
| Sum of fractions with squares on top | Engel Form |
| Sum of reciprocals with fixed sum | Engel or AM-GM |
| Minimize sum given fixed sum of squares | Cauchy (or QM-AM) |
| Product of sums | AM-GM or Cauchy |

## 5. Checking Equality Conditions

A proof is incomplete without verifying equality is attainable.

Example: To show min of x + 4/x is 4 for x > 0, we must find x such that x = 4/x and x > 0. This gives x = 2, which is valid. The bound is tight.

If equality leads to a contradiction (e.g., negative value when variables must be positive), your application is wrong.

## 6. Common Mistakes Checklist

- [ ] Variables nonnegative when using AM-GM?
- [ ] Equality case achievable (with given constraints)?
- [ ] Inequality direction correct? (AM ≥ GM, not GM ≥ AM)
- [ ] Applied to the right expression? (e.g., Engel requires squares in numerator)
- [ ] All terms accounted for after splitting?
- [ ] Multiplying both sides by something that could be negative?
