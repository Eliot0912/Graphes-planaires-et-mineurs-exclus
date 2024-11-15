import pygame
import sys

# Initialiser Pygame
pygame.init()

# Définir les dimensions de la fenêtre
ecran = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Modèle de Circuit et Voiture 2D")

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)

class Circuit:
    def __init__(self, x, y, largeur_exterieure, hauteur_exterieure, marge_interieure):
        self.rect_exterieur = pygame.Rect(x, y, largeur_exterieure, hauteur_exterieure)
        self.rect_interieur = pygame.Rect(x + marge_interieure, y + marge_interieure, 
                                          largeur_exterieure - 2 * marge_interieure, hauteur_exterieure - 2 * marge_interieure)
        self.ligne_depart = pygame.Rect(x + largeur_exterieure // 2 - 5, y + hauteur_exterieure - 20, 10, 20)

    def dessiner(self, ecran):
        pygame.draw.rect(ecran, NOIR, self.rect_exterieur, 5)
        pygame.draw.rect(ecran, NOIR, self.rect_interieur, 5)
        pygame.draw.rect(ecran, ROUGE, self.ligne_depart)

    def get_start_position(self):
        return self.ligne_depart.centerx, self.ligne_depart.top

class Voiture:
    def __init__(self, x, y, largeur, hauteur, couleur):
        self.rect = pygame.Rect(x, y, largeur, hauteur)
        self.couleur = couleur
        self.vitesse = 5

    def dessiner(self, ecran):
        pygame.draw.rect(ecran, self.couleur, self.rect)

    def deplacer(self, touches, circuit):
        if touches[pygame.K_LEFT]:
            self.rect.x -= self.vitesse
            if self.rect.colliderect(circuit.rect_interieur) or not circuit.rect_exterieur.contains(self.rect):
                self.rect.x += self.vitesse
        if touches[pygame.K_RIGHT]:
            self.rect.x += self.vitesse
            if self.rect.colliderect(circuit.rect_interieur) or not circuit.rect_exterieur.contains(self.rect):
                self.rect.x -= self.vitesse
        if touches[pygame.K_UP]:
            self.rect.y -= self.vitesse
            if self.rect.colliderect(circuit.rect_interieur) or not circuit.rect_exterieur.contains(self.rect):
                self.rect.y += self.vitesse
        if touches[pygame.K_DOWN]:
            self.rect.y += self.vitesse
            if self.rect.colliderect(circuit.rect_interieur) or not circuit.rect_exterieur.contains(self.rect):
                self.rect.y -= self.vitesse

# Créer le circuit
circuit = Circuit(100, 100, 600, 400, 50)

# Récupérer la position de départ du circuit
start_x, start_y = circuit.get_start_position()

# Créer la voiture à la position de départ du circuit
voiture = Voiture(start_x - 25, start_y - 15, 50, 30, NOIR)  # Ajuster pour centrer la voiture sur la ligne de départ

# Boucle principale du jeu
en_cours = True
while en_cours:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            en_cours = False

    touches = pygame.key.get_pressed()
    voiture.deplacer(touches, circuit)

    # Remplir l'écran avec du blanc
    ecran.fill(BLANC)

    # Dessiner le circuit
    circuit.dessiner(ecran)

    # Dessiner la voiture
    voiture.dessiner(ecran)

    # Mettre à jour l'affichage
    pygame.display.flip()

pygame.quit()
sys.exit()