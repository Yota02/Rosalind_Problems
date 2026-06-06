"""
update_stats.py — Scan solutions directory and regenerate README stats.

Usage:
    python scripts/update_stats.py

Run automatically via .githooks/pre-commit.
"""

import os
import re
import shutil

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOLUTIONS_DIR = os.path.join(REPO_ROOT, "python")
README_PATH = os.path.join(REPO_ROOT, "README.md")

DIFFICULTY_DIRS = ["01-easy", "02-medium", "03-hard"]

# ── Complete problem database ──────────────────────────────────────────────

PROBLEMS = [
    # (id, title, difficulty, thematic)
    # -- Easy / String Algorithms --
    ("DNA", "Counting DNA Nucleotides", "easy", "string-algorithms"),
    ("RNA", "Transcribing DNA into RNA", "easy", "string-algorithms"),
    ("REVC", "Complementing a Strand of DNA", "easy", "string-algorithms"),
    ("HAMM", "Counting Point Mutations", "easy", "string-algorithms"),
    ("SUBS", "Finding a Motif in DNA", "easy", "string-algorithms"),
    ("REVP", "Locating Restriction Sites", "easy", "string-algorithms"),
    ("LEXF", "Enumerating k-mers Lexicographically", "easy", "string-algorithms"),
    ("LEXV", "Ordering Strings of Varying Length Lexicographically", "medium", "string-algorithms"),
    ("KMER", "k-Mer Composition", "medium", "string-algorithms"),
    ("KMP", "Speeding Up Motif Finding", "medium", "string-algorithms"),
    ("TRIE", "Introduction to Pattern Matching", "medium", "string-algorithms"),
    ("SUFF", "Encoding Suffix Trees", "hard", "string-algorithms"),
    ("LREP", "Finding the Longest Multiple Repeat", "hard", "string-algorithms"),
    ("MREP", "Identifying Maximal Repeats", "hard", "string-algorithms"),
    # -- Easy / Combinatorics --
    ("FIB", "Rabbits and Recurrence Relations", "easy", "combinatorics"),
    ("IPRB", "Mendel's First Law", "easy", "combinatorics"),
    ("PROB", "Introduction to Random Strings", "medium", "combinatorics"),
    ("SIGN", "Enumerating Oriented Gene Orderings", "medium", "combinatorics"),
    ("PPER", "Partial Permutations", "medium", "combinatorics"),
    ("PMCH", "Perfect Matchings and RNA Secondary Structures", "medium", "combinatorics"),
    ("LIA", "Independent Alleles", "medium", "combinatorics"),
    ("MRNA", "Inferring mRNA from Protein", "easy", "combinatorics"),
    ("RSTR", "Matching Random Motifs", "medium", "combinatorics"),
    ("EVAL", "Expected Number of Restriction Sites", "medium", "combinatorics"),
    ("INDC", "Independent Segregation of Chromosomes", "medium", "combinatorics"),
    # -- Easy / Sequence Basics --
    ("GC", "Computing GC Content", "easy", "sequence-basics"),
    ("IEV", "Calculating Expected Offspring", "easy", "sequence-basics"),
    ("PROT", "Translating RNA into Protein", "easy", "sequence-basics"),
    ("PRTM", "Calculating Protein Mass", "easy", "sequence-basics"),
    ("SPLC", "RNA Splicing", "easy", "sequence-basics"),
    ("ORF", "Open Reading Frames", "easy", "sequence-basics"),
    ("SSEQ", "Finding a Spliced Motif", "medium", "sequence-basics"),
    ("TRAN", "Transitions and Transversions", "medium", "sequence-basics"),
    # -- Easy / Set Theory --
    ("SETO", "Introduction to Set Operations", "medium", "set-theory"),
    ("SSET", "Counting Subsets", "medium", "set-theory"),
    ("PDST", "Creating a Distance Matrix", "medium", "set-theory"),
    ("INOD", "Counting Phylogenetic Ancestors", "medium", "set-theory"),
    # -- Medium / String Search --
    ("LCSM", "Finding a Shared Motif", "easy", "string-search"),
    ("CORR", "Error Correction in Reads", "medium", "string-search"),
    ("ITWV", "Finding Disjoint Motifs in a Gene", "medium", "string-search"),
    ("KSIM", "Finding All Similar Motifs", "hard", "string-search"),
    # -- Medium / Dynamic Programming --
    ("LGIS", "Longest Increasing Subsequence", "medium", "dynamic-programming"),
    ("LCSQ", "Finding a Shared Spliced Motif", "medium", "dynamic-programming"),
    ("SCSP", "Interleaving Two Motifs", "medium", "dynamic-programming"),
    ("EDIT", "Edit Distance", "medium", "dynamic-programming"),
    ("EDTA", "Edit Distance Alignment", "medium", "dynamic-programming"),
    ("CTEA", "Counting Optimal Alignments", "medium", "dynamic-programming"),
    ("MOTZ", "Motzkin Numbers and RNA Secondary Structures", "medium", "dynamic-programming"),
    ("CAT", "Catalan Numbers and RNA Secondary Structures", "medium", "dynamic-programming"),
    ("MMCH", "Maximum Matchings and RNA Secondary Structures", "medium", "dynamic-programming"),
    ("RNAS", "Wobble Bonding and RNA Secondary Structures", "medium", "dynamic-programming"),
    # -- Medium / Graph Theory --
    ("GRPH", "Overlap Graphs", "easy", "graph-theory"),
    ("TREE", "Completing a Tree", "medium", "graph-theory"),
    ("DBRU", "Constructing a De Bruijn Graph", "medium", "graph-theory"),
    ("NWCK", "Distances in Trees", "medium", "graph-theory"),
    ("NKEW", "Newick Format with Edge Weights", "medium", "graph-theory"),
    ("QRT", "Quartets", "hard", "graph-theory"),
    ("QRTD", "Quartet Distance", "hard", "graph-theory"),
    ("CNTQ", "Counting Quartets", "hard", "graph-theory"),
    # -- Medium / Sequence Alignment --
    ("CONS", "Consensus and Profile", "easy", "sequence-alignment"),
    ("GLOB", "Global Alignment with Scoring Matrix", "medium", "sequence-alignment"),
    ("LOCA", "Local Alignment with Scoring Matrix", "medium", "sequence-alignment"),
    ("GCON", "Global Alignment with Constant Gap Penalty", "medium", "sequence-alignment"),
    ("GAFF", "Global Alignment with Affine Gap Penalty", "medium", "sequence-alignment"),
    ("OAP", "Overlap Alignment", "hard", "sequence-alignment"),
    ("SMGB", "Semiglobal Alignment", "hard", "sequence-alignment"),
    ("SIMS", "Finding a Motif with Modifications", "hard", "sequence-alignment"),
    ("LAFF", "Local Alignment with Affine Gap Penalty", "hard", "sequence-alignment"),
    ("MULT", "Multiple Alignment", "hard", "sequence-alignment"),
    ("MGAP", "Maximizing Gap Symbols of an Optimal Alignment", "hard", "sequence-alignment"),
    ("OSYM", "Isolating Symbols in Alignments", "hard", "sequence-alignment"),
    ("RSUB", "Identifying Reversing Substitutions", "hard", "sequence-alignment"),
    # -- Medium / Genome Assembly --
    ("LONG", "Genome Assembly as Shortest Superstring", "medium", "genome-assembly"),
    ("PCOV", "Genome Assembly with Perfect Coverage", "medium", "genome-assembly"),
    ("GASM", "Genome Assembly Using Reads", "hard", "genome-assembly"),
    ("GREP", "Genome Assembly with Perfect Coverage and Repeats", "hard", "genome-assembly"),
    ("ASMQ", "Assessing Assembly Quality with N50 and N75", "hard", "genome-assembly"),
    ("LING", "Linguistic Complexity of a Genome", "hard", "genome-assembly"),
    ("PDPL", "Creating a Restriction Map", "hard", "genome-assembly"),
    # -- Medium / Proteomics --
    ("MPRT", "Finding a Protein Motif", "medium", "proteomics"),
    ("SPEC", "Inferring Protein from Spectrum", "medium", "proteomics"),
    ("CONV", "Comparing Spectra with the Spectral Convolution", "medium", "proteomics"),
    ("FULL", "Inferring Peptide from Full Spectrum", "medium", "proteomics"),
    ("PRSM", "Matching a Spectrum to a Protein", "hard", "proteomics"),
    ("SGRA", "Using the Spectrum Graph to Infer Peptides", "medium", "proteomics"),
    # -- Medium / Population Genetics --
    ("AFRQ", "Counting Disease Carriers", "medium", "population-genetics"),
    ("WFMD", "The Wright-Fisher Model of Genetic Drift", "medium", "population-genetics"),
    ("FOUN", "The Founder Effect and Genetic Drift", "medium", "population-genetics"),
    ("EBIN", "Wright-Fisher's Expected Behavior", "medium", "population-genetics"),
    ("SEXL", "Sex-Linked Inheritance", "medium", "population-genetics"),
    # -- Hard / Phylogeny --
    ("CTBL", "Creating a Character Table", "medium", "phylogeny"),
    ("CSTR", "Creating a Character Table from Genetic Strings", "medium", "phylogeny"),
    ("CHBP", "Character-Based Phylogeny", "hard", "phylogeny"),
    ("EUBT", "Enumerating Unrooted Binary Trees", "hard", "phylogeny"),
    ("ROOT", "Counting Rooted Binary Trees", "hard", "phylogeny"),
    ("CUNR", "Counting Unrooted Binary Trees", "medium", "phylogeny"),
    ("SPTD", "Phylogeny Comparison with Split Distance", "hard", "phylogeny"),
    ("ALPH", "Alignment-Based Phylogeny", "hard", "phylogeny"),
    # -- Hard / Advanced Topics --
    ("MEND", "Inferring Genotype from a Pedigree", "hard", "advanced-topics"),
    ("CSET", "Fixing an Inconsistent Character Set", "hard", "advanced-topics"),
    ("SORT", "Sorting by Reversals", "medium", "advanced-topics"),
    ("REAR", "Reversal Distance", "medium", "advanced-topics"),
    ("FIBD", "Mortal Fibonacci Rabbits", "easy", "advanced-topics"),
]

THEMATIC_ORDER = [
    ("string-algorithms", "🧬 String Algorithms"),
    ("combinatorics", "📊 Combinatorics & Probability"),
    ("sequence-basics", "🧪 Sequence Basics"),
    ("set-theory", "🔢 Set Theory"),
    ("string-search", "🔍 String Search"),
    ("dynamic-programming", "📈 Dynamic Programming"),
    ("graph-theory", "🕸️ Graph Theory"),
    ("sequence-alignment", "🧩 Sequence Alignment"),
    ("genome-assembly", "🧬 Genome Assembly"),
    ("proteomics", "⚗️ Proteomics & Spectrometry"),
    ("population-genetics", "🧫 Population Genetics"),
    ("phylogeny", "🌳 Phylogeny"),
    ("advanced-topics", "⚙️ Advanced Topics"),
]


def scan_solved() -> set[str]:
    """Scan the python/ directory for solved problems."""
    solved = set()
    for diff_dir in DIFFICULTY_DIRS:
        diff_path = os.path.join(SOLUTIONS_DIR, diff_dir)
        if not os.path.isdir(diff_path):
            continue
        for theme_dir in os.listdir(diff_path):
            theme_path = os.path.join(diff_path, theme_dir)
            if not os.path.isdir(theme_path):
                continue
            for prob_dir in os.listdir(theme_path):
                sol_path = os.path.join(theme_path, prob_dir, "solution.py")
                if os.path.isfile(sol_path):
                    # Extract ID from the docstring
                    with open(sol_path) as f:
                        content = f.read()
                    m = re.search(r'^ID:\s*(\S+)', content, re.MULTILINE)
                    if m:
                        solved.add(m.group(1))
                    else:
                        # Fallback: use directory name prefix before first '-'
                        pid = prob_dir.split("-")[0]
                        solved.add(pid)
    return solved


def progress_bar(fraction: float, width: int = 30) -> str:
    filled = int(fraction * width)
    empty = width - filled
    return "█" * filled + "░" * empty


def build_readme(solved: set[str]) -> str:
    total = len(PROBLEMS)
    solved_count = sum(1 for p in PROBLEMS if p[0] in solved)
    pct = solved_count / total * 100 if total else 0
    bar = progress_bar(solved_count / total)

    lines = []
    lines.append("# 🧬 Rosalind — Bioinformatics Progress\n")
    lines.append(
        f'<div align="center">\n'
        f'  <img src="https://img.shields.io/badge/Progress-{solved_count}%2F{total}-00BFFF" alt="Progress"/>\n'
        f'  <img src="https://img.shields.io/badge/Python-3.12+-blue" alt="Python"/>\n'
        f'  <img src="https://img.shields.io/badge/License-MIT-green" alt="License"/>\n'
        f'</div>\n'
    )
    lines.append(f"\n## 📈 Progression\n")
    lines.append(f"**{solved_count} / {total}** problèmes résolus ({pct:.1f}%)\n")
    lines.append(f"```\n{bar} {pct:.1f}%\n```\n")

    # Stats by difficulty
    for diff_label, diff_key in [("🟢 Facile", "easy"), ("🟡 Moyen", "medium"), ("🔴 Difficile", "hard")]:
        sub = [p for p in PROBLEMS if p[2] == diff_key]
        sub_solved = sum(1 for p in sub if p[0] in solved)
        sub_total = len(sub)
        sub_pct = sub_solved / sub_total * 100 if sub_total else 0
        sub_bar = progress_bar(sub_solved / sub_total)
        lines.append(f"**{diff_label}** : {sub_solved}/{sub_total} ({sub_pct:.1f}%)")
        lines.append(f"```\n{sub_bar} {sub_pct:.1f}%\n```\n")

    # Table by thematic
    lines.append("## 📋 Problèmes\n")
    lines.append("| ID | Titre | Statut | Difficulté | Thématique | Lien |")
    lines.append("|---|---|---|---|---|---|")

    for theme_slug, theme_label in THEMATIC_ORDER:
        theme_problems = [p for p in PROBLEMS if p[3] == theme_slug]
        if not theme_problems:
            continue

        lines.append(f"| **{theme_label}** | | | | | |")
        labels = {"easy": "🟢 Facile", "medium": "🟡 Moyen", "hard": "🔴 Difficile"}

        for pid, title, diff, theme in theme_problems:
            status = "✅" if pid in solved else "⬜"
            diff_label = labels.get(diff, diff)
            sol_path = _solution_path(pid)
            link = f"[Voir]({sol_path})" if sol_path else "—"
            lines.append(f"| **{pid}** | {title} | {status} | {diff_label} | {theme_label} | {link} |")

        lines.append("")

    lines.append("---\n")
    lines.append(
        "_Généré automatiquement par `scripts/update_stats.py` "
        "via pre-commit hook._\n"
    )

    return "\n".join(lines)


def _solution_path(pid: str) -> str | None:
    """Find the solution.py path for a problem ID, relative to repo root."""
    for diff_dir in DIFFICULTY_DIRS:
        diff_path = os.path.join(SOLUTIONS_DIR, diff_dir)
        if not os.path.isdir(diff_path):
            continue
        for theme_dir in os.listdir(diff_path):
            theme_path = os.path.join(diff_path, theme_dir)
            if not os.path.isdir(theme_path):
                continue
            for prob_dir in os.listdir(theme_path):
                if prob_dir.startswith(pid + "-") or prob_dir == pid:
                    rel = os.path.join("python", diff_dir, theme_dir, prob_dir, "solution.py")
                    if os.path.isfile(os.path.join(REPO_ROOT, rel)):
                        return rel
    return None


def main():
    solved = scan_solved()
    readme_content = build_readme(solved)

    with open(README_PATH, "w") as f:
        f.write(readme_content)

    solved_ids = [p[0] for p in PROBLEMS if p[0] in solved]
    total = len(PROBLEMS)
    print(f"[update_stats] README mis à jour : {len(solved_ids)}/{total} problèmes résolus.")


if __name__ == "__main__":
    main()
