import random
from helpers import aOrAn, validateIntInput, validateYesOrNoInput, generateTrip

DESTINATIONS = ['Maui', 'San Diego', 'Fiji', 'Jacksonville', 'Chernobyl']
TRANSPORTATIONS = ['uber', 'tram', 'rickshaw', 'limosine', 'helicopter']
DAYTIME_ACTIVITIES = [ 'parasailing', 'snorkeling', 'hiking', 'sight seeing', 'shopping']
RESTAURANTS = ['The Caribou', 'The Blue', "3's Bar & Grill", 'The Excalibur', 'Wingstop', "Friendly's BBQ"]
EVENING_ENTERTAINMENTS = ['comedy club', 'concert', 'bowling alley', 'rollerskating rink', 'pub crawl']
LISTS = [DESTINATIONS, TRANSPORTATIONS, DAYTIME_ACTIVITIES, RESTAURANTS, EVENING_ENTERTAINMENTS]

EDIT_PROMPT = f'''Choose an option:
  1) New destination
  2) Change mode of transportation
  3) New daytime activity
  4) New restaurant
  5) New evening entertainment
  6) Generate new trip
  7) Book it!
'''

def displayTrip(trip):
  print(f'''
You're heading to {trip[0]}!
Where {aOrAn(trip[1])} {trip[1]} will take you {trip[2]}, to dinner at {trip[3]} and then {aOrAn(trip[4])} {trip[4]}.
''')

def promptNewTrip():
  userInput = validateYesOrNoInput('Are you ready to book your trip? (y/n): ')
  if(userInput == 'y'):
    newTrip = generateTrip(LISTS)
    editTrip(newTrip)
  else:
    print('Come see us again if you change your mind!')
    exit()

#refactor to diplay options to change individual parts of the trip
def editTrip(newTrip):
  booked = False
  while not booked:
    displayTrip(newTrip)
    userInput = validateIntInput(EDIT_PROMPT)
    if(userInput > 0 and userInput < 6):
      i = userInput - 1
      newTrip[i] = random.choice(LISTS[i])
    elif(userInput == 6):
      newTrip = generateTrip(LISTS)
    elif(userInput == 7):
      booked = True
    else:
      print('Please select between 1-7')

  print(f'''Your trip has been confirmed! Please check your email.
  ''')

promptNewTrip()