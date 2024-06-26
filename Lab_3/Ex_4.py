def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1): #проверка делители от 2 до целой части квадратного корня 
        if num % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers = filter_prime(numbers_list)
print("Prime Numbers:", prime_numbers)