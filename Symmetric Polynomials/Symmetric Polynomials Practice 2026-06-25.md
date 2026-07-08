# Symmetric Polynomials — Practice Problems

Let s = x + y, p = xy.

# Recurrence Relation (made by Max)

s_2=s^2-2p
s_n=s*s_n-1-p*s_n-2

## Level 1: Basic Rewriting

Express in terms of s and p.

1. ✅ x² + y² = s² − 2p
    Solution: x² + y² = (x+y)² − 2xy = s² − 2p

2. ✅ x³ + y³ = s³ − 3ps
    Solution: x³ + y³ = (x+y)(x² − xy + y²) = s(s² − 2p − p) = s³ − 3ps

3. ✅ x⁴ + y⁴ = s⁴ − 4ps² + 2p²
    Solution: x⁴ + y⁴ = (x² + y²)² − 2x²y² = (s² − 2p)² − 2p²

4. ✅ x⁵ + y⁵ = s⁵ − 5ps³ + 5p²s
    Solution: x⁵ + y⁵ = s·S₄ − p·S₃ = s(s²−2p)² − 2p²s − p(s³−3ps) = s⁵ − 5ps³ + 5p²s

5. ✅ x²y + xy² = sp
    Solution: x²y + xy² = xy(x+y) = sp

6. ✅ x³y + xy³ = p(s² − 2p)
    Solution: x³y + xy³ = xy(x² + y²) = p(s² − 2p)

7. ✅ x³y² + x²y³ = p²s
    Solution: x³y² + x²y³ = x²y²(x+y) = p²s

8. ✅ (x − y)² = s² − 4p
    Solution: (x−y)² = x² − 2xy + y² = (s² − 2p) − 2p = s² − 4p

---

## Level 2: Substitution & Evaluation

Given x + y = 5, xy = 6, find:

9. ✅ x² + y² = 13
    Solution: s² − 2p = 25 − 12 = 13

10. ✅ x³ + y³ = 35
    Solution: s³ − 3ps = 125 − 90 = 35

11. ✅ x⁴ + y⁴ = 97
    Solution: (s²−2p)² − 2p² = 13² − 72 = 169 − 72 = 97

12. ✅ x⁵ + y⁵ = 275
    Solution: s⁵ − 5ps³ + 5p²s = 3125 − 3750 + 900 = 275

13. ✅ 1/x + 1/y = 5/6
    Solution: (x+y)/(xy) = s/p = 5/6

14. ✅ 1/x² + 1/y² = 13/36
    Solution: (x²+y²)/(x²y²) = 13/36

15. ✅ x²y + xy² = 30
    Solution: sp = 5·6 = 30

16. ✅ (x − y)² = 1
    Solution: s² − 4p = 25 − 24 = 1

---

## Level 3: System Solving

Solve for real x, y:

17. ✅ x + y = 4, x² + y² = 10 → (1, 3) or (3, 1)
    Solution: S₂ = s² − 2p → 10 = 16 − 2p → p = 3. Quadratic t² − 4t + 3 = 0 → (t−1)(t−3) = 0.

18. ✅ x + y = 3, x³ + y³ = 18 → ((3+√5)/2, (3−√5)/2) or swapped
    Solution: S₃ = s³ − 3ps → 18 = 27 − 9p → p = 1. Quadratic t² − 3t + 1 = 0 → t = (3 ± √5)/2.

19. ✅ x + y = 2, x⁴ + y⁴ = 34 → (1+√2, 1−√2) or swapped
    Solution: S₄ = (s²−2p)² − 2p² = (4−2p)² − 2p² = 34 → p² − 8p − 9 = 0 → p = −1 (p=9 gives no real solutions). Quadratic t² − 2t − 1 = 0 → t = 1 ± √2.

20. ✅ x + y = 1, x³ + y³ = 19 → (3, −2) or (−2, 3)
    Solution: S₃ = s³ − 3ps → 19 = 1 − 3p → p = −6. Quadratic t² − t − 6 = 0 → (t−3)(t+2) = 0.

---

## Level 4: AIME-Style

21. ✅ Let x and y be real numbers such that x + y = 3 and x² + y² = 7. Find x⁵ + y⁵. → 123
    Solution: S₂ = s² − 2p → 7 = 9 − 2p → p = 1. Recurrence: S₃ = 3·7 − 1·3 = 18, S₄ = 3·18 − 1·7 = 47, S₅ = 3·47 − 1·18 = 123.

22. ✅ Suppose x + y = 2 and x³ + y³ = 14. Find x² + y². → 6
    Solution: S₃ = s³ − 3ps → 14 = 8 − 6p → p = −1. S₂ = s² − 2p = 4 − 2(−1) = 6.

23. ✅ If x + y = 5 and x² + y² = 13, find the value of x²y + xy². → 30
    Solution: S₂ = s² − 2p → 13 = 25 − 2p → p = 6. x²y + xy² = sp = 5·6 = 30.

24. ✅ Let r and s be the roots of x² − 7x + 10 = 0. Compute r³ + s³ without solving for r and s. → 133
    Solution: s = 7, p = 10. r³ + s³ = s³ − 3ps = 343 − 210 = 133.

25. ✅ Suppose x + y = a and xy = b. Express x⁴ + y⁴ in terms of a and b. Then find x⁴ + y⁴ when a = 2 and b = −1. → a⁴ − 4a²b + 2b²; 34
    Solution: x⁴ + y⁴ = (s²−2p)² − 2p² = (a²−2b)² − 2b² = a⁴ − 4a²b + 2b². For a=2, b=−1: 16 + 16 + 2 = 34.

---

## Level 5: Challenge

26. ✅ Find all pairs (x, y) of real numbers satisfying:
    x + y = 6, x⁴ + y⁴ = 272 → (2,4) or (4,2)
    Solution: S₄ = (36−2p)² − 2p² = 272 → p² − 72p + 512 = 0 → (p−8)(p−64)=0. p=64 gives no real solutions. p=8: t²−6t+8=0 → (2,4) or (4,2).

27. ✅ If x + y = 1 and x² + y² = 2, find x⁷ + y⁷. → 71/8
    Solution: S₂ = s²−2p → 2 = 1−2p → p = −1/2. Recurrence: S₃=5/2, S₄=7/2, S₅=19/4, S₆=13/2, S₇=71/8.

28. ✅ Let x and y be roots of t² − 3t + 1 = 0. Compute x⁵ + y⁵ + 1/(x⁵ y⁵). → 124
    Solution: s=3, p=1. S₅ = 123. 1/(x⁵y⁵) = 1/p⁵ = 1. Sum = 123 + 1 = 124.

29. ✅ For real numbers x, y with x + y = 2, the minimum value of x⁴ + y⁴ is m. Find m. → 2
    Solution: S₄ = 2(p−4)² − 16. Real condition: s²−4p ≥ 0 → p ≤ 1. Minimum at p=1: S₄ = 2(1−4)² − 16 = 2.

30. ✅ Suppose x + y = 4 and xy = 2. Compute x³y² + x²y³. → 16
    Solution: x³y² + x²y³ = x²y²(x+y) = p²s = 4·4 = 16.

---

## Level 6: Extra Challenge

31. ✅ Let x and y be real numbers with x² + y² = 7 and x³ + y³ = 10. Find x + y and xy. → s=1, p=−3
    Solution: S₂ = s²−2p = 7, S₃ = s³−3ps = 10. Substituting p = (s²−7)/2 gives s³−21s+20=0 → (s−1)(s+5)(s−4)=0. s=−5,4 give p with negative discriminant, so only s=1, p=−3 works.

32. ✅ Given x + y = 3 and x⁴ + y⁴ = 17, find x³ + y³. → 9
    Solution: S₄ = (9−2p)² − 2p² = 17 → p²−18p+32=0 → p=2 or 16. p=16 gives no real solutions. p=2: S₃ = 27 − 18 = 9.

33. ✅ If x + y = 5 and xy = 3, compute x⁶ + y⁶. → 6346
    Solution: S₂=19, S₃=80, S₄=343, S₅=1475, S₆=5·1475−3·343=6346.

34. ✅ Let x and y be the roots of t² − 4t + 1 = 0. Find the value of (x² + 1)(y² + 1). → 16
    Solution: s=4, p=1. (x²+1)(y²+1) = x²y² + x² + y² + 1 = p² + S₂ + 1 = 1 + 14 + 1 = 16.

35. ✅ Suppose x + y = 2 and xy = −1. Compute x⁶ + y⁶ + x⁴y² + x²y⁴. → 204
    Solution: Factor as S₆ + p²·S₂. s=2, p=−1. S₂=6, S₆=198. Sum = 198 + 6 = 204.

36. ✅ Let a, b be real numbers such that a + b = 4 and a³ + b³ = 28. Find the quadratic equation whose roots are a and b. → t² − 4t + 3 = 0
    Solution: S₃ = s³ − 3ps → 28 = 64 − 12p → p = 3. Quadratic: t² − 4t + 3 = 0.

37. ✅ If x + y = 6 and x² + y² = 20, find the maximum possible value of xy. → 8
    Solution: S₂ = s² − 2p → 20 = 36 − 2p → p = 8 (uniquely determined).

38. ✅ For nonzero real numbers x, y with x + y = 2 and 1/x + 1/y = 1, find |x − y|. → 2
    Solution: 1/x+1/y = s/p = 2/p = 1 → p = 2. (x−y)² = s²−4p = 4−8 = −4, so |x−y| = 2 (magnitude of 2i).

39. ✅ Given that x + y + z = 0 and x² + y² + z² = 2, find the value of x⁴ + y⁴ + z⁴. → 2
    Solution: (x+y+z)² = x²+y²+z² + 2(xy+yz+zx) → 0 = 2 + 2σ₂ → σ₂ = −1. Then (σ₂)² = x²y²+y²z²+z²x² + 2xyz(x+y+z) → 1 = x²y²+y²z²+z²x². So x⁴+y⁴+z⁴ = (x²+y²+z²)² − 2(1) = 4 − 2 = 2.

40. ✅ For real numbers x, y with x² + xy + y² = 3, find the maximum value of x − y. → 2√3
    Solution: Let u=x+y, v=x−y. Then x²+xy+y² = (3u²+v²)/4 = 3 → 3u²+v²=12. Max v² at u=0 → v²=12 → v=2√3.

---
