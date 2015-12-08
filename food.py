class Food(object):
	def __init__(self, recipe, color, ingredients_list):
		self.recipe = recipe
		self.color = color
		self.ingredients_list = ingredients_list
	def print_recipe(self):
		print self.recipe
		print self.color
		print self.ingredients_list
	def add_ingredient(self, additional_ing):
		self.ingredients_list.append(additional_ing)


# Food - Required Method: print_recipe()

pb_apple = Food("Cut apples.\nPlace apples and some peanut butter on platter with a knife.", "red", ["peanut butter", "apple", "butter"])
pb_apple.print_recipe()

pb_apple.add_ingredient("chocolate")
pb_apple.print_recipe()


# Food - Second Method:

