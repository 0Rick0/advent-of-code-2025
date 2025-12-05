from utils import test

example_input = '''\
3-5
10-14
16-20
12-18

1
5
8
11
17
32
'''


def parse_input(data: str) -> tuple[list[range], list[int]]:
    i = iter(data.splitlines())
    ranges: list[range] = []
    items: list[int] = []
    for line in i:
        if not line:
            break
        a, b = map(int, line.split('-'))
        ranges.append(range(a, b + 1))
    for line in i:
        if not line:
            continue
        items.append(int(line))
    return ranges, items


def solve_part1(data: str) -> int:
    ranges, items = parse_input(data)
    available = 0
    for item in items:
        for r in ranges:
            if item in r:
                available += 1
                break
    return available


def range_intersect(range_a: range, range_b: range) -> bool:
    assert range_a.step == 1 and range_b.step == 1
    return range_a.start in range_b or range_b.start in range_a


def range_join(range_a: range, range_b: range) -> range:
    assert range_a.step == 1 and range_b.step == 1
    assert range_a.start <= range_b.start
    return range(range_a.start, max(range_a.stop, range_b.stop))


def solve_part2(data: str) -> int:
    ranges, _ = parse_input(data)
    # make sure all ranges are sorted from their start index for ease
    ranges = sorted(ranges, key=lambda r: r.start)
    idx = 0
    while idx < len(ranges) - 1:
        # loop over every range object in the list
        range_a = ranges[idx]
        range_b = ranges[idx + 1]
        if range_intersect(range_a, range_b):
            # if two ranges intersect, join them into a single range
            ranges[idx] = range_join(range_a, range_b)
            del ranges[idx + 1]
            # NOTE: we do not advance the index in this case
        else:
            # if the ranges do not intersect, move to the next two ranges
            idx += 1
    return sum(map(len, ranges))


def main():
    test(solve_part1(example_input), 3)
    print(solve_part1(open('input.txt').read()))
    test(solve_part2(example_input), 14)
    print(solve_part2(open('input.txt').read()))


if __name__ == "__main__":
    main()
