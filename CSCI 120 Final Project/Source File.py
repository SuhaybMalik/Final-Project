import pygame
from sys import exit
import random
from Classes import player_brawler
from Classes import Enemy

def display_player_health(player):

    """dynamically displayers the players current health each turn"""

    health = player.current_health
    health_surface = game_font_50.render(f'Health: {health}', False, (64, 64, 64))
    health_rectangle = health_surface.get_rect(topleft = (100, 50))
    screen.blit(health_surface, health_rectangle)

def display_player_stamina(player):

    """dynamically displays the players current stamina each turn"""

    stamina = player.current_stamina
    stamina_surface = game_font_50.render(f'Stamina: {stamina}', False, (64, 64, 64))
    stamina_rectangle = stamina_surface.get_rect(topleft = (100, 80))
    screen.blit(stamina_surface, stamina_rectangle)

def display_enemy_health(enemy):

    """dynamically displays the enemy's current health each turn"""

    health = enemy.current_health
    health_surface = game_font_50.render(f'Health: {health}', False, (64, 64, 64))
    health_rectangle = health_surface.get_rect(topright = (1100, 50))
    screen.blit(health_surface, health_rectangle)

#initializing pygame and creating a blank display
pygame.init()
width = 1200
height = 600
screen = pygame.display.set_mode((width, height))

#loading and playing music
pygame.mixer.music.load('../CSCI 120 Final Project/Music/game song.wav')
pygame.mixer.music.play()
MUSIC_END = pygame.USEREVENT
pygame.mixer.music.set_endevent(MUSIC_END)

#loading the logo and other useful assets
pygame.display.set_caption('Adventure of Pie')
logo = pygame.image.load('../CSCI 120 Final Project/game logo/pie logo.jpg')
pygame.display.set_icon(logo)
clock = pygame.time.Clock()
game_font_25 = pygame.font.Font('../CSCI 120 Final Project/font/Pixeltype.ttf', 25)
game_font_50 = pygame.font.Font('../CSCI 120 Final Project/font/Pixeltype.ttf', 50)
game_font_150 = pygame.font.Font('../CSCI 120 Final Project/font/Pixeltype.ttf', 150)

#booleans to control game states
running = True
game_active = True
fight_1 = True  
fight_2 = False
fight_3 = False
final_fight = False
game_won = False

#loading the backgorund and game over text
background = pygame.image.load('../CSCI 120 Final Project/Graphics/Backgrounds/battle background.png').convert_alpha()
cloud_surface = pygame.image.load('../CSCI 120 Final Project/Graphics/Backgrounds/clouds.png').convert_alpha()
cloud_rectangle = cloud_surface.get_rect(topleft = (0, 0))

game_over_surface = game_font_150.render('GAME OVER!', False, (64, 64, 64))
game_over_rectanlge = game_over_surface.get_rect(center = (600, 300))
win_surface = game_font_150.render('YOU WON!', False, (64, 64, 64))
win_rectangle = win_surface.get_rect(center = (600, 300))
restart_surface = game_font_50.render('PRESS SPACE TO RESTART!', False, (64, 64, 64))
restart_rectangle = restart_surface.get_rect(center = (600, 400))
jab_text_surface = game_font_25.render('-5 Stamina : 10 Damage', False, 'white')
punch_text_surface = game_font_25.render('-40 Stamina : 40 Damage', False, 'white')
flex_text_surface = game_font_25.render('-25 Stamina : Next Attack 3X', False, 'white')
focus_text_surface = game_font_25.render('+20 Stamina', False, 'white') 

#loading the player character
player_x, player_y = (275, 370)
player_surface = pygame.image.load('../CSCI 120 Final Project/Graphics/Characters/player_1.png').convert_alpha()
player_rectangle = player_surface.get_rect(center = (player_x, player_y))
player = player_brawler(100, 100, 1, 10, 40, 0, 0)

#loading buttons that control player abilities
ability_punch_button_surface = pygame.image.load('../CSCI 120 Final Project/Graphics/Buttons/punch button.png').convert_alpha()
ability_punch_button_rectangle = ability_punch_button_surface.get_rect(center = (150, 550))
ability_flex_button_surface = pygame.image.load('../CSCI 120 Final Project/Graphics/Buttons/flex button.png').convert_alpha()
ability_flex_button_rectangle = ability_flex_button_surface.get_rect(center = (1050, 550))
ability_focus_button_surface = pygame.image.load('../CSCI 120 Final Project/Graphics/Buttons/focus button.png').convert_alpha()
ability_focus_button_rectangle = ability_focus_button_surface.get_rect(center = (825, 550))
ability_jab_button_surface = pygame.image.load('../CSCI 120 Final Project/Graphics/Buttons/jab button.png').convert_alpha()
ability_jab_button_rectangle = ability_jab_button_surface.get_rect(center = (375, 550))

#loading enemies
enemy_x, enemy_y = (925, 350)
test_hurt = 0

ringmaster = Enemy(80, 15, 20)
ringmaster_surface = pygame.image.load('../CSCI 120 Final Project/Graphics/Characters/ringmaster_1.png').convert_alpha()
ringmaster_rectangle = ringmaster_surface.get_rect(center = (enemy_x, enemy_y))
ringmaster_hurt = pygame.image.load('../CSCI 120 Final Project/Graphics/Characters/ringmaster_2.png')

mermaidman = Enemy(50, 7, 10)
mermaidman_surface = pygame.image.load('../CSCI 120 Final Project/Graphics/Characters/mermaidman_1.png').convert_alpha()
mermaidman_rectangle = mermaidman_surface.get_rect(center = (enemy_x, enemy_y))
mermaidman_hurt = pygame.image.load('../CSCI 120 Final Project/Graphics/Characters/mermaidman_2.png').convert_alpha()

foxy = Enemy(150, 17, 23)
foxy_surface = pygame.image.load('../CSCI 120 Final Project/Graphics/Characters/foxy_1.png').convert_alpha()
foxy_rectangle = foxy_surface.get_rect(center = (enemy_x, enemy_y))
foxy_hurt = pygame.image.load('../CSCI 120 Final Project/Graphics/Characters/foxy_2.png')

#while loop to actually display game window
while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == MUSIC_END:
            pygame.mixer.music.play()

        if game_active:

            if fight_1:

                if player.my_turn:

                    if event.type == pygame.MOUSEBUTTONDOWN:
                    
                        if ability_punch_button_rectangle.collidepoint(event.pos) and player.current_stamina >= 40:
                            
                            mermaidman.damage_taken(player.ability_hevpunch())
                            player.set_my_turn(False, 0)
                            test_hurt = 1
                            mermaidman.enemy_turn = True
                            if not mermaidman.is_alive():
                                fight_1 = False
                                fight_2 = True
                                player.heal()
                                player.set_my_turn(True, 0)

                        elif ability_flex_button_rectangle.collidepoint(event.pos) and player.current_stamina >= 25:

                            player.ability_flex()
                            player.set_my_turn(False, 0)
                            mermaidman.enemy_turn = True

                        elif ability_focus_button_rectangle.collidepoint(event.pos):

                            player.ability_cont()
                            player.set_my_turn(False, 0)
                            mermaidman.enemy_turn = True

                        elif ability_jab_button_rectangle.collidepoint(event.pos) and player.current_stamina >= 5:

                            mermaidman.damage_taken(player.ability_punch())
                            player.set_my_turn(False, 0)
                            test_hurt = 1
                            mermaidman.enemy_turn = True
                            if not mermaidman.is_alive():
                                fight_1 = False
                                fight_2 = True
                                player.heal()
                                player.set_my_turn(True, 0)

                elif mermaidman.enemy_turn:

                    player.damage_taken(mermaidman.damage_done())
                    player.set_my_turn(True, 10)
                    mermaidman.enemy_turn = False

                    if not player.is_alive():
                        game_active = False

            elif fight_2:

                if player.my_turn:

                    if event.type == pygame.MOUSEBUTTONDOWN:

                        if ability_punch_button_rectangle.collidepoint(event.pos) and player.current_stamina >= 40:
                            
                            ringmaster.damage_taken(player.ability_hevpunch())
                            player.set_my_turn(False, 0)
                            test_hurt = 1
                            ringmaster.enemy_turn = True
                            if not ringmaster.is_alive():
                                fight_2 = False
                                fight_3 = True
                                player.heal()
                                player.set_my_turn(True, 0)

                        elif ability_flex_button_rectangle.collidepoint(event.pos) and player.current_stamina >= 25:

                            player.ability_flex()
                            player.set_my_turn(False, 0)
                            ringmaster.enemy_turn = True

                        elif ability_focus_button_rectangle.collidepoint(event.pos):

                            player.ability_cont()
                            player.set_my_turn(False, 0)
                            ringmaster.enemy_turn = True

                        elif ability_jab_button_rectangle.collidepoint(event.pos) and player.current_stamina >= 5:

                            ringmaster.damage_taken(player.ability_punch())
                            player.set_my_turn(False, 0)
                            test_hurt = 1
                            ringmaster.enemy_turn = True
                            if not ringmaster.is_alive():
                                fight_2 = False
                                fight_3 = True
                                player.heal()
                                player.set_my_turn(True, 0)

                elif ringmaster.enemy_turn:

                    player.damage_taken(ringmaster.damage_done())
                    player.set_my_turn(True, 10)
                    ringmaster.enemy_turn = False

                    if not player.is_alive():
                        game_active = False

            elif fight_3:

                if player.my_turn:

                    if event.type == pygame.MOUSEBUTTONDOWN:

                        if ability_punch_button_rectangle.collidepoint(event.pos) and player.current_stamina >= 40:
                            
                            foxy.damage_taken(player.ability_hevpunch())
                            player.set_my_turn(False, 0)
                            test_hurt = 1
                            foxy.enemy_turn = True
                            if not foxy.is_alive():
                                fight_3 = False
                                game_won = True

                        elif ability_flex_button_rectangle.collidepoint(event.pos) and player.current_stamina >= 25:

                            player.ability_flex()
                            player.set_my_turn(False, 0)
                            foxy.enemy_turn = True

                        elif ability_focus_button_rectangle.collidepoint(event.pos):

                            player.ability_cont()
                            player.set_my_turn(False, 0)
                            foxy.enemy_turn = True

                        elif ability_jab_button_rectangle.collidepoint(event.pos) and player.current_stamina >= 5:

                            foxy.damage_taken(player.ability_punch())
                            player.set_my_turn(False, 0)
                            test_hurt = 1
                            foxy.enemy_turn = True
                            if not foxy.is_alive():
                                fight_3 = False
                                game_won = True

                elif foxy.enemy_turn:

                    player.damage_taken(foxy.damage_done())
                    player.set_my_turn(True, 10)
                    foxy.enemy_turn = False

                    if not player.is_alive():
                        game_active = False

            elif game_won:

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_SPACE:

                        game_active = True
                        fight_1 = True  
                        fight_2 = False
                        fight_3 = False
                        final_fight = False
                        game_won = False
                        player = player_brawler(100, 100, 1, 10, 40, 0, 0)
                        mermaidman = Enemy(50, 7, 10)
                        ringmaster = Enemy(80, 15, 20)
                        foxy = Enemy(150, 17, 23)

        else: 

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:

                    game_active = True
                    fight_1 = True  
                    fight_2 = False
                    fight_3 = False
                    final_fight = False
                    game_won = False
                    player = player_brawler(100, 100, 1, 10, 40, 0, 0)
                    mermaidman = Enemy(50, 7, 10)
                    ringmaster = Enemy(80, 15, 20)
                    foxy = Enemy(150, 17, 23)

    if game_active:

        screen.blit(background, (0, 0))

        cloud_rectangle.right += 4
        if cloud_rectangle.left >= 1200:
            cloud_rectangle.right = 0
        screen.blit(cloud_surface, cloud_rectangle)

        screen.blit(player_surface, player_rectangle)

        screen.blit(ability_punch_button_surface, ability_punch_button_rectangle)
        screen.blit(punch_text_surface, (50, 575))
        screen.blit(ability_flex_button_surface, ability_flex_button_rectangle)
        screen.blit(flex_text_surface, (940, 575))
        screen.blit(ability_focus_button_surface, ability_focus_button_rectangle)
        screen.blit(focus_text_surface, (775, 575))
        screen.blit(ability_jab_button_surface, ability_jab_button_rectangle)
        screen.blit(jab_text_surface, (275, 575))

        if fight_1:

            if test_hurt > 0:
                screen.blit(mermaidman_hurt, mermaidman_rectangle)
                test_hurt -= 0.1 

            else:
                screen.blit(mermaidman_surface, mermaidman_rectangle)

            display_player_health(player)
            display_player_stamina(player)
            display_enemy_health(mermaidman)

        elif fight_2: 

            if test_hurt > 0:
                screen.blit(ringmaster_hurt, ringmaster_rectangle)
                test_hurt -= 0.1

            else:
                screen.blit(ringmaster_surface, ringmaster_rectangle)

            display_player_health(player)
            display_player_stamina(player)
            display_enemy_health(ringmaster)

        elif fight_3:

            if test_hurt > 0:
                screen.blit(foxy_hurt, foxy_rectangle)
                test_hurt -= 0.1

            else:
                screen.blit(foxy_surface, foxy_rectangle)

            display_player_health(player)
            display_player_stamina(player)
            display_enemy_health(foxy)

        elif game_won:

            screen.fill('aqua')
            screen.blit(win_surface, win_rectangle)
            screen.blit(restart_surface, restart_rectangle)

    else:

        screen.fill('aqua')
        screen.blit(game_over_surface, game_over_rectanlge)
        screen.blit(restart_surface, restart_rectangle)

    pygame.display.update()
    clock.tick(60)



 