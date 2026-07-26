import pygame


def display_images(images, framerate):
    assert images != []
    pygame.init()
    screen = pygame.display.set_mode((len(images[0]), len(images[0][0])))
    clock = pygame.time.Clock()

    image = images.pop(0)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                return

    for x in range(len(image)):
        for y in range(len(image[x])):
            screen.set_at((x, y), image[x][y])

    pygame.display.flip()
    clock.tick(framerate)
