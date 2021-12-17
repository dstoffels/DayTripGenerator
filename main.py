from helpers import buildOptionsString, validateIntInput, validateYesOrNoInput
from tripHelpers import cancelTrip, confirmTrip, generateNewTrip, changeSelectionOnTrip
from contants import INITIAL_USER_PROMPT, LISTS, OPTIONS_ERR_MSG

def promptUserForNewTrip():
  userInput = validateYesOrNoInput(INITIAL_USER_PROMPT)
  if(userInput == 'y' or userInput =='yes'):
    newTrip = generateNewTrip(LISTS)
    promptUserToEditConfirmOrCancelTrip(newTrip)
  else:
    cancelTrip()

def promptUserToEditConfirmOrCancelTrip(newTrip):
  prompt = buildOptionsString()

  while True:
    userSelection = validateIntInput(prompt)

    match userSelection:
      case 1 | 2 | 3 | 4 | 5:
        newTrip = changeSelectionOnTrip(userSelection, newTrip, LISTS)
        prompt = buildOptionsString()
      case 6:
        newTrip = generateNewTrip(LISTS)
        prompt = buildOptionsString()
      case 7:
        confirmTrip(newTrip)
      case 8:
        cancelTrip()
      case _:
        prompt = OPTIONS_ERR_MSG

promptUserForNewTrip()