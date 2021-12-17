from helpers import aOrAn, buildOptionsString, validateIntInput, validateYesOrNoInput
from tripHelpers import cancelTrip, displayTrip, confirmTrip, generateNewTrip, changeSelectionOnTrip
from contants import INITIAL_USER_PROMPT, LISTS, OPTIONS_ERR_MSG, USER_CANCEL_MSG, USER_OPTIONS


def initialPrompt():
  userInput = validateYesOrNoInput(INITIAL_USER_PROMPT)
  if(userInput == 'y' or userInput =='yes'):
    newTrip = generateNewTrip(LISTS)
    editTrip(newTrip)
  else:
    print(USER_CANCEL_MSG)
    exit()

def editTrip(newTrip):
  prompt = buildOptionsString()
  displayTrip(newTrip)
  while True:
    userSelection = validateIntInput(prompt)

    if(userSelection > 0 and userSelection < 6):
      newTrip = changeSelectionOnTrip(userSelection, newTrip, LISTS)
      prompt = buildOptionsString()
    elif(userSelection == 6):
      newTrip = generateNewTrip(LISTS)
      prompt = buildOptionsString()
    elif(userSelection == 7):
      confirmTrip(newTrip)
    elif(userSelection == 8):
      cancelTrip()
    else:
      prompt = OPTIONS_ERR_MSG

initialPrompt()