from components.food import Food
from components.snake import Snake
from core.audio import AudioManager
from core.score import ScoreManager

# Classe principale de jeu
class GameManager:

    def __init__(self):
        self.over = False
        self.score_manager = ScoreManager()
        self.initializing()
        self.audio = AudioManager()
        self.audio.play('music')
        
    def initializing(self):
        self.score_manager.init_score()
        self.snake = Snake()
        self.generate_food()
        self.is_playing = False
    
    def reinitializing(self):
        self.audio.play('perdu')    
        self.over = True
        if self.score_manager.score_max < self.score_manager.score:
            self.score_manager.score_max = self.score_manager.score
            self.score_manager.ecrire_maxscore(self.score_manager.score_max)
        self.initializing()
        
    def draw_element(self, fenetre):
        self.food.draw_food(fenetre)
        self.snake.draw_snake(fenetre)

    def update(self):
        # mise à jour du serpent
        self.snake.update()
        self.check_collision()

    def generate_food(self):
        self.food = Food()
        bad_pos = len(self.snake.body)
        while bad_pos >= 0:
            for place in self.snake.body:
                # est-ce que le food occupe la même case que le corps de snake
                if place.x_pos == self.food.block.x_pos and place.y_pos == self.food.block.y_pos:
                    self.food = Food()
                    break
                bad_pos -= 1
            if bad_pos >= 1:
                bad_pos = len(self.snake.body)
                                
    def check_collision(self):
        # verifier si la tête du serpent occupent la même case que la nourriture
        if self.snake.head.x_pos == self.food.block.x_pos and self.snake.head.y_pos == self.food.block.y_pos:
            self.generate_food()
            self.score_manager.score += 1
            self.audio.play('nourriture')
        else:
            self.snake.body.pop(0)

    def game_over(self, col, lin):
        # on verifie si le snake sort de la fenêtre
        if not 0 <= self.snake.head.x_pos < col or not 0 <= self.snake.head.y_pos < lin:
            self.reinitializing()
        for block in self.snake.body:
            if self.snake.head.x_pos == block.x_pos and self.snake.head.y_pos == block.y_pos:
                self.reinitializing()
        
