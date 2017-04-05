class Animal():
	noise = "Grunt"
	size = "Large"
	color = "brown"
	hair = "Covers body"
	def get_color(self):
		return self.color
	def make_noise(self):
		return self.noise


dog = Animal()
dog.make_noise()
dog.size = "small"
dog.color = "black"
dog.hair = "hairless"


class Dog(Animal):
	name = 'john'
#	color = "brown"
#	def get_color(self):
#		print(self.name)
#		return self.color



obj = Dog()
obj == self

................................................

class Animal():
	name = 'Amy'
	noise = "Grunt"
	size = "Large"
	color = "Brown"
	hair = "Covers body"
	def get_color(self, abc):
		return self.color       #TypeError: get_color() missing 1 required positional argument: 'abc'
	def get_noise(self):
		return self.noise


dog = Animal()
dog.get_color()
dog.get_noise()


#arg = Positional Argument
#kwarg = Keyword arument
def some_func(arg_1, arg_2, arg_3, kwarg_1=None):
	pass

def some_func(arg_1, arg_2, kwarg_1=None, kwarg_2=None):
	print(arg_1,arg_2)
	if kwarg_1 != None:
		print(kwarg_1)

some_func("Good", "Bad", kwarg_1="I am good")

email_address = "another@gmail.com"
to_list = "abc@gmail.com"
from_list = ["another2@gmail.com", "hello@teamrkm.com"]
def send_email(email, to_list=to_list, from_ist=from_list):
	pass

send_email("hello@rkmteam.com", to_list=['ac@gmail.com'], from_list=["abc@gmail.com"])
  

 class Animal():
	name = 'Amy'
	noise = "Grunt"
	size = "Large"
	color = "Brown"
	hair = "Covers body"
	def get_color(self, abc):
		return self.color + " " +abc
		@property    
	def get_noise(self):
		return self.noise


dog = Animal()
dog.get_color("red") #o/p = 'brown red'