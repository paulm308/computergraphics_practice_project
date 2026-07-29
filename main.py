import src.project as proj
import src.display as disp
import src.scene as scene
from typing import Callable
from tqdm import tqdm


def display_static_scene(scene: Callable):
    verteces, surface_normals, faces, surface_atributes, light_positions, light_atributes, indirect_light, focal_point_x, background_color, num_x, num_y, framerate, save_path = scene()
    rays = proj.compute_rays(num_x, num_y, focal_point_x)
    intersections = proj.compute_intersections_parallel(rays, verteces, faces, 8)
    image = proj.compute_image_parallel(intersections, num_x, num_y, rays, verteces, light_positions, faces, surface_normals, surface_atributes, light_atributes, background_color, indirect_light, 8)
    disp.display_images([image], framerate, save_path)


def display_dynamic_scene(scene: Callable):
    scene_frames, background_color, num_x, num_y, framerate, save_path = scene()
    images = []
    for i in tqdm(range(len(scene_frames))):
        verteces, surface_normals, faces, surface_atributes, light_positions, light_atributes, indirect_light, focal_point_x = scene_frames[i]
        rays = proj.compute_rays(num_x, num_y, focal_point_x)
        intersections = proj.compute_intersections(rays, verteces, faces)
        image = proj.compute_image(intersections, num_x, num_y, rays, verteces, light_positions, faces, surface_normals, surface_atributes, light_atributes, background_color, indirect_light)
        images.append(image)
    disp.display_images(images, framerate, save_path)


if __name__ == "__main__":
    display_static_scene(scene.special_scene)
