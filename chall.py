from soccersimulator import SoccerTeam, Simulation, show_simu, Strategy
from strategies  import *


## Creation d'une equipe
pyteam = SoccerTeam(name="PyTeam")
thon = SoccerTeam(name="ThonTeam")
pyteam.add("PyPlayer",Fonceur()) #Strategie qui ne fait rien
thon.add("ThonPlayer",stratAttente())   #Strategie aleatoire

#Creation d'une partie
simu = Simulation(pyteam,thon)
#Jouer et afficher la partie
show_simu(simu)
