# # Creating a list
# fruits = ['banana','apple', 'cherry']
# # Adding an item
# fruits.append('orange')
# # Accessing an item
# print(fruits[1])  # Output: banana
# print(fruits)

# fruits.append('grape')
# print(fruits)

# fruits.remove('apple')
# print('After removing apple, the list is:')
# print(fruits)

# fruits.pop()
# print('After popping last item, the list is:')
# print(fruits)

# fruits.sort()
# print('After sorting, the list is:')
# print(fruits)



# # Creating a tuple
# coordinates = (10.0, 20.0)
# # Accessing an item
# print(coordinates[0])  # Output: 10.0
# # Tuples are immutable, so the following would raise an error:
# # coordinates[0] = 15.0
# coordinates.append(30.0)  # This will raise an AttributeError
# print(coordinates)

# coordinates[1] = 25.0  # This will raise a TypeError
# print(coordinates)
# print('Tuple remains unchanged:')
# print(coordinates)



# # Creating a set
# unique_numbers = {1, 2, 3, 2, 1}
# print(unique_numbers)  # Output: {1, 2, 3}
# # Adding an item
# unique_numbers.add(4)
# # Checking membership
# print(2 in unique_numbers)

# if (5 not in unique_numbers):
#     unique_numbers.add(5)

# Creating a dictionary
person = {'name': 'Alice', 'age': 30, 'city': 'New York'}
# Accessing a value by key
print(person['name'])  # Output: Alice
# Adding a new key-value pair
person['email'] = 'alice@example.com'

print(person.keys())
print(person.values())
