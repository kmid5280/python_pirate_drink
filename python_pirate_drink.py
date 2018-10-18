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

def pirate_drink():
  """This function asks the user questions about their drink from the questions dictionary, and if the user answers yes, will output the drink's ingredients according to the ingredients dictionary."""
  strong = ''
  salty = ''
  bitter = ''
  sweet = ''
  fruity = ''

  while strong not in ("y","n"):
    strong = input(questions["strong"])
    if strong == 'y':
      print(ingredients["strong"])
    elif strong == 'n':
      print('No strong then.')
    else:
      print("y or n")
      
  while salty not in ('y','n'):
    salty = input(questions["salty"])
    if salty == 'y':
      print(ingredients["salty"])
    elif strong == 'n':
      print('No salty then.')
    else:
      print("y or n")
  
  while bitter not in ('y','n'):
    bitter = input(questions["bitter"])
    if bitter == 'y':
      print(ingredients["bitter"])
    elif bitter == 'n':
      print('No bitter then.')
    else:
      print("y or n")
  
  while sweet not in ('y','n'):
    sweet = input(questions["sweet"])
    if sweet == 'y':
      print(ingredients["sweet"])
    elif sweet == 'n':
      print('No sweet then.')
    else:
      print("y or n")
  
  while fruity not in ('y','n'):
    fruity = input(questions["fruity"])
    if fruity == 'y':
      print(ingredients["fruity"])
    elif fruity == 'n':
      print('No fruity then.')
    else:
      print("y or n")


if __name__ == '__main__':
  pirate_drink()