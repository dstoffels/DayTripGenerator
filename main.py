from helpers import aOrAn, buildOptionsString, validateIntInput, validateYesOrNoInput
from tripHelpers import displayTrip, confirmTrip, generateNewTrip, changeSelectionOnTrip
from contants import INITIAL_USER_PROMPT, LISTS, USER_CANCEL_MSG, USER_OPTIONS

editPrompt = buildOptionsString()

def initialPrompt():
  userInput = validateYesOrNoInput(INITIAL_USER_PROMPT)
  if(userInput == 'y' or userInput =='yes'):
    newTrip = generateNewTrip(LISTS)
    editTrip(newTrip)
  else:
    print(USER_CANCEL_MSG)
    exit()

def editTrip(newTrip):
  booked = False
  while not booked:
    displayTrip(newTrip)
    userSelection = validateIntInput(editPrompt)
    if(userSelection > 0 and userSelection < 6):
      newTrip = changeSelectionOnTrip(userSelection, newTrip, LISTS)
    elif(userSelection == 6):
      newTrip = generateNewTrip(LISTS)
    elif(userSelection == 7):
      booked = True
      confirmTrip(newTrip)
    elif(userSelection == 8):
      print(USER_CANCEL_MSG)
      exit()
    else:
      print(f'Please select between 1-{len(USER_OPTIONS)}')
  exit()

initialPrompt()