import sys
import pygame
from settings import Settings
import game_functions as gf
from ship import Ship
def run_game():
	pygame.init()
	ai_settings=Settings()
	
	screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	ship=Ship(ai_settings,screen)
	#pygame.display.set_caption("Alien Invation")

	
	while True:
		gf.check_events(ship)
		ship.update()
		gf.update_screen(ai_settings,screen,ship)

run_game() 
