#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  final_count = None

  for k in recipe.keys():
    if k in ingredients.keys():
      count = int(ingredients[k] / recipe[k])
      if count <= 0:
        return 0
      elif final_count is None:
        final_count = count
      else:
        if count < final_count:
          final_count = count
    else:
      return 0
    
  if final_count is None:
    return 0

  return final_count




if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))