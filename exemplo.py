import pygame

pygame.init()

# Janela
screen = pygame.display.set_mode((800, 600))

# Carregar imagens com transparência
player_img = pygame.image.load("big_m_still.png").convert_alpha()
map_img = pygame.image.load("Level_1.png").convert_alpha()

# Posições iniciais
player_x, player_y = 100, 100
map_x, map_y = 0, 0

# Criar máscaras
player_mask = pygame.mask.from_surface(player_img)
map_mask = pygame.mask.from_surface(map_img)

clock = pygame.time.Clock()

running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(map_img, (map_x, map_y))
    screen.blit(player_img, (player_x, player_y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= 5
    if keys[pygame.K_RIGHT]:
        player_x += 5
    if keys[pygame.K_UP]:
        player_y -= 5
    if keys[pygame.K_DOWN]:
        player_y += 5

    # Verificar colisão com máscara
    offset = (player_x - map_x, player_y - map_y)
    print(map_mask.overlap(player_mask, offset))

    if map_mask.overlap(player_mask, offset):
        print("Colisão!")


    # debug_surface = map_mask.to_surface(setcolor=(255, 0, 0), unsetcolor=(0, 0, 0, 0))
    # screen.blit(debug_surface, (map_x, map_y))
 
    # debug_surface2 = player_mask.to_surface(setcolor=(0, 255, 0), unsetcolor=(0, 0, 0, 0))
    # screen.blit(debug_surface2, (player_x, player_y))


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
