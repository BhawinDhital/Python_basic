#If statement in python
friends = ['hem','bishnu','jiwan','thir']
for friend in friends:
    if friend =='bishnu':
        print(friend.upper())
    else:
        print(friend.title())

for friend in friends:
    if friend =='bishnu':
        print(friend.upper())
    else:
        print(friend.title())

friends = ['hem','bishnu','jiwan','thir']
for friend in friends:
    if friend =='bishnu':
        print("true")
    else:
        print("false")
friend = 'hem'
friend == 'Hem'
print(friend)

car = 'Audi'
car.lower() == 'audi'
print(car)

car = 'Audi'
if car !='honda':
    print("ride an Audi!")

answer = 40
if answer !=42:
    print("try again!")

friends = ['hem','bishnu','jiwan','thir']
'hem' in friends

banned_cars = ['honda','volvo','solvo','olvo']
car = 'honda'
if car not in banned_cars:
    print(car.title() +",  you can ride if you wish.")

car = 'toyota'
print("Is car == 'toyota'? I predict True.")
print(car=='toyota')
print("Is car == 'audi'? I predict False.")
print(car=='audi')

age = 20
if age >=18:
    print("you are old enough to vote!")
    print("Have you registered to vote yet?")
#if-else
age = 17
if age >=18:
    print("you are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("sorry, you are too young to vote.")
    print("you can register as soon as you are 18.")

age = 70
if age < 4:
    ticket_prize = 0
elif age < 18:
    ticket_prize = 10
elif age < 30 :
    ticket_prize = 20
else:
    ticket_prize = 50
print('ticket_prize:',ticket_prize)

age = 2
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >65:
    price = 5
print("your cost is $" + str(price) +".")

requested_toppings = ['mushrooms','cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'cheese' in requested_toppings:
    print("Adding cheese.")
print("Finishing making your pizza!")
#if-else
requested_toppings = ['mushrooms','cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif 'cheese' in requested_toppings:
    print("Adding cheese.")
print("Finishing making your pizza!")

#if statement with list.
requested_toppings = ['mushrooms','green peppers','cheese']
for requested_topping in requested_toppings:
    print("Adding" + requested_topping+ ".")
print("\nFinished making your pizza Hem Ji")

#requested_toppings = ['mushrooms','green peppers','cheese']
#for requested_topping in requested_toppings:
#    if requested_topping == 'green peppers':
#        print("sorry! we are out of green peppers right now.")
#    else:
#        print("Adding" + requested_topping + ".")
#print("\nFinished making your pizza!")

requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding" + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("you have only one option of plain pizza")

#Multiple lists
available_cars = ['toyota','honda','nissan','hundai']
requested_cars = ['toyota','volvo','subaru']
for requested_car in requested_cars:
    if requested_car in available_cars:
        print("Ride" + " " + requested_car +".")
    else:
        print("Sorry!, we do not have" + " " + requested_car + ".")
print("\nStart riding your car!")
