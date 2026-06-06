"""
ID: TEMPLATE
TITLE: Problem Title
URL: https://rosalind.info/problems/TEMPLATE/
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
        f.write(result + "\n")
