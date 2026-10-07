def cryptic_sorter(strings: list[str]) -> list[str]:
    result: list[str] = strings
    length: int = len(result)

    i = 0
    while i < length:
        j = 0
        while j < length - 1 - i:
            left: str = result[j]
            right: str = result[j + 1]

            swap: bool = False

            if len(left) > len(right):
                swap = True

            elif len(left) == len(right):
                if left.lower() > right.lower():
                    swap = True

            if swap:
                result[j+1], result[j] = result[j+1], result[j]
            j += 1
        i += 1

    return result


if __name__ == "__main__":
    tests = [
        (
            ["apple", "cat", "banana", "dog", "elephant"],
            ["cat", "dog", "apple", "banana", "elephant"],
        ),
        (
            ["aaa", "bbb", "AAA", "BBB"],
            ["aaa", "AAA", "bbb", "BBB"],
        ),
        (
            ["hello", "world", "hi", "test"],
            ["hi", "test", "hello", "world"],
        ),
        (
            [],
            [],
        ),
        (
            [""],
            [""],
        ),
        (
            ["b", "A", "a", "B"],
            ["A", "a", "b", "B"],
        ),
        (
            ["ccc", "aaa", "bbb"],
            ["aaa", "bbb", "ccc"],
        ),
        (
            ["abcd", "a", "abc", "ab"],
            ["a", "ab", "abc", "abcd"],
        ),
    ]

    for values, expected in tests:
        result = cryptic_sorter(values)

        print("Input:   ", values)
        print("Result:  ", result)
        print("Expected:", expected)
        print("OK:", result == expected)
        print()
