from soccersimulator import *
from soccersimulator.settings import *
from tools import *
import random
import math

## Strategie defense 1
class defense(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Defense1")
	def compute_strategy(self,state,id_team,id_player):
		f = functions(state,id_team,id_player)
		idEnemy = f.idEnemy
		if f.Team2():
			if f.Ballx2sup():
				return f.ShootOuAvanceVersBalle()
			else:
				return f.Ralenti()
		else:
			if f.Ballx2inf():
				return f.ShootOuAvanceVersBalle()
			else:
				return f.Ralenti()

## Strategie defense 2
class defense2(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Defense2")
	def compute_strategy(self,state,id_team,id_player):
		f = functions(state,id_team,id_player)
		idEnemy = f.idEnemy
		if f.Team2():
			if f.Ballx4sup():
				return f.ShootOuAvanceVersBalle()
			else:
				return f.Ralenti()
		else:
			if f.Ballx4inf():
				return f.ShootOuAvanceVersBalle()
			else:
				return f.Ralenti()

## Strategie Attente puis But
class stratAttente(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Attack1")
	def compute_strategy(self,state,id_team,id_player):
		f = functions(state,id_team,id_player)
		idEnemy = f.idEnemy
		playerDataa = f.playerData()
		if(f.canShoot()):
			return f.TirDirect()
		else:
			if f.Team2() and (f.id_player == 1) and f.Ballx2sup():
				return f.BougePas()
			elif f.Team1() and (f.id_player == 1) and f.Ballx2inf():
				return f.BougePas()
			elif f.Team1() and (f.id_player == 2) and f.Ballx4sup() and (playerDataa[0]>3*GAME_WIDTH / 4):
				return f.BougePas()
			elif f.Team2() and (f.id_player == 2) and f.Ballx4inf() and (playerDataa[0]<GAME_WIDTH / 4):
				return f.BougePas()
			else:
				return f.AvanceVersBalle()


