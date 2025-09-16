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



if __name__ == "__main__":
    Ns = [1, 5, 10, 50, 100]
    for n in Ns:
        approx_pi = 4 * leibniz_sum_2j(n)
        error = abs(approx_pi - math.pi)
        print(f"n={n:<5d} approx_pi={approx_pi:.6f} error={error:.6e}")
