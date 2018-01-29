from soccersimulator import Vector2D, SoccerState, SoccerAction
from soccersimulator import Simulation, SoccerTeam, Player, show_simu
from soccersimulator import Strategy
from soccersimulator import settings
from soccersimulator import utils
from soccersimulator.settings import *
import random
import math

def vecteurShootGoal(Balle, cage_x, cage_y, puissance):
	return Vector2D((cage_x - Balle.position.x),(cage_y - Balle.position.y)).normalize() * puissance

def teta2Vecteurs(v1, v2):
	teta = math.acos((v1.x*v2.x + v1.y*v2.y) / (v1.norm*v2.norm))
	print teta
	return teta

def idTEnemy(id_Team):
	if(id_Team == 2):
		return 1
	return 2

#def obstacle(Balle, cage_x, cage_y, puissance):
#	tirVecteur = vecteurShootGoal(Balle, cage_x, cage_y, puissance)
	
	
	
