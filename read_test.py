import time as timeModule
import os
import pandas as pd
from functions import read

# main loop
while(True):
	time = read('time.txt')
	gameName = read('gameName.txt')
	homeTeamName = read('homeTeamName.txt')
	awayTeamName = read('awayTeamName.txt')
	homeScore = read('homeScore.txt')
	awayScore = read('awayScore.txt')
	homeFouls = read('homeFouls.txt')
	awayFouls = read('awayFouls.txt')
	
	df = pd.DataFrame([gameName, time, homeTeamName, awayTeamName, homeScore, 
	awayScore, homeFouls, awayFouls])
	df.index = ['Game', 'Time', 'Home team', 'Away team', 'Home score', 
	'Away score', 'Home fouls', 'Away fouls']
	df.columns = ['Game status']
	os.system('cls' if os.name == 'nt' else 'clear')
	print(df)
	timeModule.sleep(1)