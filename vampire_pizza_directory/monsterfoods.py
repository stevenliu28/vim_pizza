#create the superclass
class Monster(object):
	#set up class attribute, the same fpr all instances
	eats="food"
	#define the __init__ method
	def __init__(self,name):
		#set up instance attribute, diffirient for each instance
		self.name=name
		#define method for speaking behavior
	def speak(self):
		print(self.name+ "speaks")
		# define a method for eating behavior
	def eat(self,meal):
		if meal==self.eat:
			print("yum")
		else:
			print("blech")
			# create an instance of monsterfood
#my_monster=Monster("spooky snack")
# call the methods on the instants
#my_monster.speak()
#my_monster.eat("food")

# create a subclass of monster
class frankenburger(Monster)



