import src.generate_objects as obj
import numpy as np


def simple_cube_scene():
    # compute transformed cube (no viewtransform camara is assumed to be at 0, 0, 0)
    cube_verteces, cube_faces, cube_surface_normals = obj.generate_cube()

    cube_verteces = obj.convert_to_homogeneous_vertex(cube_verteces)
    cube_verteces = obj.convert_to_numpy(cube_verteces)
    cube_surface_normals = obj.convert_to_homogeneous_vector(cube_surface_normals)
    cube_surface_normals = obj.convert_to_numpy(cube_surface_normals)

    t1 = obj.translate((-0.5, -0.5, -0.5))
    r = obj.rotate((30., 30., 30.))
    s = obj.scale_and_mirror((4., 4., 4.))
    t2 = obj.translate((7., 0., 0.))
    m = t2 @ s @ r @ t1

    nr = obj.normal_matrix(r)
    ns = obj.normal_matrix(s)
    nm = ns @ nr

    cube_verteces = [obj.clean(m @ vertex.T) for vertex in cube_verteces]
    cube_verteces = obj.convert_to_cartesians(cube_verteces)
    cube_surface_normals = [obj.clean(nm @ surface_normal.T) for surface_normal in cube_surface_normals]
    cube_surface_normals = obj.convert_to_cartesians(cube_surface_normals)
    cube_surface_normals = [obj.normalize(surface_normal) for surface_normal in cube_surface_normals]

    # colors and materials
    surface_atributes = [[np.array([0., 0., 1.]), 1 / np.pi, 1 / np.pi, 1 / np.pi, 8],
                         [np.array([0., 0., 1.]), 1 / np.pi, 1 / np.pi, 1 / np.pi, 8],
                         [np.array([0., 1., 1.]), 1 / np.pi, 1 / np.pi, 1 / np.pi, 8],
                         [np.array([0., 1., 1.]), 1 / np.pi, 1 / np.pi, 1 / np.pi, 8],
                         [np.array([0., 1., 0.]), 1 / np.pi, 1 / np.pi, 1 / np.pi, 8],
                         [np.array([0., 1., 0.]), 1 / np.pi, 1 / np.pi, 1 / np.pi, 8],
                         [np.array([1., 1., 0.]), 1 / np.pi, 1 / np.pi, 1 / np.pi, 8],
                         [np.array([1., 1., 0.]), 1 / np.pi, 1 / np.pi, 1 / np.pi, 8],
                         [np.array([1., 0., 1.]), 1 / np.pi, 1 / np.pi, 1 / np.pi, 8],
                         [np.array([1., 0., 1.]), 1 / np.pi, 1 / np.pi, 1 / np.pi, 8],
                         [np.array([1., 0., 0.]), 1 / np.pi, 1 / np.pi, 1 / np.pi, 8],
                         [np.array([1., 0., 0.]), 1 / np.pi, 1 / np.pi, 1 / np.pi, 8]]

    # lights:
    light_positions = [np.array([-1., 0., 0.])]
    light_atributes = [np.array([1., 1., 1.])]
    indirect_light = [np.array([.3, .3, .3])]
    background_color = np.array([0., 0., 0.])

    # camera:
    focal_point_x = -1.
    width = 400
    height = 300
    framerate = 1
    save_path = "static_output.png"

    return cube_verteces, cube_surface_normals, cube_faces, surface_atributes, light_positions, light_atributes, indirect_light, focal_point_x, background_color, width, height, framerate, save_path


def dynamic_cube_scene():
    # compute transformed cube (no viewtransform camara is assumed to be at 0, 0, 0)
    cube_verteces, cube_faces, cube_surface_normals = obj.generate_cube()

    cube_verteces = obj.convert_to_homogeneous_vertex(cube_verteces)
    cube_verteces = obj.convert_to_numpy(cube_verteces)
    cube_surface_normals = obj.convert_to_homogeneous_vector(cube_surface_normals)
    cube_surface_normals = obj.convert_to_numpy(cube_surface_normals)

    t1 = obj.translate((-0.5, -0.5, -0.5))
    s = obj.scale_and_mirror((4., 4., 4.))
    t2 = obj.translate((7., 0., 0.))
    ns = obj.normal_matrix(s)

    scene_frames = []
    for i in range(36):

        r_i = obj.rotate((i * 10., i * 10., i * 10.))
        m = t2 @ s @ r_i @ t1

        nr_i = obj.normal_matrix(r_i)
        nm = ns @ nr_i

        cube_verteces_i = [obj.clean(m @ vertex.T) for vertex in cube_verteces]
        cube_verteces_i = obj.convert_to_cartesians(cube_verteces_i)
        cube_surface_normals_i = [obj.clean(nm @ surface_normal.T) for surface_normal in cube_surface_normals]
        cube_surface_normals_i = obj.convert_to_cartesians(cube_surface_normals_i)
        cube_surface_normals_i = [obj.normalize(surface_normal) for surface_normal in cube_surface_normals_i]
        scene_frames.append([cube_verteces_i, cube_surface_normals_i])

    # colors and materials
    surface_atributes = [[np.array([0., 0., 1.]), 1 / np.pi, 1 / np.pi, 1 / np.pi, 8],
                         [np.array([0., 0., 1.]), 1 / np.pi, 1 / np.pi, 1 / np.pi, 8],
                         [np.array([0., 1., 1.]), 1 / np.pi, 1 / np.pi, 1 / np.pi, 8],
                         [np.array([0., 1., 1.]), 1 / np.pi, 1 / np.pi, 1 / np.pi, 8],
                         [np.array([0., 1., 0.]), 1 / np.pi, 1 / np.pi, 1 / np.pi, 8],
                         [np.array([0., 1., 0.]), 1 / np.pi, 1 / np.pi, 1 / np.pi, 8],
                         [np.array([1., 1., 0.]), 1 / np.pi, 1 / np.pi, 1 / np.pi, 8],
                         [np.array([1., 1., 0.]), 1 / np.pi, 1 / np.pi, 1 / np.pi, 8],
                         [np.array([1., 0., 1.]), 1 / np.pi, 1 / np.pi, 1 / np.pi, 8],
                         [np.array([1., 0., 1.]), 1 / np.pi, 1 / np.pi, 1 / np.pi, 8],
                         [np.array([1., 0., 0.]), 1 / np.pi, 1 / np.pi, 1 / np.pi, 8],
                         [np.array([1., 0., 0.]), 1 / np.pi, 1 / np.pi, 1 / np.pi, 8]]

    # lights:
    light_positions = [np.array([-1., 0., 0.])]
    light_atributes = [np.array([1., 1., 1.])]
    indirect_light = [np.array([.3, .3, .3])]
    background_color = np.array([0., 0., 0.])

    # camera:
    focal_point_x = -1.
    width = 400
    height = 300
    framerate = 12

    save_path = "dynamic_output.mp4"

    for i in range(len(scene_frames)):
        scene_frames[i] += [cube_faces, surface_atributes, light_positions, light_atributes, indirect_light, focal_point_x]
    return scene_frames, background_color, width, height, framerate, save_path
