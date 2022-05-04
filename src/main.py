from game_manager import GameManager  
from pygame import display, draw, event, init,time, font
from pygame.locals import *

# Initialisation de pygame
init()

# Les variables
COL = 15
LIN = 20
PIX = 32
game_manager = GameManager()
TIMER = USEREVENT
time.set_timer(TIMER, 200)

def afficher_ligne():
    for x in range(0,COL):
        for y in range(0, LIN):
            draw.rect(fenetre, (0,0,0), (x*PIX,y*PIX,PIX,PIX), width=1)

n = 2
# Création de fenêtre
fenetre = display.set_mode((COL*PIX,LIN*PIX))
display.set_caption(f"Snake2 {n}")
# font de texte à affiche
font_text = font.SysFont("monospace", 18)
font_game_over = font.SysFont("Ravie", 30)
# Texte à affiche
text_game_over = font_game_over.render("Game Over", 1, (255,25,25))
pause = font_text.render("Appuyer sur ESPACE pour continuer...", 1, (0,0,0))

# Le boucle principale (Mainloop)
Run = True
while Run:
    
    display.set_caption(f"Snake2                                Score max : {game_manager.score_manager.score_max} | Score : {game_manager.score_manager.score}", "src/assets/icon_snake.ico")
    
    # La couleur de fenêtre (Blanc)
    fenetre.fill((0,255,20))

    # dessiner les elements de jeu
    game_manager.draw_element(fenetre)

    # Quand le jeu est en pause ou game_over
    if game_manager.is_playing == False:
        fenetre.blit(pause, (2*PIX, 9*PIX))
        
    if game_manager.over:
        fenetre.blit(text_game_over, (5*PIX,3*PIX))

    # Pour le maket on affiche la ligne et la colone
    # afficher_ligne()

    # Gestion d'évenement
    for e in event.get():

        if e.type == QUIT:
            if game_manager.score_manager.score > game_manager.score_manager.score_max:
                game_manager.ecrire_maxscore(game_manager.score_manager.score)
            Run = False
        
        if e.type == KEYDOWN:
            
            if game_manager.is_playing:
                if e.key == K_RIGHT and game_manager.snake.direction != "gauche" :
                    game_manager.snake.direction = "droite"
                    break
                elif e.key == K_LEFT and game_manager.snake.direction != "droite" :
                    game_manager.snake.direction = "gauche"
                    break
                elif e.key == K_DOWN and game_manager.snake.direction != "haut" :
                    game_manager.snake.direction = "bas"
                    break
                elif e.key == K_UP and game_manager.snake.direction != "bas" :
                    game_manager.snake.direction = "haut"
                    break

            if e.key == K_SPACE:
                if game_manager.is_playing == True:
                    game_manager.is_playing = False
                else:
                    game_manager.is_playing = True
                    game_manager.over = False
            
        elif e.type == TIMER:
            
            if game_manager.is_playing == True:
                    game_manager.update()
            game_manager.game_over(COL,LIN)

    # Actualisation de fenêtre
    display.flip()

quit()
