"""
ID: DNA
TITLE: Counting DNA Nucleotides
URL: https://rosalind.info/problems/dna/
"""


def solve(s: str) -> str:
    return f"{s.count('A')} {s.count('C')} {s.count('G')} {s.count('T')}"


if __name__ == "__main__":
    s = open("input.txt").read().strip()
    result = solve(s)
    print(result)
    open("output.txt", "w").write(result + "\n")
