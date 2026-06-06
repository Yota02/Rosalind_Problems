"""
ID: DNA
TITLE: Counting DNA Nucleotides
URL: https://rosalind.info/problems/dna/
"""


def solve(data: str) -> str:
    """
    Solve the problem.

    Args:
        data: Raw input string from Rosalind

    Returns:
        Formatted result string
    """
    s = data.strip()
    return f"{s.count('A')} {s.count('C')} {s.count('G')} {s.count('T')}"


if __name__ == "__main__":
    import os
    basedir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(basedir, "input.txt")) as f:
        data = f.read()
    result = solve(data)
    print(result)
    with open(os.path.join(basedir, "output.txt"), "w") as f:
        f.write(result + "\n")