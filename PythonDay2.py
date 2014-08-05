class Burger():
	def_init_(self, filling, doneness, size, toppings, container):
		self.filling = filling
		self.doneness = doneness
		self.size = size
		if self.toppings_allowed(toppings):
			self.toppings=toppings
		else:
			self.toppings=[]
		self.toppings = self.toppings_allowed
		self.container = container
	
	def _str_(self):
		return "I'm a %s %s burger topped with %s" % (self.doneness,self.filling, toppings)
	
	def tastiness(self):
		if "cheese" in toppings:
			return "VERY GOOD"
		elif self.doneness=="raw":
			return "yuck!"
	
	def toppings_allowed(self, attempted_toppings):
		allowed_toppings = ["cheese, "tomato", "onion", "lettuce", "bacon"]
		toppings=[]
		for topping in attempted_toppings:
			if topping in allowed_toppings:
				toppings.append(topping)
			return toppings
	
	def cook(self):
		time_for_size=0
		if self.doneness=="raw":
			time_for_doneness=0
		elif self.doneness=="rare"
			time_for_doneness = 5
		elif self.doneness=="medium"
			time_for_doneness = 6
		elif self.doneness=="well done"
			time_for_doneness = 8
		else:
			return "UNKNOWN"
			
		return self.size * 4 * time_for_doneness

rare_burger = Burger("beef", "medium", "0.33", ["cheese"], "bread")

class VeggieBurger(Burger):
	def_int_(self, toppings_ordered, container)
	Burger._init_(self, "veggie patty", "medium", 0.35, toppings_ordered, container)
	
	def toppings_allowed(self, attempted_toppings):
		allowed_toppings = ["cheese, "tomato", "onion", "lettuce"]
		toppings=[]
		for toppings in attempted_toppings:
			if topping in allowed_toppings:
				toppings.append(topping)
			return toppings
	def cooking_time(self):
		return 6

veggie_burger=VeggieBurger(["tomato", "bacon"], "bread")
print veggie_burger.cooking_time()
print veggie_burger.tastiness()
print veggie_burger

def first(x):
	x[0]
	
