def sum(list_ofnumbers):
    sum = 0
    for number in list_ofnumbers:
        sum = sum + number
    return sum

list_of_numbers=[1,2,3,4,5,6,7,8,9]
sum_list = sum(list_of_numbers)
print(sum_list)