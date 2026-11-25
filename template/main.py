import sys
from pathlib import Path


def part1(data: str):
    lines = data.splitlines()
    return None


def part2(data: str):
    lines = data.splitlines()
    return None


if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else "input"
    data = (Path(__file__).parent / f"{name}.txt").read_text()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
