from utils import test

example_ranges = '''\
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,\
1698522-1698528,446443-446449,38593856-38593862,565653-565659,\
824824821-824824827,2121212118-2121212124\
'''

def solve_part1(ranges: list[str]) -> int:
    duplicate_total = 0
    for r in ranges:
        low, high = map(int, r.split('-'))
        for num in range(low, high + 1):
            strnum = str(num)
            if len(strnum) % 2 != 0:
                continue
            if strnum[:len(strnum) // 2] == strnum[len(strnum) // 2:]:
                duplicate_total += num
    return duplicate_total

def is_duplicate(num: int) -> bool:
    if num < 10:
        return False
    strnum = str(num)
    if len(set(strnum)) == 1:
        return True
    strlen = len(strnum)
    middle = strlen // 2
    for i in range(middle, 0, -1):
        if strlen % i != 0:
            continue
        part = strnum[:i]
        if part * (strlen // i) == strnum:
            return True
    return False

def solve_part2(ranges: list[str]) -> int:
    duplicate_total = 0
    for r in ranges:
        low, high = map(int, r.split('-'))
        for num in range(low, high + 1):
            if is_duplicate(num):
                print(f'invalid: {num}')
                duplicate_total += num
    return duplicate_total

def main():
    test(solve_part1(example_ranges.split(',')), 1227775554)
    print(solve_part1(open('input.txt', 'r').readline().split(',')))
    assert not is_duplicate(12)
    assert is_duplicate(12341234)
    assert is_duplicate(123123123)
    assert is_duplicate(1212121212)
    assert is_duplicate(1111111)
    test(solve_part2(example_ranges.split(',')), 4174379265)
    print(solve_part2(open('input.txt', 'r').readline().split(',')))

if __name__ == "__main__":
    main()
