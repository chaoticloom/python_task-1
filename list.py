#A list is an ordered, mutable collection of items.

#creating a list
numbers = [ 1,2,3,4,5]
print(numbers) #[1, 2, 3, 4, 5]  

#adding into a list
numbers.append(10)
print(numbers) #[1, 2, 3, 4, 5, 10] 

#removing from a list
numbers.remove(1)
print(numbers) #[2, 3, 4, 5, 10]

#modifying a list 
numbers[1] = 7
print(numbers)  #[2, 7, 4, 5, 10]
  
