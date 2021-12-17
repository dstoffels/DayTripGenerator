import random
from contants import USER_CANCEL_MSG
from helpers import aOrAn


def generateNewTrip(lists):
  trip = []
  for list in lists:
    trip.append(random.choice(list))
  displayTrip(trip)
  return trip

def displayTrip(trip):
  print(f'''
You're heading to {trip[0]}!
Where {aOrAn(trip[1])} {trip[1]} will take you {trip[2]}, to dinner at {trip[3]} and then {aOrAn(trip[4])} {trip[4]}.
''')

# returns same trip list with user selected option randomly replaced
def changeSelectionOnTrip(selection, trip, lists):
  i = selection - 1
  newTripItem = trip[i]
  while (newTripItem == trip[i]):
    newTripItem = random.choice(lists[i])
  trip[i] = newTripItem
  displayTrip(trip)
  return trip

def confirmTrip(trip):
  print(f'''Your trip to {trip[0]} has been confirmed! Please check your email.
  ''')
  exit()

def cancelTrip():
  print(USER_CANCEL_MSG)
  exit()