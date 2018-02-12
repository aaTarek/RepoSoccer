from soccersimulator  import Strategy, SoccerAction, Vector2D
from soccersimulator import Simulation, SoccerTeam, Player, show_simu
from soccersimulator import Strategy
from soccersimulator import settings
from soccersimulator.settings import *
from tools import *
import random
import math

## Strategie Attente puis But
class stratAttente(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Random")
	def compute_strategy(self,state,id_team,id_player):
		idEnemy = idTEnemy(id_team)
		playerPositionX = state.player_state(id_team, id_player).position.x
		playerPositionY = state.player_state(id_team, id_player).position.y
		ballPositionX = state.ball.position.x
		ballPositionY = state.ball.position.y
		goalX = 0
		goalY = GAME_HEIGHT / 2
		if (id_team == 1):
			goalX = GAME_WIDTH
			# distance entre le joueur et la balle
		dist = math.hypot(ballPositionX - playerPositionX, ballPositionY - playerPositionY)
		# Si la balle est au centre (engagement) on ne bouge pas
		if (state.ball.position.x == (GAME_WIDTH / 2)) and (state.ball.position.y == (GAME_HEIGHT / 2) and state.step < 35):
			return SoccerAction(Vector2D(0,0), Vector2D(0,0))
		# 
		elif(dist < PLAYER_RADIUS + BALL_RADIUS and state.ball.position.x > GAME_WIDTH / 2 and state.player_state(idEnemy, id_player).position.y > playerPositionY):
			return SoccerAction(Vector2D(angle=3.14,norm=0.2), vecteurShootGoal(state.ball, goalX, state.player_state(id_team, id_player).position.y, 10))
		elif(dist < PLAYER_RADIUS + BALL_RADIUS):
			return SoccerAction(Vector2D(angle=3.14,norm=0.2), vecteurShootGoal(state.ball, goalX, GAME_HEIGHT / 2, 10))
		else:
			return SoccerAction(Vector2D(ballPositionX - playerPositionX,ballPositionY - playerPositionY).normalize() * maxPlayerAcceleration, Vector2D(0,0))


## Strategie aleatoire
class RandomStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Random")
    def compute_strategy(self,state,id_team,id_player):
        return SoccerAction(Vector2D.create_random(),Vector2D.create_random())

class Fonceur(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Random")
	def compute_strategy(self,state,id_team,id_player):
		idEnemy = idTEnemy(id_team)
		playerPositionX = state.player_state(id_team, id_player).position.x
		playerPositionY = state.player_state(id_team, id_player).position.y
		ballPositionX = state.ball.position.x
		ballPositionY = state.ball.position.y
		dist = math.hypot(ballPositionX - playerPositionX, ballPositionY - playerPositionY)
		goalX = 0
		goalY = GAME_HEIGHT / 2
		if (id_team == 1):
			goalX = GAME_WIDTH
		if(dist < PLAYER_RADIUS + BALL_RADIUS and state.ball.position.x > GAME_WIDTH / 2):
			return SoccerAction(Vector2D(angle=3.14,norm=0.2), vecteurShootGoal(state.ball, goalX, state.player_state(id_team, id_player).position.y, 10))
		elif(dist < PLAYER_RADIUS + BALL_RADIUS):
			return SoccerAction(Vector2D(angle=3.14,norm=0.2), vecteurShootGoal(state.ball, goalX, GAME_HEIGHT / 2, 4.5))
		else:
			return SoccerAction(Vector2D(ballPositionX - playerPositionX,ballPositionY - playerPositionY).normalize() * maxPlayerAcceleration, Vector2D(0,0))

class Strategy2(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Random")
	def compute_strategy(self,state,id_team,id_player):
		playerPositionX = state.player_state(id_team, id_player).position.x
		playerPositionY = state.player_state(id_team, id_player).position.y
		ballPositionX = state.ball.position.x
		ballPositionY = state.ball.position.y
		dist = math.hypot(ballPositionX - playerPositionX, ballPositionY - playerPositionY)
		if(dist < PLAYER_RADIUS + BALL_RADIUS):
			return SoccerAction(Vector2D(angle=3.14,norm=0.2), vecteurShootGoal(state.ball, GAME_WIDTH, GAME_HEIGHT / 2, 10))
		else:
			return SoccerAction(Vector2D(ballPositionX - playerPositionX,ballPositionY - playerPositionY).normalize() * maxPlayerAcceleration, Vector2D(0,0))

