from soccersimulator import SoccerTeam, Simulation, show_simu, Strategy
from strategies  import *


## Creation d'une equipe
pyteam = SoccerTeam(name="PyTeam")
thon = SoccerTeam(name="ThonTeam")

pyteam.add("PyPlayer",defense()) #Strategie qui ne fait rien
pyteam.add("PyPlayer2",attente()) #Strategie qui ne fait rien
#pyteam.add("PyPlayer3",stratAttente())

thon.add("ThonPlayer",stratAttente())   #Strategie aleatoire
#thon.add("ThonPlayer2",defense())   #Strategie aleatoire
#thon.add("ThonPlayer3",defense2())

#Creation d'une partie
simu = Simulation(pyteam,thon)
#Jouer et afficher la partie
show_simu(simu)
