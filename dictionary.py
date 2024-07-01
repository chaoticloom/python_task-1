#an unordered, mutable  collection of key-value pairs.

#creating a dictionary
my_dict = { 'name' : 'kashif', 'age' : 20, 'city' : 'new_delhi' }

print(my_dict) #{'name': 'kashif', 'age': 20, 'city': 'new_delhi'}


# Accessing values
print(my_dict['city']) #new_delhi


#updating a existing value
my_dict['age'] = 21
print(my_dict['age']) #21


#adding a new key-value pair
my_dict['email'] = 'name@example.com'

print(my_dict) #{'name': 'kashif', 'age': 20, 'city': 'new_delhi', 'email': 'name@example.com'}


#removing  a key-value pair
del my_dict['email']

print(my_dict) #{'name': 'kashif', 'age': 21, 'city': 'new_delhi'}


      
