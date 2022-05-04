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