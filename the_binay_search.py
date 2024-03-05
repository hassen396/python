#sorted dataset
dataSet=[1,2,3,4,6,8,9,12,23,45,54,78]

#the value we are looking for
target=int(input('enter a number to be searched :'))

#showing which number they actuallu  looking for
print('the number you enterd is ', target)

#a fuction which take the dataset and the target number and returns either
#  the index of a number is the number exists or returns the number doesn't 
# exist message
def binary_search(dataSet, target):
    start=0
    end=len(dataSet)-1
    while start <= end:
        mid=int((start+end)/2)
        guess=dataSet[mid]
        if guess == target:
            return mid
        elif guess > target:
            end = mid - 1
        else:
            start = mid+1
    return (target, 'is not exist in the dataset o')
    #calling the function we created earlier
print(binary_search(dataSet, target))