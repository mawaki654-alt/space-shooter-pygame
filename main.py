import pygame
import random
from classes import Personnage, Joueur, Ennemi, Projectile, Jeu  # importe nos classes depuis classes.py

pygame.init()  # démarre les modules internes de Pygame

LARGEUR, HAUTEUR = 800, 800  # taille de la fenêtre en pixels
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))  # crée la fenêtre
pygame.display.set_caption("Mon Space Shooter")         # titre affiché en haut de la fenêtre

horloge = pygame.time.Clock()  # sert à limiter la vitesse de la boucle (FPS)

joueur = Joueur(300, 550)  # crée le joueur à la position x=300, y=550
jeu = Jeu(joueur)          # crée la partie et lui donne le joueur

en_cours = True  # tant que c'est True, le jeu tourne
police = pygame.font.Font(None, 36)  # crée une police de taille 36

while en_cours:  # boucle principale : une itération = une frame
    for event in pygame.event.get():  # parcourt les événements de cette frame (clavier, souris, fermeture...)
        if event.type == pygame.QUIT:       # clic sur la croix de la fenêtre
            en_cours = False                # arrête la boucle principale
        elif event.type == pygame.KEYDOWN:  # une touche vient d'être pressée (une seule fois, pas en continu)
            if event.key == pygame.K_SPACE:                  # si c'est la barre espace
                jeu.projectiles.append(joueur.tirer())       # le joueur crée un projectile, on l'ajoute à la liste
    touches = pygame.key.get_pressed()  # état de toutes les touches

    fenetre.fill((128, 128, 128))  # efface l'écran avec du gris
    jeu.avancer()                  # fait avancer les projectiles et retire ceux sortis de l'écran
    jeu.gerer_collision()          # vérifie les touches : score, PV, suppressions
    if joueur.pv <= 0:         # si le joueur n'a plus de PV
        en_cours = False           # arrête la boucle principale apres perte des PV 
    jeu.faire_apparaitre_ennemis() # fait apparaître un ennemi toutes les 180 frames
    jeu.faire_tirer_ennemis()      # chaque ennemi a 2% de chance de tirer à chaque frame
    pygame.draw.rect(fenetre, (50, 50, 50), (joueur.x, joueur.y, 40, 40))  # dessine le joueur (carré gris foncé 40x40)
    for ennemi in jeu.ennemis:  # pour chaque ennemi en vie...
        pygame.draw.rect(fenetre, (200, 200, 200), (ennemi.x, ennemi.y, 40, 40))  # ...dessine un carré gris clair
    for projectile in jeu.projectiles:  # pour chaque projectile actif...
        pygame.draw.rect(fenetre, (255, 255, 255), (projectile.x, projectile.y, 5, 10))  # ...dessine un petit rectangle blanc

    texte_score = police.render(f"Score: {jeu.score}", True, (255,255,255))  # crée le texte du score
    fenetre.blit(texte_score, (10, 10))  # affiche le score en haut à gauche
    texte_pv = police.render(f"PV: {joueur.pv}", True, (255,255,255))  # crée le texte du PV
    fenetre.blit(texte_pv, (10, 45))  # affiche le PV en haut à gauche

    pygame.display.flip()  # affiche tout ce qui vient d'être dessiné
    horloge.tick(60)       # limite le jeu à 60 images par seconde

    if touches[pygame.K_LEFT]:   # flèche gauche maintenue
        joueur.x -= 5            # le joueur recule de 5 pixels
    if touches[pygame.K_RIGHT]:  # flèche droite maintenue
        joueur.x += 5            # le joueur avance de 5 pixels
    joueur.x = max(0, min(joueur.x, 760))  # empêche le joueur de sortir de l'écran 

if joueur.pv <= 0:  # si le joueur n'a plus de PV
     Game_over = police.render("Game Over", True, (255, 0, 0))  # crée le texte "Game Over" en rouge
     fenetre.fill((0, 0, 0))  # efface l'écran avec du noir
     texte_score_final = police.render(f"Score final: {jeu.score}", True, (255, 255, 255))  # crée le texte du score final en blanc 
     fenetre.blit(texte_score_final, (300, 350))  # affiche le score final au centre de l'écran
     fenetre.blit(Game_over, (310,400))
     pygame.display.flip()  # affiche le texte 
     pygame.time.delay(3000)  # attend 3 secondes


pygame.quit()  # ferme proprement Pygame quand la boucle est terminée