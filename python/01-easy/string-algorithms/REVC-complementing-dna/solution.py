"""
ID: REVC
TITLE: Complementing a Strand of DNA
URL: https://rosalind.info/problems/revc/
"""

COMPLEMENT = str.maketrans("ACGT", "TGCA")


def solve(s: str) -> str:
    return s.translate(COMPLEMENT)[::-1]


if __name__ == "__main__":
    s = open("input.txt").read().strip()
    result = solve(s)
    print(result)
    open("output.txt", "w").write(result + "\n")
