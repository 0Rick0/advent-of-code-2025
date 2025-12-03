from utils import test

example_input = '''\
987654321111111
811111111111119
234234234234278
818181911112111
'''


def maximize_joltage_2(batteries: list[int]) -> tuple[int, int]:
    highest_value = max(batteries)
    index_highest_value = batteries.index(highest_value)
    if index_highest_value == len(batteries) - 1:
        second_highest_value = max(batteries[:-1])
        index_second_highest_value = batteries.index(second_highest_value)
        return index_second_highest_value, index_highest_value
    next_highest_value = max(batteries[index_highest_value + 1:])
    index_next_highest_value = batteries.index(next_highest_value)
    return index_highest_value, index_next_highest_value


def maximize_joltage_n(batteries: list[int], n: int) -> int:
    # if no batteries left, return 0
    if n == 0:
        return 0
    # Find the highest battery in the current list, ignoring the last n batteries
    highest_battery = max(batteries[:-n+1] if n > 1 else batteries)
    idx = batteries.index(highest_battery)
    # find the recurse with n - 1, taking a subset of batteries from after the current battery
    return highest_battery * (10 ** (n - 1)) + maximize_joltage_n(batteries[idx + 1:], n - 1)


def solve_part1(inp: list[str]) -> int:
    total_joltage = 0
    for line in inp:
        if not line:
            continue
        batteries = list(map(int, line))
        a, b = maximize_joltage_2(batteries)
        # print(f'{line} -> [{a}]{batteries[a]} [{b}]{batteries[b]}')
        total_joltage += batteries[a] * 10 + batteries[b]
    return total_joltage


def solve_part2(inp: list[str]) -> int:
    total_joltage = 0
    for line in inp:
        if not line:
            continue
        batteries = list(map(int, line))
        joltage = maximize_joltage_n(batteries, 12)
        # print(f'{line} -> {joltage}')
        total_joltage += joltage
    return total_joltage


def main():
    test(solve_part1(example_input.splitlines()), 357)
    print(solve_part1(open('input.txt').read().splitlines()))

    test(solve_part2(example_input.splitlines()), 3121910778619)
    print(solve_part2(open('input.txt').read().splitlines()))


if __name__ == '__main__':
    main()
