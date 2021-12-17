from contants import OPTIONS_ERR_MSG, USER_OPTIONS

def aOrAn(word):
  VOWELS = ['a','e','i','o','u']
  for vowel in VOWELS:
    if(word[0] == vowel):
      return 'an'
  return 'a'

def validateYesOrNoInput(prompt):
  ACCEPTABLE_INPUTS = ['y', 'yes', 'n', 'no']
  userInput = str.lower(input(prompt)) 
  while True:
    for acceptableInput in ACCEPTABLE_INPUTS:
      if(userInput == acceptableInput):
        return userInput 
    userInput = input("Please enter 'y' or 'n'.")

def validateIntInput(prompt):
  while True:
    try:
      response = int(input(prompt))
      return response
    except:
      prompt = OPTIONS_ERR_MSG

def buildOptionsString():
  optionsString = ''
  i = 1
  for option in USER_OPTIONS:
    optionsString += f'''{i}) {option}\n'''
    i += 1
  return optionsString + '\nChoose an option: '


