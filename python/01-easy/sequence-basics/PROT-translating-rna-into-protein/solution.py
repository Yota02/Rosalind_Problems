"""
ID: PROT
TITLE: Translating RNA into Protein
URL: https://rosalind.info/problems/prot/
"""


CODON_TABLE = {
    "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
    "UAU": "Y", "UAC": "Y", "UAA": "*", "UAG": "*",
    "UGU": "C", "UGC": "C", "UGA": "*", "UGG": "W",
    "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
    "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G",
}

STOP_CODONS = {"UAA", "UAG", "UGA"}


def solve(data: str) -> str:
    rna = data.strip()
    protein = []
    for i in range(0, len(rna), 3):
        codon = rna[i:i+3]
        if codon in STOP_CODONS:
            break
        if codon in CODON_TABLE:
            protein.append(CODON_TABLE[codon])
    return "".join(protein)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read()
    result = solve(data)
    print(result)
    with open("output.txt", "w") as f:
        f.write(result + "\n")
