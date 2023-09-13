calc_input = input()


def main(query_for_calc):
    calc_input_lst = calc_input.split()
    operation = calc_input[1]
    number_1 = calc_input[0]
    number_2 = calc_input[2]
    if operation == "+":
        res = addition(number_1, number_2)
    if operation == "-":
        # res = subtraction(number_1, number_2)
        pass
    if operation == "*":
        # res = multiplication(number_1, number_2)
        pass
    if operation == "/":
        # res = division(number_1, number_2)
        pass
    return res

