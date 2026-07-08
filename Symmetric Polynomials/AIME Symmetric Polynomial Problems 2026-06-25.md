# Real AIME Problems — Symmetric Polynomials

## Problem 1 ✅ (1996 AIME #5)

Suppose that the roots of x³ + 3x² + 4x − 11 = 0 are a, b, c, and that the roots of x³ + rx² + sx + t = 0 are a + b, b + c, c + a. Find t. → 23

Solution: By Vieta, a+b+c = −3, ab+bc+ca = 4, abc = 11. Then (a+b)(b+c)(c+a) = (a+b+c)(ab+bc+ca) − abc = (−3)(4) − 11 = −23. Since the constant term of the second cubic is −(a+b)(b+c)(c+a) = t, we get t = 23.

---

## Problem 2 ✅ (2008 AIME II #7)

Let r, s, and t be the three roots of the equation

8x³ + 1001x + 2008 = 0.

Find (r + s)³ + (s + t)³ + (t + r)³. → 753

Solution: No x² term → r+s+t = 0, so r+s = −t, etc. Expression = (−t)³+(−r)³+(−s)³ = −(r³+s³+t³). From 8r³+1001r+2008 = 0, summing gives 8(r³+s³+t³) + 1001(0) + 3·2008 = 0 → r³+s³+t³ = −753. Answer = 753.

---

## Problem 3 ✅ (2003 AIME II #9)

Consider the polynomials

P(x) = x⁶ − x⁵ − x³ − x² − x

Q(x) = x⁴ − x³ − x² − 1

Given that z₁, z₂, z₃, z₄ are the roots of Q(x) = 0, find P(z₁) + P(z₂) + P(z₃) + P(z₄). → 6

Solution: From Q(z)=0, z⁴ = z³+z²+1. Then z⁵ = z⁴+z³+z, z⁶ = z⁵+z⁴+z². Substitute into P(z): P(z) = (z⁵+z⁴+z²) − z⁵ − z³ − z² − z = z⁴ − z³ − z = (z³+z²+1) − z³ − z = z² − z + 1. Summing: ∑z² − ∑z + 4. By Vieta on Q: ∑z = 1, ∑z² = (∑z)² − 2∑zᵢzⱼ = 1 − 2(−1) = 3. So answer = 3 − 1 + 4 = 6.

---

## Problem 4 ✅ (2005 AIME I #8)

The equation 2^{333x−2} + 2^{111x+2} = 2^{222x+1} + 1 has three real roots. Given that their sum is m/n where m and n are relatively prime positive integers, find m + n. → 113

Solution: Let y = 2^{111x}. Then 2^{333x} = y³, 2^{222x} = y². The equation becomes y³/4 + 4y = 2y² + 1 → y³ − 8y² + 16y − 4 = 0. By Vieta, y₁y₂y₃ = 4. Sum of x-roots = (log₂ y₁ + log₂ y₂ + log₂ y₃)/111 = log₂(y₁y₂y₃)/111 = log₂(4)/111 = 2/111. So m=2, n=111, m+n=113.

---

## Problem 5 ✅ (2001 AIME I #3)

Find the sum of the roots, real and non-real, of the equation

(x² − 7x + 11)^(x² − 13x + 42) = 1

given that there are no multiple roots. → 27

Solution: Cases: (i) a=1 → x²−7x+11=1 → x=2,5. (ii) a=−1, b even → x²−7x+11=−1 → x=3,4; b=12,6 both even. (iii) b=0, a≠0 → x²−13x+42=0 → x=6,7; a≠0. Roots are 2,3,4,5,6,7. Sum = 27.

---

## Problem 6 ✅ (1995 AIME #5)

For certain real values of a, b, c, and d, the equation

x⁴ + ax³ + bx² + cx + d = 0

has four non-real roots. The product of two of these roots is 13 + i and the sum of the other two roots is 3 + 4i. Find b. → 51

Solution: Roots are p, p̅, q, q̅. Given p·q = 13+i ⇒ p̅·q̅ = 13−i, and p̅+q̅ = 3+4i ⇒ p+q = 3−4i. Then (p+q)(p̅+q̅) = |p|² + |q|² + p·q̅ + p̅·q = 25. Now b = |p|² + |q|² + (p·q + p̅·q̅) + (p·q̅ + p̅·q) = 26 + 25 = 51.

---

## Problem 7 ✅ (AIME-style synthesis)

Let x and y be real numbers such that

x + y = 4, x³ + y³ = 28.

Find all possible values of x⁵ + y⁵. → 244

Solution: s=4, S₃=28. S₃ = s³−3ps → 28=64−12p → p=3. Recurrence: S₂=10, S₃=28, S₄=4·28−3·10=82, S₅=4·82−3·28=244.

---

## Problem 8 ✅ (AIME-style synthesis)

Suppose r and s are the roots of t² − 5t + 2 = 0. Compute

r⁴ + s⁴ + (r² + s²)rs. → 475

Solution: s=5, p=2. r²+s² = 25−4=21. r⁴+s⁴ = (r²+s²)²−2(rs)² = 441−8=433. (r²+s²)rs = 21·2=42. Sum = 433+42=475.

---

## Problem 9 ✅ (AMC 12-style)

Let a and b be the roots of x² − 6x + 2 = 0. Find a³ + b³ + a²b + ab². → 192

Solution: s=6, p=2. a³+b³ = s³−3ps = 216−36=180. a²b+ab² = sp=12. Sum=192.

---

## Problem 10 ✅ (AIME-style — Vieta + recurrence)

Let p and q be the roots of x² − 4x + 1 = 0. Find p⁷ + q⁷. → 10084

Solution: s=4, p=1. Recurrence: S₂=14, S₃=52, S₄=194, S₅=724, S₆=2702, S₇=4·2702−1·724=10084.

---

Note: These are real AIME problems (#1–6) plus AIME-style synthesis problems (#7–10). Work through them and I'll verify your answers.
