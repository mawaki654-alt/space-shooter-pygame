import random


class Personnage:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Joueur(Personnage):
    def __init__(self, x, y, pv = 5):
        super().__init__(x, y)
        self.pv = pv

    def tirer(self):
         x = self.x
         y = self.y
         vitesse = 5
         camp = "joueur"
         return Projectile(x, y, vitesse, camp)



class Ennemi(Personnage):
    def __init__(self, x, y):
        super().__init__(x, y)

    def tirer(self):
        x = self.x
        y = self.y
        vitesse = 5
        camp = "ennemi"
        return Projectile(x, y, vitesse, camp)



class Projectile():
    def __init__(self, x, y, vitesse, camp):
        self.x = x
        self.y = y
        self.vitesse = vitesse
        self.camp = camp

    def mouvement(self):
        if self.camp == "joueur":
                self.y -= self.vitesse
        elif self.camp == "ennemi":
                self.y += self.vitesse


class Jeu():
    def __init__(self, joueur):
        self.joueur = joueur
        self.ennemis = []
        self.projectiles = []
        self.score = 0
        self.lv = 1
        self.frames = 0

    def gerer_collision(self):
         projectiles_a_retirer = []
         ennemis_a_retirer = []
         for projectile in self.projectiles:
              if projectile.camp == "joueur":
                   for ennemis in self.ennemis:
                        if abs(projectile.x - ennemis.x) < 30 and abs(projectile.y - ennemis.y) < 30:
                             self.score += 1
                             projectiles_a_retirer.append(projectile)
                             ennemis_a_retirer.append(ennemis)
                             break
              elif projectile.camp == "ennemi":
                   if abs(projectile.x - self.joueur.x) < 30 and abs(projectile.y - self.joueur.y) < 30:
                        self.joueur.pv -= 1
                        projectiles_a_retirer.append(projectile)
                        if self.joueur.pv == 0:
                             print("Game Over")
                             

         for p in projectiles_a_retirer:
            self.projectiles.remove(p)
         for e in ennemis_a_retirer:
            self.ennemis.remove(e)

    def avancer(self):
        projectiles_retirer = []
        for projectile in self.projectiles:
             projectile.mouvement()
             if abs(projectile.y - 800) < 20 or abs(projectile.y - 0) < 20:
                projectiles_retirer.append(projectile)

        for p in projectiles_retirer: 
            self.projectiles.remove(p)

    def faire_apparaitre_ennemis(self):
        self.frames += 1
        if self.frames % 180 == 0:
             x_aleatoire = random.randint(0, 760)
             nouvel_ennemi = Ennemi(x_aleatoire, 50)
             self.ennemis.append(nouvel_ennemi)   

    def faire_tirer_ennemis(self):
         for ennemis in self.ennemis:
              if random.random() < 0.02:
                   self.projectiles.append(ennemis.tirer())  

         

                        