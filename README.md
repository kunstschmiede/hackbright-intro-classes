# Classes Exercise
*Complete these in files in this repo called `food.py`, `animals.py` and `plants.py`, respectively.*

For each of the following, create a class with at least the method described and one other, storing any attributes necessary.  Instantiate each of them with three different concrete examples.  Consider what things you might want to know about each item that are common to all things in that category (e.g. every food item has a recipe, but the recipe is different for each item).

## Food

### Required method: `print_recipe()`

I should be able to create and use a food item as follows

```
pb_apple = new Food("Cut apples.\nPlace apples and some peanut butter on platter with a knife.")
pb_apple.print_recipe()
```

and get the following output:
```
Recipe
======
Cut apples.
Place apples and some peanut butter on platter with a knife.
```

Note: You can require more parameters to the `___init___` method for your second method if desired.

### Second Method
Up to you!

### Instantiate
Instantiate your class with 3 different sets of values, calling each method on each of them.  (hint: what structure do you know of that's good for storing a known number of things? How can you perform the same set of actions on each item in turn without writing repetitive code?)

## Animals

### Required method: `has_fur()`
should return a boolean

### Second Method
Up to you!

### Instantiate
Instantiate your class with 3 different sets of values, calling each method on each of them.

## Plants

### Required method: `set_is_flowering(bool)`
should take a boolean indicating whether the plant is currently flowering and update an attribute in the class accordingly

### Second Method
Up to you!

### Instantiate
Instantiate your class with 3 different sets of values, calling each method on each of them.
