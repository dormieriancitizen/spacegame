import pygame, random
from math import sin, cos, pi
pygame.init()

# Set up the window
window_width = 1920
window_height = 1080
window = pygame.display.set_mode((window_width, window_height))

#Text
font = pygame.font.Font(None, 36)

# Load the background image
bg_image = pygame.image.load('assets/background.png').convert()
bg_image = pygame.transform.scale(bg_image, (5000, 5000))

# Load the player image
player_image = pygame.image.load('assets/player.png').convert_alpha()
player_image = pygame.transform.scale(player_image, (50, 50))

# Set up the clock
clock = pygame.time.Clock()

# Set up the player position and speed
player_x = bg_image.get_width()/2
player_y = bg_image.get_height()/2

player_rot = 0

player_xv = 0
player_yv = 0

player_speed = 5

#Particles
particles = []

particle_image = pygame.image.load('assets/particle.png').convert_alpha()
particle_image = pygame.transform.scale(particle_image, (50, 50))

class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = random.uniform(-0.5, 0.5)
        self.vy = random.uniform(-1, -0.5)
        self.life = 20

    
    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.life -= 1

        if self.life < 0:
            pass
    
    def draw(self, surface):
        surface.blit(particle_image, (0 - (player_x+self.x), 0 - (player_y+self.y)))


def draw():
    #For outlands
    window.fill((0, 0, 0))

    # Calculate the background position based on the player position

    # Draw the background
    window.blit(bg_image, (-player_x, -player_y))

    #Draw any particles
    for particle in particles:
        particle.draw(window)

    # Draw the player
    rotated_player_image = pygame.transform.rotate(player_image, player_rot)
    player_rect = rotated_player_image.get_rect(center=(window_width/2, window_height/2))
    window.blit(rotated_player_image, (window_width/2, window_height/2))

    #debug
    text = font.render(str(player_rot), True, (255, 255, 255))
    window.blit(text,(0,0))

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle input
    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        running = False
    
    if keys[pygame.K_a]:
        player_rot += player_speed
        player_rot = player_rot % 360
    if keys[pygame.K_d]:
        player_rot -= player_speed
        player_rot = player_rot % 360
    if keys[pygame.K_w]:
        player_yv -= sin(player_rot * pi / 180) * player_speed
        player_xv += cos(player_rot * pi / 180) * player_speed

        for i in range(5):
            particles.append(Particle(player_x, player_y))

    if keys[pygame.K_s]:
        player_yv = player_yv * 0.7
        player_xv = player_xv * 0.7

    player_y += player_yv
    player_x += player_xv

    player_yv = player_yv * 0.95
    player_xv = player_xv * 0.95

    # Draw the game
    
    draw()

    # Update the display
    pygame.display.update()

    # Cap the framerate
    clock.tick(60)

# Clean up
pygame.quit()
