"""
ID: PERM
TITLE: Enumerating Gene Orders
URL: https://rosalind.info/problems/perm/
"""


import math
from itertools import permutations


def solve(data: str) -> str:
    n = int(data.strip())
    nums = list(range(1, n + 1))
    perms = list(permutations(nums))
    result = [str(math.factorial(n))]
    result.extend(" ".join(map(str, p)) for p in perms)
    return "\n".join(result)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read()
    result = solve(data)
    print(result)
    with open("output.txt", "w") as f:
        f.write(result + "\n")
