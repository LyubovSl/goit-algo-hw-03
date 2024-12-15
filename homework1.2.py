from random import randint
def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or quantity < 1 or quantity > (max - min + 1):
        return "Введіть число від 1 до 1000"
    else:
        result_array = set()
        while len(result_array) != quantity:
            result_array.add(randint(min, max))
        numbers = sorted(list(result_array))
        return numbers
lottery_numbers = get_numbers_ticket(1,1036, 5)
print("Ваші лотерейні числа:", lottery_numbers)