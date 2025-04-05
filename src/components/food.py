from pygame import sprite, image
from random import randrange

from core.block import Block

# Classe du nourriture
class Food(sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.x = randrange(10)
        self.y = randrange(15)
        self.block = Block(self.x, self.y)
        self.image = image.load("src/assets/food.png")

    def draw_food(self, fenetre):
        # Methode pour affiche l'image de la nourriture sur l'écran
        fenetre.blit(self.image, (self.block.x,self.block.y))