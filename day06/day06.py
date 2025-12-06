import functools

from utils import test

OPERATORS = {
    '+': int.__add__,
    # '-': int.__sub__,
    '*': int.__mul__,
    # '/': int.__truediv__,
}

example_input = '''\
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
'''


def parse_input(inp: str) -> list[list[str]]:
    values = [line.split() for line in inp.splitlines() if line]
    return list(map(list, zip(*values)))


def solve_one(inp: list[list[str]]) -> int:
    op = inp[-1]
    values = list(map(int, inp[:-1]))
    out = functools.reduce(OPERATORS[op], values)
    return out


def solve_one2(inp: list[str]) -> int:
    op = ''.join(l[-1] for l in inp).strip()
    values = [int(''.join(l[:-1]).strip()) for l in inp]
    # values = list(map(int, inp[:-1]))
    out = functools.reduce(OPERATORS[op], values)
    return out


def solve_part1(inp: str) -> int:
    values = parse_input(inp)
    return sum(map(solve_one, values))


def parse_input2(inp: str) -> list[list[list[str]]]:
    lines = [line for line in inp.splitlines() if line]
    groups = []
    current_group = []
    for i in range(len(lines[0])):
        current_digits = [line[i] for line in lines]
        if all(digit == ' ' for digit in current_digits):
            groups.append(current_group)
            current_group = []
        else:
            current_group.append(current_digits)
    groups.append(current_group)
    return groups


def solve_part2(inp: str) -> int:
    values = parse_input2(inp)
    return sum(map(solve_one2, values))


def main():
    test(solve_one(['123', '45', '6', '*']), 33210)
    test(solve_part1(example_input), 4277556)
    print(solve_part1(open('input.txt').read()))
    test(solve_part2(example_input), 3263827)
    print(solve_part2(open('input.txt').read()))


if __name__ == '__main__':
    main()
