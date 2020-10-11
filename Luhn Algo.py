def luhn_algo(card_number):
    num_digits = len(card_number)
    n_sum = 0
    second_digit = False

    for i in range(num_digits - 1, -1, -1):
        d = int(card_number[i])

        if second_digit = True:
            d = d * 2

        n_sum += d // 10
        n_sum += d % 10

        second_digit = not second_digit

    if n_sum % 10 == 0:
        print("This is a valid card")
    else:
        print("This is an invalid card")


card_num = input("Enter credit card number: ")
luhn_algo(card_num)
