"""
ID: GC
TITLE: Computing GC Content
URL: https://rosalind.info/problems/gc/
"""


def parse_fasta(data: str) -> dict[str, str]:
    records = {}
    for block in data.strip().split(">"):
        if not block:
            continue
        lines = block.splitlines()
        label = lines[0]
        seq = "".join(lines[1:])
        records[label] = seq
    return records


def gc_content(seq: str) -> float:
    return (seq.count("G") + seq.count("C")) / len(seq) * 100


def solve(data: str) -> str:
    records = parse_fasta(data)
    best_id = max(records, key=lambda k: gc_content(records[k]))
    return f"{best_id}\n{gc_content(records[best_id]):.6f}"


if __name__ == "__main__":
    data = open("input.txt").read()
    result = solve(data)
    print(result)
    open("output.txt", "w").write(result + "\n")
