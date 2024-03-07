# a methode to sum even numbers from a given list
def sum_even_numbers(list_of_nums):
    print(list_of_nums)
    sum_of_evens = 0
    for i in range(len(list_of_nums)):
        if list_of_nums[i] % 2 == 0:
            sum_of_evens = sum_of_evens + list_of_nums[i]

    return sum_of_evens
