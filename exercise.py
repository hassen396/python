base = {1,2,3,4,5,6,7,8,9,10}
square_of_base = { i ** 2 for i in base }
print(square_of_base)
dictionary1= {1:'one', 2:'two'}
dictionary2= {b:a for a,b in dictionary1.items()}
print(dictionary2.items())
my_greet='''hello 
this is me 
and this is my 
greeting" '''
print(my_greet)
list1= ['one','two','three']
merged_string = ", ".join(list1)
print(merged_string)
list2 = merged_string.split(", ")
print(list2, list2)
list3= list1+list2
print(list3)