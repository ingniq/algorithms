from stack import Stack
import operator


def postfix_eval(postfix_expr):
    postfix_expr = postfix_expr.replace(" ", "")

    if not isinstance(int(postfix_expr[0]), int):
        raise ValueError("The first character must be an integer.")

    if not isinstance(int(postfix_expr[1]), int):
        raise ValueError("The second character must be an integer.")

    s1 = __str_to_stack(postfix_expr)
    s2 = Stack()

    operators = {
        "+": operator.add,
        "*": operator.mul,
        "=": s2.pop
        }

    while s1.size() != 0:
        el = s1.pop()

        if el in operators:
            if "=" == el:
                return operators.get(el)()

            el = operators.get(el)(s2.pop(), s2.pop())
        else:
            try:
                el = int(el)
            except ValueError:
                raise ValueError("Unsupported the type of operator or operand.")

        s2.push(el)


def __str_to_stack(text_str):
    text_stack = Stack()

    last_index = len(text_str) - 1

    while last_index >= 0:
        text_stack.push(text_str[last_index])
        last_index -= 1

    return text_stack
