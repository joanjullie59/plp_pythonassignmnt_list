#create an empty list
#append elements to the list
#insert 15 at the second position (index 1)
#extend the list with [50,60,70]
#remove the last element
#sort the list in ascending order
#find and print the index of value 30
from operator import indexOf

my_list=[]

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

my_list.insert(1,15)

my_list.extend([50,60,70])

my_list.pop()

my_list.sort()

index_of_30=my_list.index(30)
print("Index of 30:",index_of_30)
