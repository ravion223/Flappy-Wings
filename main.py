import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
speed = [2, 2]
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

flappy_bird = pygame.image.load('./media/flappy-bird.png')
flappy_bird_rect = flappy_bird.get_rect()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    flappy_bird_rect = flappy_bird_rect.move(speed)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    pygame.display.flip()

    dt = clock.tick(60) / 1000

    screen.fill("light blue")
    screen.blit(screen, flappy_bird_rect)

pygame.quit()