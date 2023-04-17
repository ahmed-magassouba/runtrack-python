import pygame 
from pygame.locals import *
from sys import exit
from random import randint

FPS = 60
framePerSec = pygame.time.Clock()

# Predefined some colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)

# Screen information
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)


# Load the images
# X_IMAGE = pygame.image.load("X.png").convert_alpha()
# O_IMAGE = pygame.image.load("O.png").convert_alpha()
# X_IMAGE = pygame.transform.scale(X_IMAGE, (200, 200))
# O_IMAGE = pygame.transform.scale(O_IMAGE, (200, 200))

# Create the board
# board = [[0, 0, 0],
#             [0, 0, 0],
#             [0, 0, 0]]


class Board :

    def __init__(self,screen):
        self.screen = screen

        #les ligne de la grille
        self.board = [((200,0),(200,600)),
                      ((400,0),(400,600)),
                      ((0,200),(600,200)),
                      ((0,400),(600,400))]
        
        #on initie la grille
        self.array_board = [[None for i in range(0,3)] for j in range(0,3)]

    #print de la grille
    def print_board(self):
        print(self.array_board)
        
    # fonction pour dessiner la grille     
    def draw_board(self):
        for line in self.board:
            pygame.draw.line(self.screen,GREY,line[0], line[1],5)

    def fixer_la_valeur(self,x,y,value):
        self.array_board[y][x] = value



class Game :

    def __init__(self):

        self.screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
        pygame.display.set_caption("TicTacToe1337")
        self.InGame = True
        self.screen.fill(WHITE)
        self.board = Board(self.screen)
        self.player = 1
        self.compteur = 0
        self.game_over = False


    def functionPrincipale(self):
        
        while self.InGame:
            for event in pygame.event.get():

                #si l'utilisateur clique sur la croix pour fermer la fenetre
                if event.type == QUIT:
                    self.InGame = False
                    pygame.quit()
                    exit()

                #si l'utilisateur clique sur le boutton droit de la souris
                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                    if not self.game_over:

                        #on recupere les coordonnées de la souris
                        mouse_x, mouse_y = pygame.mouse.get_pos()

                        #on recupere les coordonnées de la case
                        #le symbole // correspond a la division entière
                        case_x = mouse_x // 200
                        case_y = mouse_y // 200

                        #on dessine le X ou le O
                        if self.player == 1:
                            pygame.draw.line(self.screen,RED,(case_x*200+15,case_y*200+15),(case_x*200+185,case_y*200+185),35)
                            pygame.draw.line(self.screen,RED,(case_x*200+15,case_y*200+185),(case_x*200+185,case_y*200+15),35)
                            self.player = 2
                        else:
                            pygame.draw.circle(self.screen,BLUE,(case_x*200+100,case_y*200+100),85,35)
                            self.player = 1

                        #on met a jour la grille
                        self.board.fixer_la_valeur(case_x,case_y,'X' if self.compteur % 2 == 0 else 'O')

                        self.compteur += 1




            #             #on verifie si le joueur a gagné
            #             self.check_win()
            #             #on met a jour l'affichage
            #             pygame.display.flip()
            #             framePerSec.tick(FPS)
            #         else:
            #             self.reset()
            #             self.game_over = False

            # self.screen.fill(WHITE)
            self.board.print_board()
            self.board.draw_board()  
          
            pygame.display.flip() 

if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.functionPrincipale()
    pygame.quit()



    
       






