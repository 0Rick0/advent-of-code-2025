from utils import test

TEST_INPUT_1 = '''\
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
'''.splitlines()

def calculate_next_position(move: str, current: int) -> tuple[int, int]:
    direction = move[0]
    amount = int(move[1:])
    delta = -amount if direction == 'L' else amount
    next_position = current + delta
    zero_passes = 0
    if current == 0:
        zero_passes -= 1
    if next_position == 0:
        zero_passes += 1
    while next_position < 0:
        zero_passes += 1
        next_position = 99 + next_position + 1
        # print(f'current position={current}, move={move}, next_position={next_position}')
    while next_position > 99:
        zero_passes += 1
        next_position = next_position - 99 - 1
        print(f'current position={current}, move={move}, next_position={next_position}')
    if current == 0 and next_position == 0:
        zero_passes += 1
    return next_position, max(zero_passes, 0)


def solve_part1(inp: list[str]) -> int:
    position = 50
    count_zero = 0
    for move in inp:
        position, _ = calculate_next_position(move, position)
        if position == 0:
            count_zero += 1
        # print(f'move={move}, position={position}')
    return count_zero

def solve_part2(inp: list[str]) -> int:
    position = 50
    count_zero = 0
    for move in inp:
        position, zero_passes = calculate_next_position(move, position)
        count_zero += zero_passes
        print(f'move={move}, position={position}, count_zero={zero_passes}')
    return count_zero


def main():
    # test(solve_part1(TEST_INPUT_1), 3)
    # print(solve_part1(open('input.txt', 'r').read().splitlines()))
    test(solve_part2(TEST_INPUT_1), 6)
    test(solve_part2(['L50', 'R200']), 3)
    test(solve_part2(['R50', 'L50']), 1)
    print(solve_part2(open('input.txt', 'r').read().splitlines()))


if __name__ == "__main__":
    main()
