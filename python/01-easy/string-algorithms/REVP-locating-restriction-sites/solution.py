"""
ID: REVP
TITLE: Locating Restriction Sites
URL: https://rosalind.info/problems/revp/
"""


COMPLEMENT = str.maketrans("ATCG", "TAGC")


def reverse_complement(s: str) -> str:
    return s.translate(COMPLEMENT)[::-1]


def solve(data: str) -> str:
    lines = data.strip().splitlines()
    _, *seq_lines = lines
    dna = "".join(seq_lines)
    results = []
    for length in range(4, 13):
        for start in range(len(dna) - length + 1):
            sub = dna[start : start + length]
            if sub == reverse_complement(sub):
                results.append(f"{start + 1} {length}")
    return "\n".join(results)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read()
    result = solve(data)
    print(result)
    with open("output.txt", "w") as f:
        f.write(result + "\n")
