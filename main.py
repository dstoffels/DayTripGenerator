import random
from helpers import aOrAn, intInput, yesOrNoInput

destinations = ['Maui', 'San Diego', 'Fiji', 'Jacksonville', 'Chernobyl']
entertainmentsByDay = [ 'parasailing', 'snorkeling', 'hiking', 'sight seeing', 'shopping']
restaurants = ['The Caribou', 'The Blue', "3's Bar & Grill", 'The Excalibur', 'Wingstop', "Friendly's BBQ"]
entertainmentsByNight = ['comedy club', 'concert', 'bowling alley', 'rollerskating rink', 'pub crawl']
transportations = ['uber', 'tram', 'bicycle', 'limosine', 'helicopter']
lists = [destinations, entertainmentsByDay, restaurants, entertainmentsByNight, transportations]

def generateRandomTrip(lists):
  trip = []
  for list in lists:
    trip.append(random.choice(list))
  return trip



def displayTrip(trip):
  print(f'''
You're heading to {trip[0]}!
There, you'll start with some {trip[1]}, followed by dinner reservations at {trip[2]} and then {aOrAn(trip[3])} {trip[3]}.
{aOrAn(trip[4])} {trip[4]} will get you to & from each stop.
''')

#refactor to diplay options to change individual parts of the trip
def confirmTrip():
  userInput = intInput(f'''
  Choose an option:
  1) Change destination
  2) ''')
  # while (userInput == 'n'):
  #   userInput = input('Book this trip? (y/n): ')
  #   newTrip = generateRandomTrip(lists)
  #   displayTrip(newTrip)
  print('Your trip has been confirmed! Please check your email.')

def promptNewTrip():
  userInput = input('Are you ready for your trip? (y/n): ')
  if(userInput == 'y'):
    newTrip = generateRandomTrip(lists)
    displayTrip(newTrip)
    confirmTrip()
  else:
    print('Come see us again if you change your mind!')
    exit()

promptNewTrip()
# allow user to pick which part of the trip they'd like to change
# display numbered options: 1 new destination, 2 new restaurant, 3 new entertainment, 4 change transportation, 5 new trip, 6 book it!
