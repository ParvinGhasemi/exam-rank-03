def bracket_validator(string: str) -> bool:
    brackets: dict[str, str] = {
        ")": "(",
        "]": "[",
        "}": "{",
    }

    stack: str = ""
    for char in string:
        if char in brackets.values():
            stack += char
        if char in brackets.keys():
            if stack == "":
                return False
            if stack[-1] != brackets[char]:
                return False
            stack = stack[:-1]

    return stack == ""


if __name__ == "__main__":
    tests = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("hello(world)", True),
        ("((())", False),
        ("", True),
        (")", False),
        ("((()))", True),
    ]

    for text, expected in tests:
        result = bracket_validator(text)
        print("'"+text+"'", "->  ", result, " |  expected:", expected)
        print()
