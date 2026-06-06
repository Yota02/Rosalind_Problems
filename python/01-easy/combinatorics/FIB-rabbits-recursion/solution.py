"""
ID: FIB
TITLE: Rabbits and Recurrence Relations
URL: https://rosalind.info/problems/fib/
"""


def solve(n: int, k: int) -> int:
    a, b = 1, 1
    for _ in range(n - 2):
        a, b = b, b + a * k
    return b


if __name__ == "__main__":
    n, k = map(int, open("input.txt").read().strip().split())
    result = solve(n, k)
    print(result)
    open("output.txt", "w").write(str(result) + "\n")
