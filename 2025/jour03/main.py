import sys
from pathlib import Path


def part1(data: str):
    lines = data.splitlines()
    total_jolt = 0
    for line in lines :
        p1 = 0
        p2 = len(line)-1
        v1 = int(line[p1])
        v2 = int(line[p2])
        for i in range (len(line)-1):
            if int(line[i]) > v1:
                v1 = int(line[i])
                p1 = i
        for j in range (p1+1,len(line)):
            if int(line[j]) > v2:
                v2 = int(line[j])
                p2 = j
        
        total_jolt += int(line[p1]+line[p2])

    return total_jolt


def part2(data: str):
    lines = data.splitlines()
    total = 0
    for line in lines :
        total_jolt = ""

        p1 = 0
        p2 = len(line)-1
        pm = -1
        v1 = int(line[p1])
        v2 = int(line[p2])
        res = ""
        for i in range(11,-1,-1):
            pm, vm = biggest(line, pm + 1, i)
        
            total_jolt += str(vm)
        total += int(total_jolt)
    return total

def biggest(nb, px ,remaining):
    p1 = px
    v1 = int(nb[p1])
    for i in range (px, len(nb)-remaining):
        if int(nb[i]) > v1:
            v1 = int(nb[i])
            p1 = i

    return p1, v1


if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else "input"
    data = (Path(__file__).parent / f"{name}.txt").read_text()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
