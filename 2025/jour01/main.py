import sys
from pathlib import Path


def part1(data: str):
    lines = data.splitlines()
    zeros = 0
    dial = 50
    for line in lines:
        sense = line[0]
        value = int(line[1:])
        if sense == "L":
            dial -= value
        elif sense == "R":
            dial += value
        dial %= 100
        if dial == 0:
            zeros += 1
    return zeros


def part2(data: str):
    lines = data.splitlines()
    zeros = 0
    dial = 50
    for line in lines:
        sense = line[0]
        value = int(line[1:])
        zeros += value // 100
        value %= 100
        if sense == "L":
            if 0 < dial <= value:
                zeros += 1
            dial = (dial - value) % 100

        elif sense == "R":
            dial += value
            if dial >= 100:
                zeros += 1
            dial %= 100

    return zeros


if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else "input"
    data = (Path(__file__).parent / f"{name}.txt").read_text()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
