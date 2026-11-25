import sys
from pathlib import Path


def part1(data: str):
    ranges = data.split(",")
    total_invalid = 0
    for range in ranges :
        range = range.split("-")
        first_number = int(range[0])
        last_number = int(range[1])
        total_invalid += test_invalid(first_number, last_number)

    return total_invalid


def test_invalid(first_number, last_number):
    total_invalid_range = 0
    for i in range (first_number, last_number+1):
        lenght = len(str(i))
        if lenght %2 == 0:
            if i // (10 ** (lenght//2)) == i % (10 ** (lenght//2)) : 
                total_invalid_range += i
    return total_invalid_range


def part2(data: str):
    ranges = data.split(",")
    total_invalid = 0
    for range in ranges :
        range = range.split("-")
        first_number = int(range[0])
        last_number = int(range[1])
        total_invalid += test_invalid_2(first_number, last_number)

    return total_invalid

def test_invalid_2(first_number, last_number):
    total_invalid_range = 0
    for i in range (first_number, last_number+1):
        for j in range(1,len(str(i))//2+1):
            if len(str(i))%j==0:
                if str(i)[:j]*(len(str(i))//j) == str(i):
                    total_invalid_range+=i
                    break
    return total_invalid_range

if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else "input"
    data = (Path(__file__).parent / f"{name}.txt").read_text()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
