from stack import Stack


def brackets_are_balanced(str_value):
    str_len = len(str_value)

    if str_len % 2 != 0:
        return False

    if str_value[0] != "(":
        return False

    if str_value[str_len - 1] != ")":
        return False

    stack = Stack()

    while str_len > 0:
        str_len -= 1

        if str_value[str_len] == "(":
            stack.pop()

            if stack.size() == 0:
                if str_len != 0 and str_value[str_len - 1] == "(":
                    return False
        else:
            stack.push(str_value[str_len])

    return stack.size() == 0
