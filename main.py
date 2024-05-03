import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 6, screen.get_height() / 2)
player_velocity = pygame.Vector2(0, 0)
gravity = 0.5
jump_strength = -10
fall_speed = 5

flappy_bird_png = pygame.image.load('./media/flappy-bird.png')

flappy_bird = pygame.transform.scale(flappy_bird_png, (65, 50))
flappy_bird_rect = flappy_bird.get_rect()

background_img = pygame.image.load('./media/background-level1.jpg')

background = pygame.transform.scale(background_img, (1280, 720))
background_img_rect = background.get_rect()

angle = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_velocity.y = jump_strength

    if player_velocity.y > 0:
        angle = 0
    else:
        angle = 45

    player_pos.y -= fall_speed

    keys = pygame.key.get_pressed()

    player_velocity.y += gravity

    player_pos += player_velocity

    player_pos.y = max(min(player_pos.y, screen.get_height() - flappy_bird_rect.height), 0)

    pygame.display.flip()

    dt = clock.tick(60) / 1000

    flappy_bird_rect.center = player_pos

    rotated_bird = pygame.transform.rotate(flappy_bird, angle)

    screen.blit(background, background_img_rect)
    screen.blit(rotated_bird, flappy_bird_rect)

pygame.quit()