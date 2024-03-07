# a methode to sum even numbers from a given list
def sum_even_numbers(list_of_nums):
    print("The dataset is : ", list_of_nums)
    sum_of_evens = 0
    for i in range(len(list_of_nums)):
        if list_of_nums[i] % 2 == 0:
            sum_of_evens = sum_of_evens + list_of_nums[i]

    return sum_of_evens
# this part of the code is writen after it's been committed
# check if the sum is divisible by 3 or not


summ = sum_even_numbers([1, 2, 3, 4, 5, 6, 7, 8])
if summ % 3 == 0:
    print(True)
else:
    print(False)
