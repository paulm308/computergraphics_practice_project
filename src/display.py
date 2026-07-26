import pygame
import numpy as np
import imageio
from PIL import Image


def display_images(images, framerate, save_path):
    assert images != []
    pygame.init()
    width = len(images[0])
    height = len(images[0][0])
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    saved_frames = []
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
                screen.set_at((x, height - y - 1), tuple(color))

        if save_path is not None and frame_index < len(images):
            frame_arr = pygame.surfarray.array3d(screen).transpose(1, 0, 2)
            saved_frames.append(frame_arr.copy())

        pygame.display.flip()
        clock.tick(framerate)
        frame_index += 1

    pygame.quit()

    if save_path is not None:
        if len(saved_frames) == 1:
            Image.fromarray(saved_frames[0]).save(save_path)
        else:
            imageio.mimsave(save_path, saved_frames, fps=framerate)
