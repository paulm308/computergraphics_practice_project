import pygame
import numpy as np


def display_images(images, framerate):
    assert images != []
    pygame.init()
    width = len(images[0])
    height = len(images[0][0])
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    running = True
    frame_index = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if not running:
            break

        image = images[frame_index % len(images)]
        for x in range(width):
            for y in range(height):
                color = np.clip(np.array(image[x][y]) * 255, 0, 255).astype(int)
                screen.set_at((x, y), tuple(color))

        pygame.display.flip()
        clock.tick(framerate)
        frame_index += 1

    pygame.quit()
