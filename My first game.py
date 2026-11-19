
import pygame

pygame.init()


screen = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Wildilife Informatioon Displya")


bg = pygame.transform.scale(pygame.image.load("background.png"), (500, 500))

tiger = pygame.transform.scale(pygame.image.load("tiger.png"), (220, 220))



heading = pygame.font.Font(None, 42).render("Wildlife Spotlight: Tiger", True, "black")

fact = pygame.font.Font(None, 28).render("Tigers are powerful wild cats.", True, "black")



runing = True


while runing:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            runing = False


    screen.blit(bg, (0, 0))

    screen.blit(tiger, (140, 110))

    screen.blit(heading, (55, 25))

    screen.blit(fact, (85, 420))



    pygame.display.flip()


pygame.quit()
