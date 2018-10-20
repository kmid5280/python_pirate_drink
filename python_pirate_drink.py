from questions import questions
from ingredients import ingredients

responses = {}
ingredient_results = []

def pirate_drink():
  """This function asks the user questions about their drink from the questions dictionary, and if the user answers yes, will output the drink's ingredients according to the ingredients dictionary."""
  strong = ''
  salty = ''
  bitter = ''
  sweet = ''
  fruity = ''

  while strong not in ("y","n", "yes", "no"):
    strong = input(questions["strong"])
    if strong == 'y' or strong == 'yes':
      responses['strong'] = True
      print("Adding strong ingredients then.")
    elif strong == 'n' or strong == 'no':
      responses['strong'] = False
      print('No strong then.')
    else:
      print("y or n")
      
  while salty not in ("y","n", "yes", "no"):
    salty = input(questions["salty"])
    if salty == 'y' or salty == 'yes':
      responses['salty'] = True
      print("Adding salty ingredients then.")
    elif salty == 'n' or salty == 'no':
      responses['salty'] = False
      print('No salty then.')
    else:
      print("y or n")
  
  while bitter not in ("y","n", "yes", "no"):
    bitter = input(questions["bitter"])
    if bitter == 'y':
      responses['bitter'] = True
      print("Adding bitter ingredients then.")
    elif bitter == 'n':
      responses['bitter'] = False
      print('No bitter then.')
    else:
      print("y or n")
  
  while sweet not in ("y","n", "yes", "no"):
    sweet = input(questions["sweet"])
    if sweet == 'y':
      responses['sweet'] = True
      print("Adding sweet ingredients then.")
    elif sweet == 'n':
      responses['sweet'] = False
      print('No sweet then.')
    else:
      print("y or n")
  
  while fruity not in ("y","n", "yes", "no"):
    fruity = input(questions["fruity"])
    if fruity == 'y':
      responses['fruity'] = True
      print("Adding fruity ingredients then.")
    elif fruity == 'n':
      responses['fruity'] = False
      print('No fruity then.')
    else:
      print("y or n")


def return_ingredients():
  """This function adds necessary ingredients to the drink based on the user's responses."""
  if responses['strong'] == True:
    ingredient_results.extend(ingredients['strong'])
  if responses['salty'] == True:
    ingredient_results.extend(ingredients['salty'])
  if responses['bitter'] == True:
    ingredient_results.extend(ingredients['bitter'])
  if responses['sweet'] == True:
    ingredient_results.extend(ingredients['sweet'])
  if responses['fruity'] == True:
    ingredient_results.extend(ingredients['fruity'])
  
  print("Your total ingredients are: ", ingredient_results)

if __name__ == '__main__':
  pirate_drink()
  return_ingredients()