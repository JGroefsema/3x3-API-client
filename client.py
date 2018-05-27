##############################################
### TODO
### - write docstring
### - reset score to 0 at start of game
### - place data files in seperate folder
##############################################

# import modules
import websocket
import json
import time
from functions import read, write, format_timeRemaining

# setup variables
path = 'data/'
url = "wss://fiba-3x3-scores-uat.herokuapp.com/api/ws"
apiKey = read('apiKey.txt')
requestId = "test connection"
eventId = read('eventId.txt')
gameId = ''
timeRemaining = 600000

# make subscribe message
subscribe = {}
subscribe['apiName'] = "TvFeedApiV3"
subscribe['apiCommand'] = "subscribe"
subscribe['apiKey'] = apiKey
subscribe['requestId'] = requestId
subscribe['eventId'] = eventId

# setup WebSocket
ws = websocket.WebSocket()
ws.connect(url)
ws.send(json.dumps(subscribe))

# main loop
while(True):
	# get data
	ans = ws.recv()
	try:
		data = json.loads(ans)['data']
	except KeyError:
		print(ans)
		break
		
	
	# get game info
	homeTeamId = read('homeTeamId.txt')
	awayTeamId = read('awayTeamId.txt')
	if gameId != read('gameId.txt'):
		gameId = read('gameId.txt')
		print('Current game: {}'.format(read('gameName.txt')))
	
	# get time remaining
	try:
		clockRunning = data[gameId]['clockRunning']
		timeRemaining = data[gameId]['timeRemaining']
		# write time remaining to file
		write(format_timeRemaining(timeRemaining), 'time.txt')
	except (KeyError, NameError):
		pass
	
	# get score
	try:
		write(data[gameId]['currentTeamScore'][homeTeamId], 'homeScore.txt')
	except (KeyError, NameError):
		pass
	try:
		write(data[gameId]['currentTeamScore'][awayTeamId], 'awayScore.txt')
	except (KeyError, NameError):
		pass
	
	# get fouls
	try:
		write(data[gameId]['currentTeamFouls'][homeTeamId], 'homeFouls.txt')
	except (KeyError, NameError):
		pass
	try:
		write(data[gameId]['currentTeamFouls'][awayTeamId], 'awayFouls.txt')
	except (KeyError, NameError):
		pass

ws.close()