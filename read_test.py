import time as timeModule
import os
import pandas as pd
from functions import read

path = ''

# main loop
while(True):
	time = read(path + 'time.txt')
	gameName = read(path + 'gameName.txt')
	homeTeamName = read(path + 'homeTeamName.txt')
	awayTeamName = read(path + 'awayTeamName.txt')
	homeScore = read(path + 'homeScore.txt')
	awayScore = read(path + 'awayScore.txt')
	homeFouls = read(path + 'homeFouls.txt')
	awayFouls = read(path + 'awayFouls.txt')
	
	df = pd.DataFrame([gameName, time, homeTeamName, awayTeamName, homeScore, 
	awayScore, homeFouls, awayFouls])
	df.index = ['Game', 'Time', 'Home team', 'Away team', 'Home score', 
	'Away score', 'Home fouls', 'Away fouls']
	df.columns = ['Game status']
	os.system('cls' if os.name == 'nt' else 'clear')
	print(df)
	timeModule.sleep(1)