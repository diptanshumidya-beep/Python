import pygame
import random


pygame.init()



SPRITE_COLoR_CHANGE_EVENT = pygame.USEREVENT +1

BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT+2

Blue = pygame.Color('blue')

LightBlue = pygame.Color('lightblue')

DarkBlue = pygame.Color('darkblue')


YELLOW = pygame.Color('yellow')

Magenta = pygame.Color('magenta')


Orange= pygame.Color('orange')


White= pygame.Color('white')


class Sprite (pygame.sprite.Sprite):


    def __init__(self,color,height,width):

        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)

        self.rect = self.image.get_rect()

        self.velocity = [random.choice([-1,1]),random.choice([-1,1])]

    def update(self):

        self.rect.move_ip(self.velocity)

        boundary_hit  = False

        if self.rect.left <= 0 or self.rect.right>=500:
            self.velocity[0] = -self.velocity[0]
            boundary_hit  = True


        if self.rect.top <= 0 or self.rect.bottom>=400:
                    self.velocity[1] = -self.velocity[1]
                    boundary_hit  = True
        

        if boundary_hit:


            pygame.event.post(pygame.event.Event(SPRITE_COLoR_CHANGE_EVENT))


            pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE_EVENT))



    def change_color(self):

         self.image.fill


def change_background_color():

    global bg_color

    bg_color = random.choice([Blue, LightBlue, DarkBlue])


all_sprites_list = pygame.sprite.Group()

# Instantiate the sprite

sp1 = Sprite(White, 20, 30)

# Randomly position the sprite

sp1.rect.x = random.randint(0, 480)

sp1.rect.y = random.randint(0, 370)

# Add the sprite to the group

all_sprites_list.add(sp1)

# Create the game window

screen = pygame.display.set_mode((500, 400))

# Set the window title

pygame.display.set_caption("Boundary Sprite")

# Set the initial background color

bg_color = Blue

# Apply the background color

screen.fill(bg_color)

# Game loop control flag

exit = False

# Create a clock object to control frame rate

clock = pygame.time.Clock()

# Main game loop

while not exit:

# Event handling loop

    for event in pygame.event.get():

# If the window's close button is clicked, exit the game

        if event.type == pygame.QUIT:

            exit = True

# If the sprite color change event is triggered, change the sprite's color

        elif event.type == SPRITE_COLoR_CHANGE_EVENT:

            sp1.change_color()



        elif event.type == BACKGROUND_COLOR_CHANGE_EVENT:

            change_background_color()



    all_sprites_list.update()   


    screen.fill(bg_color)



    all_sprites_list.draw(screen)


    pygame.display.flip()



    clock.tick(240)



pygame.quit()