from soccersimulator import Vector2D, SoccerState, SoccerAction
from soccersimulator import Simulation, SoccerTeam, Player, show_simu
from soccersimulator import Strategy
from soccersimulator import settings
from soccersimulator.settings import *
import random
import math

## Strategie aleatoire
class RandomStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Random")
	self.counter = 0
	self.randAngle = 0
	self.norm = 0
    def compute_strategy(self,state,id_team,id_player):
	if self.counter % 25 == 0:
		self.randAngle = random.random() * 6.28
		self.norm = random.random() * 0.2 
	self.counter = self.counter + 1

	playerPositionX = state.player_state(id_team, id_player).position.x
	playerPositionY = state.player_state(id_team, id_player).position.y
	ballPositionX = state.ball.position.x
	ballPositionY = state.ball.position.y
	dist = math.hypot(ballPositionX - playerPositionX, ballPositionY - playerPositionY)
	if(dist < PLAYER_RADIUS + BALL_RADIUS):
        	return SoccerAction(Vector2D(angle=self.randAngle,norm=self.norm), Vector2D(3.14,1))
	else:
		return SoccerAction(Vector2D(angle=self.randAngle,norm=self.norm), Vector2D(0,0))

## Creation d'une equipe
pyteam = SoccerTeam(name="Overwatch")
thon = SoccerTeam(name="Rainbow6")
pyteam.add("Lucio",RandomStrategy()) #Strategie qui ne fait rien
thon.add("Valkyrie",RandomStrategy())   #Strategie aleatoire

#Creation d'une partie
simu = Simulation(pyteam,thon)
#Jouer et afficher la partie
show_simu(simu)
































