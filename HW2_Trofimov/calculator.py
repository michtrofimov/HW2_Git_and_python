calc_input = input()


def main(query_for_calc):
    calc_input_lst = query_for_calc.split()

    operation = calc_input_lst[1]
    number_1 = calc_input_lst[0]
    number_1 = float(number_1)
    number_2 = calc_input_lst[2]
    number_2 = float(number_2)

    if operation == "+":
        # res = addition(number_1, number_2)
        pass
    elif operation == "-":
        # res = subtraction(number_1, number_2)
        pass
    elif operation == "*":
        res = multiplication(number_1, number_2)
    elif operation == "/":
        # res = division(number_1, number_2)
        pass
    return res


main(calc_input)

def multiplication(number_1, number_2):
    res = number_1 * number_2
    return res
