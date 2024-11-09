#Permutation and Combination program, dont mention number of permutation and combination, values of 'r' ill be (1......n).

import math

def permutation(n, r):
    # Permutation formula: P(n, r) = n! / (n - r)!
    return math.factorial(n) // math.factorial(n - r)

def combination(n, r):
    # Combination formula: C(n, r) = n! / (r! * (n - r)!)
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

# Get user input
n = int(input("Enter value for n: "))

# Calculate permutations and combinations for each r from 1 to n
print(f"Calculations for n = {n}:")
for r in range(1, n + 1):
    perm = permutation(n, r)
    comb = combination(n, r)
    print(f"r = {r} --> Permutation P({n}, {r}) = {perm}, Combination C({n}, {r}) = {comb}")

