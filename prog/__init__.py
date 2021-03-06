from .strategies import *
from soccersimulator import *

def get_team(nb_players):
	myteam = SoccerTeam(name="MaTeam")
	if nb_players == 1:
		myteam.add("Joueur " ,stratAttente())
	if nb_players == 2:
		myteam.add("Joueur 1", defense())
		myteam.add("Joueur 2", stratAttente())
	if nb_players == 4:
		myteam.add("Joueur 1",defense())
		myteam.add("Joueur 2",stratAttente())
		myteam.add("Joueur 3",stratAttente())
		myteam.add("Joueur 4",defense2())
	return myteam	

def get_team_challenge(num):
	myteam = SoccerTeam(name="MaTeamChallenge")
	if num == 1:
		myteam.add("Joueur Chal "+str(num),RandomStrategy())
	return myteam


