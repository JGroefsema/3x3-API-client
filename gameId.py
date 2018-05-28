# import modules
import websocket
import json
import time
from functions import read, write, reset_score

# setup variables
path = 'data/'
url = "wss://fiba-3x3-scores-uat.herokuapp.com/api/ws"
apiKey = read(path + 'apiKey.txt')
requestId = "test connection"
eventId = read(path + 'eventId.txt')
gameId = ''
ignorList =[]

# make subscribe message
subscribe = {}
subscribe['apiName'] = "TvFeedApiV3"
subscribe['apiCommand'] = "subscribe"
subscribe['apiKey'] = apiKey
subscribe['requestId'] = requestId
subscribe['eventId'] = eventId

# setup WebSocket
ws = websocket.WebSocket()

# start ws connection
ws.connect(url)

# subscribe to feed
ws.send(json.dumps(subscribe))

# initialize files
write('Home', path + 'homeTeamName.txt')
write('Away', path + 'awayTeamName.txt')
reset_score()

# main loop
while(True):
	# get data
	ans = ws.recv()
	try:
		data = json.loads(ans)['data']
	except KeyError:
		print(ans)
		break
	
	# get team info
	try:
		for i in data:
			if data[i]['dataType'] == 'game' and i not in ignorList:
				game_info = data[i]
				gameName = game_info['gameName']
				homeTeamId = game_info['homeTeamId']
				homeTeamName = data[homeTeamId]['teamName']
				awayTeamId = game_info['awayTeamId']
				awayTeamName = data[awayTeamId]['teamName']
				print('New game found: {}, {} vs. {}'.format(gameName, homeTeamName, awayTeamName))
				input_var = input('Make this new game the current game? No will ingor this game. [Y/n]')
				if input_var.lower() == 'y':
					write(i, path + 'gameId.txt')
					homeTeamId = game_info['homeTeamId']
					awayTeamId = game_info['awayTeamId']
					write(data[homeTeamId]['teamName'], path + 'homeTeamName.txt')
					write(data[awayTeamId]['teamName'], path + 'awayTeamName.txt')
					write(homeTeamId, path + 'homeTeamId.txt')
					write(awayTeamId, path + 'awayTeamId.txt')
					write(gameName, path + 'gameName.txt')
					reset_score()
				elif input_var.lower() == 'n':
					ignorList.append(i)
	except (KeyError, NameError):
		pass