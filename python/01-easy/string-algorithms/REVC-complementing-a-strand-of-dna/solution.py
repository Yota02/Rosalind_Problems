"""
ID: REVC
TITLE: Complementing a Strand of DNA
URL: https://rosalind.info/problems/revc/
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

    trans = str.maketrans({"A": "T", "T": "A", "C": "G", "G": "C"})
    completion = dna.translate(trans)

    completion = completion[::-1]

    return completion


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read()
    result = solve(data)
    print(result)
    with open("output.txt", "w") as f:
        f.write(result + "\n")
