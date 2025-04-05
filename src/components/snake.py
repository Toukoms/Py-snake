from pygame import sprite, image

from core.block import Block

# Classe du serpent
class Snake(sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.body = [Block(5,13),Block(5,12),Block(5,11)]
        self.head = Block(5,10)
        self.direction = "haut"
        self.image_body = image.load("src/assets/body.png")
        self.image_head = image.load("src/assets/head_up.png")


    def update(self):

        old_head_x = self.head.x_pos
        old_head_y = self.head.y_pos

        if self.direction == "gauche":
            self.image_head = image.load("src/assets/head_left.png")
            self.head.x_pos -= 1
        elif self.direction == "droite":
            self.image_head = image.load("src/assets/head_rigth.png")
            self.head.x_pos += 1
        elif self.direction == "bas":
            self.image_head = image.load("src/assets/head_bottom.png")
            self.head.y_pos += 1
        elif self.direction == "haut":
            self.image_head = image.load("src/assets/head_up.png")
            self.head.y_pos -= 1

        self.head.update_tile()
        self.body.append(Block(old_head_x,old_head_y))
        
    def draw_snake(self, fenetre):

        # Methode pour afficher le corps du serpent
        for block in self.body:
            fenetre.blit(self.image_body, (block.x,block.y))
        # dessiner la tête
        fenetre.blit(self.image_head, (self.head.x, self.head.y))    
