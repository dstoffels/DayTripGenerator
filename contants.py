DESTINATIONS = ['Maui', 'San Diego', 'Fiji', 'Jacksonville', 'Chernobyl']
TRANSPORTATIONS = ['uber', 'tram', 'rickshaw', 'limousine', 'helicopter']
DAYTIME_ACTIVITIES = [ 'parasailing', 'snorkeling', 'hiking', 'sight seeing', 'shopping']
RESTAURANTS = ['The Caribou', 'The Blue', "3's Bar & Grill", 'The Excalibur', 'Wingstop', "Friendly's BBQ"]
EVENING_ENTERTAINMENTS = ['comedy club', 'concert', 'bowling alley', 'rollerskating rink', 'pub crawl']
LISTS = [DESTINATIONS, TRANSPORTATIONS, DAYTIME_ACTIVITIES, RESTAURANTS, EVENING_ENTERTAINMENTS]

INITIAL_USER_PROMPT = 'Are you ready to book your trip? (y/n): '
USER_CANCEL_MSG = '\nCome see us again if you change your mind!\n'

USER_OPTIONS = ['New destination', 'Change mode of transportation', 'New daytime activity', 
'New restaurant', 'New evening entertainment', 'Generate new trip', 'Book it!', 'Cancel']

OPTIONS_ERR_MSG = f'Please enter a number between 1-{len(USER_OPTIONS)}: '