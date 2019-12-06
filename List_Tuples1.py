#Sorting a List permanently with the sort() method.
cars = ['honda','toyota','nissan','bmw']
cars.sort()
print(cars)
#reversing the order by sort(reverse=True)

cars = ['honda','toyota','nissan','bmw']
cars.sort(reverse=True)
print(cars)

#Sorting a list temporarily with the soreted() function
cars = ['honda','toyota','nissan','bmw']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

#Printing a list in reverse order.
cars = ['honda','toyota','nissan','bmw']
print(cars)
cars.reverse()
print(cars)

cars = ['honda','toyota','nissan','bmw']
len(cars)
print(len(cars))

# looping through an entire List
friends = ['hem','bishnu','thir']
for friend in friends:
    print(friend)

friends = ['hem','bishnu','thir']
for friend in friends:
    print(friend.title() + ", is a good friend")

friends = ['hem','bishnu','thir']
for friend in friends:
    print(friend.title() + ", you are great!")
    print("I respect you very much," +friend.title() + ".\n")
#Making a numerical list.
squares = []
for x in range(1,11):
    squares.append(x**2)
    print(squares)

for value in range(1,5):
    print(value)

numbers =list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)
#Listcomprehensions
squares = [x**2 for x in range(1,11)]
print(squares)

#Slicing a List
friends = ['hem','bishnu','thir','jiwan']
first_two = friends[:2]
print(first_two)

#copying a List
copy_of_friends = friends[:]
print(copy_of_friends)

digits = [1,2,3,4,5,6,7]
min(digits)
print(min(digits))
max(digits)
print(max(digits))
sum(digits)
print(sum(digits))


friends = ['hem','bishnu','shankar','tika','jiwan']
print(friends[0:3])
print(friends[1:4])
print("Here are some friends:")
for friend in friends[:3]:
    print(friend.title())

#From here Tuples start: Great!
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])
# Looping
dimensions = (200,50)
for dimension in dimensions:
    print(dimension)
# writing a tuple:
dimensions = (200,50)
print("original dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions = (400,100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
