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
from functions import read, write, format_timeRemaining, initial_call

initial_call()

# setup variables
path = ''
url = read('apiURL.txt')
gameId = ''
timeRemaining = 600000

# make subscribe message
subscribe = {}
subscribe['apiName'] = "TvFeedApiV3"
subscribe['apiCommand'] = "subscribe"
subscribe['apiKey'] = read('apiKey.txt')
subscribe['requestId'] = "test connection"
subscribe['eventId'] = read('eventId.txt')

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
	homeTeamId = read(path + 'homeTeamId.txt')
	awayTeamId = read(path + 'awayTeamId.txt')
	if gameId != read(path + 'gameId.txt'):
		gameId = read(path + 'gameId.txt')
		print('Current game: {}'.format(read(path + 'gameName.txt')))
	
	# get time remaining
	try:
		clockRunning = data[gameId]['clockRunning']
		timeRemaining = data[gameId]['timeRemaining']
		# write time remaining to file
		write(format_timeRemaining(timeRemaining), path + 'time.txt')
	except (KeyError, NameError):
		pass
	
	# get score
	try:
		write(data[gameId]['currentTeamScore'][homeTeamId], path + 'homeScore.txt')
	except (KeyError, NameError):
		pass
	try:
		write(data[gameId]['currentTeamScore'][awayTeamId], path + 'awayScore.txt')
	except (KeyError, NameError):
		pass
	
	# get fouls
	try:
		write(data[gameId]['currentTeamFouls'][homeTeamId], path + 'homeFouls.txt')
	except (KeyError, NameError):
		pass
	try:
		write(data[gameId]['currentTeamFouls'][awayTeamId], path + 'awayFouls.txt')
	except (KeyError, NameError):
		pass

ws.close()