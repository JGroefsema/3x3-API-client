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
    minRemaining = (timeRemaining//1000 - timeRemaining//1000 %60)//60
    secRemaining= timeRemaining//1000 %60
    return str(minRemaining).zfill(2)+':'+str(secRemaining).zfill(2)