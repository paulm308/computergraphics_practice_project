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
    r = obj.rotate((5., 5., 0.))
    s = obj.scale_and_mirror((2., 2., 2.))
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
    light_positions = [np.array([-1., 7., 0.])]
    light_atributes = [np.array([1., 1., 1.])]

    background_color = np.array([0., 0., 0.])

    # camera:
    focal_point_x = -1.
    width = 400
    height = 300
    framerate = 1

    return cube_verteces, cube_faces, cube_surface_normals, surface_atributes, light_positions, light_atributes, focal_point_x, background_color, width, height, framerate
