import pickle

class ScoreManager:
    
    def __init__(self):
        self.score = self.init_score()
            
        try:
            self.score_max = self.lire_maxscore()
        except FileNotFoundError:
            self.ecrire_maxscore(0)
            self.score_max = self.lire_maxscore()
            
    def init_score(self):
        self.score = 0
            
    def ecrire_maxscore(self,data):
        with open("score.max", "wb") as fichier:
            mon_pickler = pickle.Pickler(fichier)
            mon_pickler.dump(data)
            
    def lire_maxscore(self):
        with open("score.max","rb") as fichier:
            contenu = pickle.Unpickler(fichier)
            return contenu.load()