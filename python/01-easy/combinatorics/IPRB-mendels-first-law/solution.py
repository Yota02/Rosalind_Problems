"""
ID: IPRB
TITLE: Mendel's First Law
URL: https://rosalind.info/problems/iprb/
"""


def solve(data: str) -> str:
    """
    Solve the problem.

    Args:
        data: Raw input string from Rosalind

    Returns:
        Formatted result string
    """
    k, m, n = map(int, data.strip().split())
    total = k + m + n

    p_rec = (n * (n - 1) + m * n + m * (m - 1) * 0.25) / (total * (total - 1))
    p_dom = 1 - p_rec

    return f"{p_dom:.5f}"


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read()
    result = solve(data)
    print(result)
    with open("output.txt", "w") as f:
        f.write(result + "\n")
