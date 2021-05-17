# Créé par nmelocco, le 22/01/2021 en Python 3.4

import pygame
from game import Game
pygame.init()


#générer la fenêtre de notre jeu
pygame.display.set_caption("Outspeed")
screen = pygame.display.set_mode((1080, 720))


#importer charger l'arriere plan de notre jeu
background = pygame.image.load('bg.jpg')

#charger notre jeu
game = Game()


running = True


#boucle tant que cette condition est vrai
while running:

    #applooquer l'arriere plan de notre jeu
    screen.blit(background, (0, -200))

    #appliquer l'image de mon joueur
    screen.blit(game.player.image, game.player.rect)

    #actualiser la barre de vie du joueur
    game.player.update_health_bar(screen)

    #récuprérer les projectiles du joueur
    for projectile in game.player.all_projectiles:
        projectile.move()

    #récupérer les monstres de notre jeu
    for monster in game.all_monsters:
        monster.forward()
        monster.update_health_bar(screen)

    #appliquer l'ensemble des images de mon groupe de projectiles
    game.player.all_projectiles.draw(screen)

    #appliquer l'ensemble des images de mon groupe de monstre
    game.all_monsters.draw(screen)

    #verifier si le joueur souhaite aller à gauche ou à droite
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width< screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()


    print(game.player.rect.x)

    #mettre à jour l'ecran
    pygame.display.flip()

    #si le joueur ferme cette fenetre
    for event in pygame.event.get():
        #que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture du jeu")
        #detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            #detecter si la touche espace est enclenchée pour lancer notre projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False