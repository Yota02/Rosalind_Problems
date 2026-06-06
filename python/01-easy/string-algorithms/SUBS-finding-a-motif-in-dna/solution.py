"""
ID: SUBS
TITLE: Finding a Motif in DNA
URL: https://rosalind.info/problems/subs/
"""


def solve(data: str) -> str:
    """
    Solve the problem.

    Args:
        data: Raw input string from Rosalind

    Returns:
        Formatted result string
    """
    s, t = data.strip().splitlines()
    positions = []
    for i in range(len(s) - len(t) + 1):
        if s[i:i + len(t)] == t:
            positions.append(str(i + 1))
    return " ".join(positions)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read()
    result = solve(data)
    print(result)
    with open("output.txt", "w") as f:
        f.write(result + "\n")
