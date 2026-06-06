"""
ID: RNA
TITLE: Transcribing DNA into RNA
URL: https://rosalind.info/problems/rna/
"""


def solve(data: str) -> str:
    """
    Solve the problem.

    Args:
        data: Raw input string from Rosalind

    Returns:
        Formatted result string
    """
    lines = data.strip().splitlines()
    dna = lines[0]

    rna = dna.replace("T", "U")

    return rna


if __name__ == "__main__":
    import os
    basedir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(basedir, "input.txt")) as f:
        data = f.read()
    result = solve(data)
    print(result)
    with open(os.path.join(basedir, "output.txt"), "w") as f:
        f.write(result + "\n")
