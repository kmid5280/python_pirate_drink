questions = {
  "strong": "Do ye like yer drinks strong?",
  "salty": "Do ye like it with a salty tang?",
  "bitter": "Are ye a lubber who likes it bitter?",
  "sweet": "Would ye like a bit of sweetness with yer poison?",
  "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
  "strong": ["glug of rum", "slug of whisky", "splash of gin"],
  "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
  "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
  "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
  "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

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
      print(responses)
      print(ingredients["strong"])
    elif strong == 'n' or strong == 'no':
      responses['strong'] = False
      print('No strong then.')
      print(responses)
    else:
      print("y or n")
      
  while salty not in ("y","n", "yes", "no"):
    salty = input(questions["salty"])
    if salty == 'y' or salty == 'yes':
      responses['salty'] = True
      print(ingredients["salty"])
    elif salty == 'n' or salty == 'no':
      responses['salty'] = False
      print('No salty then.')
    else:
      print("y or n")
  
  while bitter not in ("y","n", "yes", "no"):
    bitter = input(questions["bitter"])
    if bitter == 'y':
      responses['bitter'] = True
      print(ingredients["bitter"])
    elif bitter == 'n':
      responses['bitter'] = False
      print('No bitter then.')
    else:
      print("y or n")
  
  while sweet not in ("y","n", "yes", "no"):
    sweet = input(questions["sweet"])
    if sweet == 'y':
      responses['sweet'] = True
      print(ingredients["sweet"])
    elif sweet == 'n':
      responses['sweet'] = False
      print('No sweet then.')
    else:
      print("y or n")
  
  while fruity not in ("y","n", "yes", "no"):
    fruity = input(questions["fruity"])
    if fruity == 'y':
      responses['fruity'] = True
      print(ingredients["fruity"])
    elif fruity == 'n':
      responses['fruity'] = False
      print('No fruity then.')
    else:
      print("y or n")


def return_ingredients():
  """This function adds necessary ingredients to the drink based on the user's responses."""
  if responses['strong'] == True:
    ingredient_results.append(ingredients['strong'])
  if responses['salty'] == True:
    ingredient_results.append(ingredients['salty'])
  if responses['bitter'] == True:
    ingredient_results.append(ingredients['bitter'])
  if responses['sweet'] == True:
    ingredient_results.append(ingredients['sweet'])
  if responses['fruity'] == True:
    ingredient_results.append(ingredients['fruity'])
  
  print("Your total ingredients are: ", ingredient_results)

if __name__ == '__main__':
  pirate_drink()
  return_ingredients()