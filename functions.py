path = 'data/'

def read(inFile):
	with open(inFile, 'r') as f:
		read = f.read()
		f.close()
	return read

def write(data, outFile):
    with open(outFile, 'w') as f:
        f.write(str(data))
        f.close()
    return

def reset_score():
	write('10:00', path + 'time.txt')
	write('0', path + 'homeScore.txt')
	write('0', path + 'awayScore.txt')
	write('0', path + 'homeFouls.txt')
	write('0', path + 'awayFouls.txt')
	return

def format_timeRemaining(timeRemaining):
    minRemaining = (timeRemaining//1000 - timeRemaining//1000 %60)//60//1
    secRemaining= timeRemaining//1000 %60
    return str(int(minRemaining)).zfill(2)+':'+str(int(secRemaining)).zfill(2)
    
def initial_call():
	# check if correct files are present, else error out
	read('apiKey.txt')
	read('apiURL.txt')
	read('eventId.txt')
	
	# create path dir
	import os
	if not os.path.exists(path):
	    os.makedirs(path)

	# create neccesary files
	fileList = ['gameName', 'time', 'homeTeamName', 'awayTeamName', 
	'homeScore', 'awayScore', 'homeFouls', 'awayFouls', 'awayTeamId', 
	'gameId', 'homeScore', 'homeTeamId']
	for i in fileList:
		write('0', path + i + '.txt')
	return