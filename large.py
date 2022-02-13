def maximum(list_of_numbers):
    max = 0
    for number in list_of_numbers:
        if max < number:
            max = number
    return max 

numbers=[4,5,22,88,4]
x = maximum(numbers)
print(x)