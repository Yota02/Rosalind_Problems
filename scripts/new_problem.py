"""
new_problem.py — Create a new Rosalind problem directory from template.

Usage:
    python scripts/new_problem.py <PROBLEM_ID>

Example:
    python scripts/new_problem.py HAMM
    python scripts/new_problem.py SUBS
"""

import os
import sys
import textwrap

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOLUTIONS_DIR = os.path.join(REPO_ROOT, "python")

# Import problem database from update_stats
sys.path.insert(0, os.path.join(REPO_ROOT, "scripts"))
from update_stats import PROBLEMS

DIFFICULTY_MAP = {
    "easy": "01-easy",
    "medium": "02-medium",
    "hard": "03-hard",
}


def slugify(title: str) -> str:
    """Convert title to kebab-case for directory name."""
    return title.lower().replace(" ", "-").replace(",", "").replace("'", "")


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/new_problem.py <PROBLEM_ID>")
        print("Example: python scripts/new_problem.py HAMM")
        sys.exit(1)

    pid = sys.argv[1].upper()

    # Find the problem in the database
    matches = [p for p in PROBLEMS if p[0] == pid]
    if not matches:
        print(f"❌ Problem '{pid}' not found in database.")
        print("\nAvailable IDs:")
        grouped = {}
        for p in PROBLEMS:
            grouped.setdefault(p[3], []).append(p[0])
        for theme, ids in grouped.items():
            print(f"  {theme}: {', '.join(ids)}")
        sys.exit(1)

    prob_id, title, difficulty, thematic = matches[0]
    diff_dir = DIFFICULTY_MAP[difficulty]
    dir_name = f"{prob_id}-{slugify(title)}"
    target = os.path.join(SOLUTIONS_DIR, diff_dir, thematic, dir_name)
    sol_path = os.path.join(target, "solution.py")

    if os.path.exists(sol_path):
        print(f"⚠️  Solution already exists at: {sol_path}")
        sys.exit(0)

    os.makedirs(target, exist_ok=True)

    # Generate solution.py
    url = f"https://rosalind.info/problems/{prob_id.lower()}/"
    code = textwrap.dedent(f'''\
    """
    ID: {prob_id}
    TITLE: {title}
    URL: {url}
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
        # TODO: implement solution
        return str(lines)


    if __name__ == "__main__":
        with open("input.txt") as f:
            data = f.read()
        result = solve(data)
        print(result)
        with open("output.txt", "w") as f:
            f.write(result + "\\n")
    ''')

    with open(sol_path, "w") as f:
        f.write(code)

    # Create empty data files
    open(os.path.join(target, "input.txt"), "w").close()
    open(os.path.join(target, "output.txt"), "w").close()

    rel_path = os.path.relpath(target, REPO_ROOT)
    print(f"✅ Created {prob_id} — {title}")
    print(f"   📁 {rel_path}/")
    print(f"   📄 {rel_path}/solution.py")
    print(f"   📄 {rel_path}/input.txt")
    print(f"   📄 {rel_path}/output.txt")
    print(f"\nNext steps:")
    print(f"   1. Paste the Rosalind dataset into {rel_path}/input.txt")
    print(f"   2. Implement solve() in {rel_path}/solution.py")
    print(f"   3. Run:  python {rel_path}/solution.py")
    print(f"   4. Verify output.txt matches Rosalind expected result")
    print(f"   5. Commit: git add -A && git commit -m \"Add {prob_id} solution\"")


if __name__ == "__main__":
    main()
