user_ticket = input("Введите номер проездного билета (6 цифр): ")
limit_numbers = 6

if len(user_ticket) != limit_numbers or not user_ticket.isdigit():
    print("Введите ШЕСТИЗНАЧНОЕ число")

digits = [int(digit) for digit in user_ticket]

first_three_numbers = digits[:3]
second_three_numbers = digits[3:]

sum_first_three_numbers = sum(first_three_numbers)
sum_second_three_numbers = sum(second_three_numbers)

if sum_first_three_numbers == sum_second_three_numbers:
    print("Этот билет счастливый!")
else:
    print("Этот билет несчастливый.")
