#Working with lists
magicians=['alice', 'david', 'carolina']
for magician in magicians:
  print(magician)

magicians=['alice', 'david', 'carolina']
for magician in magicians:
  print(magician.title() + ", that was a great trick!")

cars=['bmw', 'audi', 'benz', 'tata']
for car in cars:
    print(car.title()+",these are awesome cars!")

magicians=['alice', 'david', 'carolina']
for magician in magicians:
  print(magician.title() + ", that was a great trick!")  
  print("i can't wait for your next trick, " + magician.title()+".\n")
  
print("Thankyou, everone. That was a great magic show") 

#forgetting to indent
signs=['hi', 'hello', 'bye', 'nothing']
for sign in signs:
 print(signs)

#indent additional lines
laptops = ['dell', 'asus', 'lenovo', 'hp']
for laptop in laptops:
    print(laptop.title()+",that was a great laptop")
print("i can't wait to see more best laptops of," + laptop.title()+".\n") 

names = ['ram', 'sham', 'rahul', 'dell']
for name in names:
    print(name.title()+"," +"your name is awesome!")
    print("i love to hear more names of these kind,"+name.title()+".\n")

    print("All these names are awesome!")


#making numericals lists
for value in range(1,10):
    print(value)

numbers = list(range(1,6))
print(numbers)   

squares =[]
for value in range(1,11):
    squares.append(value**2)

print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
min(digits)
max(digits)
sum(digits)

squares = [value**2 for value in range (1,11)]
print(squares)    

numbers = []
for numbers in range(1,21):
    print (numbers)

numbers = list(range(1,1000))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

squares = [value**3 for value in range(3,30)]
print(squares)

#slicing a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:4])

letters = ['a', 'b','c','d','e']
print(letters[1:3])

letters = ['a', 's', 'f', 'h', 'x']
print(letters[2:])

players = ['a', 'v', 'g', 'g', 'r', 'f']
print("Here are the names in my team:")
for player in players[:3]:
    print(player.title())

#copying list
my_foods = ['pizza', 'cake', 'burger']
friend_foods = my_foods[:]

my_foods.append('chappti')
friend_foods.append('ice cream')

print("my favorite food are:")
print(my_foods)

print("\n my friends favourite food:")
print(friend_foods)

fruits = ['banana', 'apple', 'orange','grapes','lemon']
print ("the first three items in the list are:")
print(fruits[1:4])

print("the three items fromt he middle are:")
print(fruits[1:4])

print("the three last items are:")
print(fruits[2:])

my_pizza = ['pizza1', 'pizza2', 'pizza3', 'pizza4']
print(my_pizza)
friend_pizza = my_pizza[:]
print(friend_pizza)

print("my favourite pizza:")
print(my_pizza[2:3])

print("my friends pizza")
print(friend_pizza[0:3])

my_pizza.append("pizza5")
print(my_pizza)

friend_pizza.append("pizza10")
print(friend_pizza)

