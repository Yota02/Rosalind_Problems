"""
ID: HAMM
TITLE: Counting Point Mutations
URL: https://rosalind.info/problems/hamm/
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
    
    original = lines[0]
    mutated = lines[1]

    mutations = sum(1 for a, b in zip(original, mutated) if a != b)

    return str(mutations)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read()
    result = solve(data)
    print(result)
    with open("output.txt", "w") as f:
        f.write(result + "\n")
