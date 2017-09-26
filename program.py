
# These are variables. Variable hold information. The name of the variable is up to you, but it can't have any spaces.
robot_price = 900
robot_count = 2
robot_tax = 1.25
book_price = 100
book_count = 1
book_tax = 1.06

# This a default python funtion called "print". A function is a block of reusable code that is uded to perform a single action. You can also create your own functions - but they will need to be defined, of course.
print(robot_price * robot_count * robot_tax + book_price * book_count * book_tax, "basic print function")

# This a list. Lists group things together. 
product_price = [900,100]
product_counts = [2,1]
product_tax = [1.25, 1.06]

# This function is taking information from a list and therefore the number in the [] represents which item in the list (i.e. it's location). Lists start at 0. So in this example [0] is referencing the first item in each list. 
print(product_price[0] * product_counts[0] * product_tax[0] + product_price[1] * product_counts[1] * product_tax[1], "basic list example")

# This is a dictionary. IT's to use for pairs of things grouped together. Dictionaries defines a variables. Dom är väldigt lika listor, men istället för siffror använder man strängar för att slå upp ett värde.
robot = {"price": 900, "count": 2, "tax": 1.25}
book = {"price": 100, "count": 1, "tax": 1.06}

# These two functions do the same thing. Excepts that in the second function it is usuing the dictionary for both robot and book. 
print(robot["price"] * 2 * 1.25 + 100 * 1.06, "list and dictionay example")
print(robot["price"] * robot["count"] * robot["tax"] + book["price"] * book["count"] * book["tax"], "dictionary example")


#The problem with dictionaries is it's not ideal for when things always have the exact same value. When things always have the same value, its better to use Classes. A class is like a recipe, its more flexible than dicgtionaries.
# These is the Class description for Product. It has 3 statements. 
class Product:
	price = 0
	count = 0
	tax = 1

# Now you need a method. Method is like a function, but it exists ONLY is Classes. En metod är en behållare, inte för data som vi tidigare sett, utan för kod. Ett sätt att samla kod man vill köra flera gånger. Gör att köra koden "anropar" man den. 
# En metod kan vara hur många rader kod som helst (men försök att inte ha dem så långa). Make sure to add a statement under each class description that references how you want the method to behave for that class type (e.g. robot.price_with_tax())
# the self variable represents the instance of the object itself. Most object-oriented languages pass this as a hidden parameter to the methods defined on an object; Python does not. You have to declare it explicitly. When you create an instance of the class and call its methods, it will be passed automatically
# Remember to indent the method so it "belongs" to the class. 
	def price_with_tax(self):
		return self.price * self.count * self.tax

robot = Product()
robot.price = 900
robot.count = 2
robot.tax = 1.25
robot.price_with_tax()


book = Product()
book.price = 100
book.count = 1
book.tax = 1.06
book.price_with_tax()

# This function executes the class together with its method.
print (robot.price_with_tax() + book.price_with_tax(),"method example")

# The __init__ method is roughly what represents a constructor in Python. When you call Class () Python creates an object for you, and passes it as the first parameter to the __init__ method. Any additional parameters (e.g., Class(24, 'Hello')) will also get passed as arguments
# __init__ is the constructor for a class. The self parameter refers to the instance of the object. The __init__ method gets called when memory for the object is allocated.

class Product:
	def __init__(self, price, count, tax):
		self.price = price
		self.count = count
		self.tax = tax

	def price_with_tax(self):
		return self.price * self.count * self.tax

robot = Product(price=900, count=2, tax=1.25)
book = Product(price=100, count=1, tax=1.06)

print (robot.price_with_tax() + book.price_with_tax(), "init example")

# It still can be easier to describe/create an object. Using lists makes it even easier.s

products = [Product(price=900, count=2, tax=1.25), Product(price=100, count=1, tax=1.06)]
total_price = products[0].price_with_tax() + products[1].price_with_tax()

print(total_price, "lists example")

# Instread of remembering to put in the total_price line of code, we can use a Loop instead. 
# Loopar är till för att göra något för varje sak i en lista eller dictionary. Vi har en lista med produkter, vi vill räkna ut priset för varje produkt, det är perfekt användning av en loop.

products = [Product(price=900, count=2, tax=1.25), Product(price=100, count=1, tax=1.06)]
total_price = 0

# Below is the Loop command. It always starts with "for". If we hadn't set total_price=0 s

for product in products:
	total_price = total_price + product.price_with_tax()

print(total_price, "a loop command")

# This is an IF-Statement.

class Product:
	def __init__(self, price, count, tax, name):
		self.price = price
		self.count = count
		self.tax = tax
		self.name = name

	def price_with_tax(self):
		total = self.price * self.count * self.tax
		if total >500:
			return 0.9 * total
		else:
			return total 

robot = Product(price=900, count=2, tax=1.25, name=robot)
book = Product(price=100, count=1, tax=1.06, name=book)

print (robot.price_with_tax() + book.price_with_tax(), "an if statement")
