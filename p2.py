#Numbers, This is the version python 2
x = 3 / 2
print(x)
y = 3.0 / 2
print(y)
Friends = ['Hem', 'Thir', 'Bishnu']
First_friend=Friends[0]
print(First_friend)

Market = ['Aldi','Lidl','Costco']
First_item = Market[0]
print(First_item)
Last_item = Market[-1]
print(Last_item)

Market = ['Aldi','Lidl','Costco']
print(Market[0].title())

Result = " My favorite market is" + " "+ Market[0] + "."
print(Result)

for shop in Market:
    print(shop)

Market = ['Aldi','Lidl','Costco']
print(Market)
Market[0]= 'Food_Lion'
print(Market)

#Append to add element
Market = ['Aldi','Lidl','Costco']
Market.append('Fod_Lion')
print(Market)
#Insert item in the desired position
Market = ['Aldi','Lidl','Costco']
Market.insert(0,'Fod_Lion')
print(Market)

#Delete an item from the List
Market = ['Aldi','Lidl','Costco']
del Market[0]
print(Market)

#Removing an item using pop method.
Market = ['Aldi','Lidl','Costco']
popped_Market = Market.pop()
print(Market)
print(popped_Market)
#Removing any item from the list using popped command.
Market = ['Aldi','Lidl','Costco']
Shop = Market.pop(1)
print(Shop)

Market = ['Aldi','Lidl','Costco']
Market.remove('Lidl')
print(Market)
