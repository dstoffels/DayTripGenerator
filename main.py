from helpers import aOrAn, validateIntInput, validateYesOrNoInput, generateNewTrip, changeSelectionOnTrip

DESTINATIONS = ['Maui', 'San Diego', 'Fiji', 'Jacksonville', 'Chernobyl']
TRANSPORTATIONS = ['uber', 'tram', 'rickshaw', 'limosine', 'helicopter']
DAYTIME_ACTIVITIES = [ 'parasailing', 'snorkeling', 'hiking', 'sight seeing', 'shopping']
RESTAURANTS = ['The Caribou', 'The Blue', "3's Bar & Grill", 'The Excalibur', 'Wingstop', "Friendly's BBQ"]
EVENING_ENTERTAINMENTS = ['comedy club', 'concert', 'bowling alley', 'rollerskating rink', 'pub crawl']
LISTS = [DESTINATIONS, TRANSPORTATIONS, DAYTIME_ACTIVITIES, RESTAURANTS, EVENING_ENTERTAINMENTS]

USER_CANCEL_MSG = '\nCome see us again if you change your mind!\n'

EDIT_PROMPT = f'''Choose an option:
  1) New destination
  2) Change mode of transportation
  3) New daytime activity
  4) New restaurant
  5) New evening entertainment
  6) Generate new trip
  7) Book it!
  8) Cancel
'''

def displayTrip(trip):
  print(f'''
You're heading to {trip[0]}!
Where {aOrAn(trip[1])} {trip[1]} will take you {trip[2]}, to dinner at {trip[3]} and then {aOrAn(trip[4])} {trip[4]}.
''')

def promptNewTrip():
  userInput = validateYesOrNoInput('Are you ready to book your trip? (y/n): ')
  if(userInput == 'y'):
    newTrip = generateNewTrip(LISTS)
    editTrip(newTrip)
  else:
    print(USER_CANCEL_MSG)
    exit()

def editTrip(newTrip):
  booked = False
  while not booked:
    displayTrip(newTrip)
    userSelection = validateIntInput(EDIT_PROMPT)
    if(userSelection > 0 and userSelection < 6):
      newTrip = changeSelectionOnTrip(userSelection, newTrip, LISTS)
    elif(userSelection == 6):
      newTrip = generateNewTrip(LISTS)
    elif(userSelection == 7):
      booked = True
    elif(userSelection == 8):
      print(USER_CANCEL_MSG)
      exit()
    else:
      print('Please select between 1-8')

  print(f'''Your trip to {newTrip[0]} has been confirmed! Please check your email.
  ''')

promptNewTrip()