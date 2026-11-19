
import pygame


pygame.init()



screen = pygame.display.set_mode((500, 400))

pygame.display.set_caption("Mini Sprite Adventure")



x, y = 50, 50

speed = 4

runing = True




while runing:

    for event in pygame.event.get():


        if event.type == pygame.QUIT:

            runing = False


    keys = pygame.key.get_pressed()

    x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * speed

    y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * speed




    x = max(0, min(x, 440))

    y = max(0, min(y, 340))



    colour = "white"

    if x == 0: colour = "blue"

    elif x == 440: colour = "yellow"

    elif y == 0: colour = "red"

    elif y == 340: colour = "green"




    screen.fill("black")

    pygame.draw.circle(screen, "green", (420, 320), 35)

    pygame.draw.circle(screen, "blue", (80, 320), 35, 4)

    pygame.draw.rect(screen, colour, (x, y, 60, 60))




    pygame.display.flip()



pygame.quit()
