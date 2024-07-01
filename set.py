#an unordered, mutable collection of unique elements that can be of any immutable data types.

#creating a set
my_set = {1,2,3,4,5}
print(my_set) #{1, 2, 3, 4, 5}


#adding a single element 
my_set.add(6)
print(my_set) #{1, 2, 3, 4, 5, 6}

#adding multiple elements
my_set.update([7,8,9])
print(my_set) #{1, 2, 3, 4, 5, 6, 7, 8, 9}


#removing a element
my_set.remove(5)
print(my_set) #{1, 2, 3, 4, 6, 7, 8, 9}


#clearing a set
my_set.clear()
print(my_set) #set()
