from copy import deepcopy

from utils import test

example_input = '''\
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.'''


def get_pos(inp: list[list[str]], x: int, y: int) -> str:
    if x < 0 or y < 0:
        return '.'
    try:
        return inp[y][x]
    except IndexError:
        return '.'


def no_empty(inp: list[list[str]], x: int, y: int) -> int:
    empty_slots = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if get_pos(inp, x + dx, y + dy) == '.':
                empty_slots += 1
    return empty_slots


def move_all(inp: list[list[str]]) -> tuple[int, list[list[str]]]:
    accessible = 0
    output = deepcopy(inp)
    for y, line in enumerate(inp):
        for x, val in enumerate(line):
            if val == '.':
                continue
            if val == '@':
                a = no_empty(inp, x, y)
                if a > 4:
                    output[y][x] = '.'
                    accessible += 1
    return accessible, output


def solve_part1(inp: list[list[str]]) -> int:
    accessible, output = move_all(inp)
    return accessible


def solve_part2(inp: list[list[str]]) -> int:
    total_moved = 0
    current = inp
    while True:
        accessible, current = move_all(current)
        total_moved += accessible
        if accessible == 0:
            break
    return total_moved


def parse_input(inp: str) -> list[list[str]]:
    return [list(line) for line in inp.splitlines()]


def main():
    test(get_pos([['@']], -1, -1), '.')
    test(get_pos([['@']], 0, 0), '@')
    test(get_pos([['@']], 1, 1), '.')
    test(solve_part1(parse_input(example_input)), 13)
    print('Part 1:', solve_part1(parse_input(open('input.txt').read())))

    test(solve_part2(parse_input(example_input)), 43)

    print('Part 2:', solve_part2(parse_input(open('input.txt').read())))


if __name__ == '__main__':
    main()
