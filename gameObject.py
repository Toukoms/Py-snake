from audio import AudioManager
from pygame import sprite, image,font
from random import randrange
import pickle

pixel = 32

# Position x et y du joueur
class Block:

    def __init__(self, position_x, position_y):
        self.x_pos = position_x
        self.y_pos = position_y
        self.update_tile()
    
    def update_tile(self):
        self.x = self.x_pos*pixel
        self.y = self.y_pos*pixel

# Classe du nourriture
class Food(sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.x = randrange(10)
        self.y = randrange(15)
        self.block = Block(self.x, self.y)
        self.image = image.load("assets/food.png")

    def draw_food(self, fenetre):
        # Methode pour affiche l'image de la nourriture sur l'écran
        fenetre.blit(self.image, (self.block.x,self.block.y))

# Classe du serpent
class Snake(sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.body = [Block(5,13),Block(5,12),Block(5,11)]
        self.head = Block(5,10)
        self.direction = "haut"
        self.image_body = image.load("assets/body.png")
        self.image_head = image.load("assets/head_up.png")


    def update(self):

        old_head_x = self.head.x_pos
        old_head_y = self.head.y_pos

        if self.direction == "gauche":
            self.image_head = image.load("assets/head_left.png")
            self.head.x_pos -= 1
        elif self.direction == "droite":
            self.image_head = image.load("assets/head_rigth.png")
            self.head.x_pos += 1
        elif self.direction == "bas":
            self.image_head = image.load("assets/head_bottom.png")
            self.head.y_pos += 1
        elif self.direction == "haut":
            self.image_head = image.load("assets/head_up.png")
            self.head.y_pos -= 1

        self.head.update_tile()
        self.body.append(Block(old_head_x,old_head_y))
        
    def draw_snake(self, fenetre):

        # Methode pour afficher le corps du serpent
        for block in self.body:
            fenetre.blit(self.image_body, (block.x,block.y))
        # dessiner la tête
        fenetre.blit(self.image_head, (self.head.x, self.head.y))    

# Classe principale de jeu
class Game:

    def __init__(self):
        self.over = False
        self.initialising()
        self.generate_food()
        self.audio = AudioManager()
        self.audio.play('music')
        
    def initialising(self):
        self.score = 0
            
        try:
            self.score_max = self.lire_maxscore()
        except FileNotFoundError:
            self.ecrire_maxscore(0)
            self.score_max = self.lire_maxscore()
            
        self.is_playing = False
        self.snake = Snake()
        self.generate_food() 
        
    def reinitialising(self):
        self.audio.play('perdu')    
        self.over = True
        if self.score_max < self.score:
            self.score_max = self.score
            self.ecrire_maxscore(self.score_max)
        self.initialising()
                
    def ecrire_maxscore(self,data):
        with open("score.bin", "wb") as fichier:
            mon_pickler = pickle.Pickler(fichier)
            mon_pickler.dump(data)
            
    def lire_maxscore(self):
        with open("score.bin","rb") as fichier:
            contenu = pickle.Unpickler(fichier)
            return contenu.load()
        
    def draw_element(self, fenetre):
        self.food.draw_food(fenetre)
        self.snake.draw_snake(fenetre)

    def update(self):
        # mise à jour du serpent
        self.snake.update()
        self.check_collision()

    def generate_food(self):
        # est-ce que le food occupe la même case que le corps de snake
        self.food = Food()
        bad_pos = True
        while bad_pos:
            for place in self.snake.body:
                # est-ce qu'il occupe la même case
                if place.x_pos == self.food.block.x_pos and place.y_pos == self.food.block.y_pos:
                    self.food = Food()
                    continue
                bad_pos = False
                                
    def check_collision(self):
        # verifier si la tête du serpent occupent la même case que la nourriture
        if self.snake.head.x_pos == self.food.block.x_pos and self.snake.head.y_pos == self.food.block.y_pos:
            self.generate_food()
            self.score += 1
            self.audio.play('nourriture')
        else:
            self.snake.body.pop(0)

    def game_over(self, col, lin):
        # on verifie si le snake sort de la fenêtre
        if not 0 <= self.snake.head.x_pos < col or not 0 <= self.snake.head.y_pos < lin:
            self.reinitialising()
        for block in self.snake.body:
            if self.snake.head.x_pos == block.x_pos and self.snake.head.y_pos == block.y_pos:
                self.reinitialising()
        