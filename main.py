from helpers import buildOptionsString, validateIntInput, validateYesOrNoInput
from tripHelpers import cancelTrip, confirmTrip, generateNewTrip, changeSelectionOnTrip
from contants import INITIAL_USER_PROMPT, LISTS, OPTIONS_ERR_MSG

def promptUserForNewTrip():
  userInput = validateYesOrNoInput(INITIAL_USER_PROMPT)
  if(userInput == 'y' or userInput =='yes'):
    newTrip = generateNewTrip(LISTS)
    promptUserToEditOrConfirmOrCancelTrip(newTrip)
  else:
    cancelTrip()

def promptUserToEditOrConfirmOrCancelTrip(newTrip):
  prompt = ''
  def resetPrompt():
    prompt = buildOptionsString()

  resetPrompt()
  while True:
    userSelection = validateIntInput(prompt)

    match userSelection:
      case 1 | 2 | 3 | 4 | 5:
        newTrip = changeSelectionOnTrip(userSelection, newTrip, LISTS)
        resetPrompt()
      case 6:
        newTrip = generateNewTrip(LISTS)
        resetPrompt()
      case 7:
        confirmTrip(newTrip)
      case 8:
        cancelTrip()
      case _:
        prompt = OPTIONS_ERR_MSG

promptUserForNewTrip()