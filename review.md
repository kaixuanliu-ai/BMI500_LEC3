# Code Review — `review_human.py`

## Partner Repo
- Original repo: [HANQI-CHEN/BMI500_LEC3](https://github.com/HANQI-CHEN/BMI500_LEC3)  
- Forked repo: [kaixuanliu-ai/BMI500_LEC3](https://github.com/kaixuanliu-ai/BMI500_LEC3)  
- File reviewed: `review_human.py`  

---

## Human Review

**Findings**
1. Variable `pairs = n // 2` is unused → remove.  
2. Using `(-1)**i` works but is inefficient; toggling a sign variable is clearer.  
3. Returning `0.0` for `n < 0` is permissive; could instead raise `ValueError`.  
4. Add return type annotation `-> float` and clearer docstring.  
5. Minor PEP8/style issues (spacing).  
6. Pairwise summation could improve numerical stability, but unnecessary for homework scale.  

**Decisions**
- Remove unused `pairs`  
- Replace `(-1)**i` with sign toggle  
- Add type annotation and improve docstring  
- Fix formatting (PEP8)  
- Keep `return 0.0` for `n < 0` (simplicity)  
- Skip pairwise optimization (not needed here)  

**Final Code**
```python
import math

def leibniz_sum_2j(n: int) -> float:
    """
    Compute partial sums of the Leibniz formula for π.

    Parameters
    ----------
    n : int
        Number of terms to include (n >= 0)

    Returns
    -------
    float
        Sum of the first n terms of the Leibniz series
    """
    if n < 0:
        return 0.0

    total, sign = 0.0, 1.0
    for i in range(n):
        total += sign / (2 * i + 1.0)
        sign = -sign
    return total


if __name__ == "__main__":
    for n in [1, 5, 10, 50, 100]:
        approx_pi = 4 * leibniz_sum_2j(n)
        error = abs(approx_pi - math.pi)
        print(f"n={n:<5d} approx_pi={approx_pi:.6f} error={error:.6e}")
```

---

## LLM Review

### Prompt (input to LLM)
```
Review this code:

import math

def leibniz_sum_2j (n:int):
    """
    Compute partial sums of the Leibniz formula for π.

    n : Number of terms to include (n >= 0, int)

    Returns: sum of the first n terms of the Leibniz series (float)
    """
    if n < 0:
        return 0.0
    
    total=0.0
    pairs = n // 2

    #For code review: I change the code to the simpler version
    for i in range(n):
        total += ((-1)**i) / (2*i + 1.0)

    return total
```

---

### LLM Output
```
Review Summary

File: review_human.py
Overall: Implementation is correct and returns the first n terms of the Leibniz series. A few small readability and efficiency improvements are recommended.

Findings & Suggestions
- Unused variable: pairs = n // 2 is defined but never used — remove it.
- Sign computation: ((-1) ** i) works but is less efficient and slightly less clear than toggling a sign variable.
- Negative n handling: Returning 0.0 for n < 0 is permissive; consider raising ValueError to surface bad input (or at least document this behavior).
- Annotations & docstring: Add -> float return annotation and make the docstring precise about n semantics.
- Performance (optional): For large n consider pairwise summation (1/(4p+1) - 1/(4p+3)) or Kahan summation to reduce floating-point error and improve convergence behaviour.
- Style: Minor spacing and PEP8 formatting improvements would help readability.

Minimal patch (recommended):

def leibniz_sum_2j(n: int) -> float:
    """
    Compute partial sums of the Leibniz formula for π.

    n : Number of terms to include (n >= 0, int)

    Returns: sum of the first n terms of the Leibniz series (float)
    """
    if n < 0:
        return 0.0

    total = 0.0
    sign = 1.0
    for i in range(n):
        total += sign / (2 * i + 1.0)
        sign = -sign

    return total

Alternative (with pairwise summation):

def leibniz_sum_2j(n: int) -> float:
    if n < 0:
        raise ValueError("n must be non-negative")


    total = 0.0
    pairs = n // 2
    for p in range(pairs):
        total += 1.0/(4*p + 1.0) - 1.0/(4*p + 3.0)
    if n % 2 == 1:
        total += 1.0/(2*n - 1)
    return total
```
 
