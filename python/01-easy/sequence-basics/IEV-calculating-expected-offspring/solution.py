"""
ID: IEV
TITLE: Calculating Expected Offspring
URL: https://rosalind.info/problems/iev/
"""


def solve(data: str) -> str:
    """
    Solve the problem.

    Args:
        data: Raw input string from Rosalind

    Returns:
        Formatted result string
    """
    counts = list(map(int, data.strip().split()))
    probs = [1, 1, 1, 0.75, 0.5, 0]
    expected = 2 * sum(c * p for c, p in zip(counts, probs))
    return str(expected)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read()
    result = solve(data)
    print(result)
    with open("output.txt", "w") as f:
        f.write(result + "\n")
