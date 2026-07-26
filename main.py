import src.project as proj
import src.display as disp
import src.scene as scene
from typing import Callable


def display_static_scene(scene: Callable):
    verteces, faces, surface_normals, surface_atributes, light_positions, light_atributes, focal_point_x, background_color, num_x, num_y, framerate = scene()
    rays = proj.compute_rays(num_x, num_y, focal_point_x)
    intersections = proj.compute_intersections(rays, verteces, faces)
    image = proj.compute_image(intersections, num_x, num_y, rays, verteces, light_positions, faces, surface_normals, surface_atributes, light_atributes, background_color)
    disp.display_images([image], framerate)


if __name__ == "__main__":
    display_static_scene(scene.simple_cube_scene)

