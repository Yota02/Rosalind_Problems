"""
ID: RNA
TITLE: Transcribing DNA into RNA
URL: https://rosalind.info/problems/rna/
"""


def solve(s: str) -> str:
    return s.replace("T", "U")


if __name__ == "__main__":
    s = open("input.txt").read().strip()
    result = solve(s)
    print(result)
    open("output.txt", "w").write(result + "\n")
