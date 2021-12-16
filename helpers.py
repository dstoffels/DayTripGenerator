import random

def aOrAn(word):
  vowels = ['a','e','i','o','u']
  for vowel in vowels:
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
      print('Please enter a number')

def generateNewTrip(lists):
  trip = []
  for list in lists:
    trip.append(random.choice(list))
  return trip

def changeSelectionOnTrip(selection, trip, lists):
  i = selection - 1
  newTripItem = trip[i]
  while (newTripItem == trip[i]):
    newTripItem = random.choice(lists[i])
  trip[i] = newTripItem
  return trip
