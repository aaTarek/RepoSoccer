from soccersimulator  import Strategy, SoccerAction, Vector2D
from soccersimulator import SoccerTeam, Simulation
from soccersimulator import show_simu
import random
from decimal import *

## Strategie aleatoire
class RandomStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Random")
    def compute_strategy(self,state,id_team,id_player):
        return SoccerAction(Vector2D(1,1,Decimal(random.randint(0, 200)) / Decimal(1000.0),0.025),Vector2D(1,1,0,1))

class RandomStrategy2(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Random")
    def compute_strategy(self,state,id_team,id_player):
        return SoccerAction(Vector2D(1,1,3.14,0.04),Vector2D(1,1,3.14,5))

## Creation d'une equipe
pyteam = SoccerTeam(name="Overwatch")
thon = SoccerTeam(name="Rainbow6")
pyteam.add("Lucio",RandomStrategy()) #Strategie qui ne fait rien
thon.add("Valkyrie",RandomStrategy2())   #Strategie aleatoire

#Creation d'une partie
simu = Simulation(pyteam,thon)
#Jouer et afficher la partie
show_simu(simu)
