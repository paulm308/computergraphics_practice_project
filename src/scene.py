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


def room_scene():
    # create the room
    room_verteces, room_faces, room_surface_normals = obj.generate_cube()

    # cutout invisible faces
    room_faces = room_faces[:2] + room_faces[4:8] + room_faces[10:]
    room_surface_normals = room_surface_normals[:2] + room_surface_normals[4:8] + room_surface_normals[10:]

    # invert cube
    room_surface_normals = [(-surface_normal[0], -surface_normal[1], -surface_normal[2]) for surface_normal in room_surface_normals]

    # translate and scale
    room_verteces = obj.convert_to_homogeneous_vertex(room_verteces)
    room_verteces = obj.convert_to_numpy(room_verteces)
    room_surface_normals = obj.convert_to_homogeneous_vector(room_surface_normals)
    room_surface_normals = obj.convert_to_numpy(room_surface_normals)

    tr1 = obj.translate((-0.5, -0.5, -0.5))
    sr = obj.scale_and_mirror((8., 6., 6.))
    tr2 = obj.translate((4., 0., 0.))
    mr = tr2 @ sr @ tr1
    nrs = obj.normal_matrix(sr)

    room_verteces = [obj.clean(mr @ vertex.T) for vertex in room_verteces]
    room_verteces = obj.convert_to_cartesians(room_verteces)
    room_surface_normals = [obj.clean(nrs @ surface_normal.T) for surface_normal in room_surface_normals]
    room_surface_normals = obj.convert_to_cartesians(room_surface_normals)
    room_surface_normals = [obj.normalize(surface_normal) for surface_normal in room_surface_normals]

    verteces = room_verteces.copy()
    surface_normals = room_surface_normals.copy()
    faces = room_faces.copy()
    # create right lightbox
    rl_verteces, rl_faces, rl_surface_normals = obj.generate_cube()

    # cutout invisible faces
    rl_faces = rl_faces[2:]
    rl_surface_normals = rl_surface_normals[2:]

    # invert cube
    rl_surface_normals = [(-surface_normal[0], -surface_normal[1], -surface_normal[2]) for surface_normal in rl_surface_normals]

    # romove duplicate verteces
    rl_verteces = rl_verteces[:5] + rl_verteces[6:]

    # update faces
    updated_rl_faces = []
    for face in rl_faces:
        updated_face = list(face)
        for i, vertex_idx in enumerate(face):
            if vertex_idx < 5:
                updated_face[i] = vertex_idx + len(verteces)
            elif vertex_idx == 5:
                updated_face[i] = 7
            else:
                updated_face[i] = vertex_idx + len(verteces) - 1
        updated_rl_faces.append(tuple(updated_face))
    rl_faces = updated_rl_faces

    # translate and scale
    rl_verteces = obj.convert_to_homogeneous_vertex(rl_verteces)
    rl_verteces = obj.convert_to_numpy(rl_verteces)
    rl_surface_normals = obj.convert_to_homogeneous_vector(rl_surface_normals)
    rl_surface_normals = obj.convert_to_numpy(rl_surface_normals)

    trl1 = obj.translate((-0.5, -0.5, -0.5))
    srl = obj.scale_and_mirror((1., 0.5, 1.))
    trl2 = obj.translate((7.5, 3.25, 2.5))
    mrl = trl2 @ srl @ trl1
    nrls = obj.normal_matrix(srl)

    rl_verteces = [obj.clean(mrl @ vertex.T) for vertex in rl_verteces]
    rl_verteces = obj.convert_to_cartesians(rl_verteces)
    rl_surface_normals = [obj.clean(nrls @ surface_normal.T) for surface_normal in rl_surface_normals]
    rl_surface_normals = obj.convert_to_cartesians(rl_surface_normals)
    rl_surface_normals = [obj.normalize(surface_normal) for surface_normal in rl_surface_normals]

    verteces += rl_verteces
    surface_normals += rl_surface_normals
    faces += rl_faces

    # create left lightbox
    ll_verteces, ll_faces, ll_surface_normals = obj.generate_cube()

    # cutout invisible faces
    ll_faces = ll_faces[2:]
    ll_surface_normals = ll_surface_normals[2:]

    # invert cube
    ll_surface_normals = [(-surface_normal[0], -surface_normal[1], -surface_normal[2]) for surface_normal in ll_surface_normals]
    # romove duplicate verteces
    ll_verteces = ll_verteces[:4] + ll_verteces[5:]

    # update faces
    updated_ll_faces = []
    for face in ll_faces:
        updated_face = list(face)
        for i, vertex_idx in enumerate(face):
            if vertex_idx < 4:
                updated_face[i] = vertex_idx + len(verteces)
            elif vertex_idx == 4:
                updated_face[i] = 6
            else:
                updated_face[i] = vertex_idx + len(verteces) - 1
        updated_ll_faces.append(tuple(updated_face))
    ll_faces = updated_ll_faces

    # translate and scale
    ll_verteces = obj.convert_to_homogeneous_vertex(ll_verteces)
    ll_verteces = obj.convert_to_numpy(ll_verteces)
    ll_surface_normals = obj.convert_to_homogeneous_vector(ll_surface_normals)
    ll_surface_normals = obj.convert_to_numpy(ll_surface_normals)

    tll1 = obj.translate((-0.5, -0.5, -0.5))
    sll = obj.scale_and_mirror((1., 0.5, 1.))
    tll2 = obj.translate((7.5, 3.25, -2.5))
    mll = tll2 @ sll @ tll1
    nlls = obj.normal_matrix(sll)

    ll_verteces = [obj.clean(mll @ vertex.T) for vertex in ll_verteces]
    ll_verteces = obj.convert_to_cartesians(ll_verteces)
    ll_surface_normals = [obj.clean(nlls @ surface_normal.T) for surface_normal in ll_surface_normals]
    ll_surface_normals = obj.convert_to_cartesians(ll_surface_normals)
    ll_surface_normals = [obj.normalize(surface_normal) for surface_normal in ll_surface_normals]

    verteces += ll_verteces
    surface_normals += ll_surface_normals
    faces += ll_faces

    # create ceiling
    ceiling_faces = [(2, 3, 9),
                     (2, 9, 15),
                     (12, 13, 16),
                     (12, 16, 19)]
    ceiling_surface_normals = [(0., -1., 0.),
                               (0., -1., 0.),
                               (0., -1., 0.),
                               (0., -1., 0.)]
    ceiling_surface_normals = obj.convert_to_numpy(ceiling_surface_normals)

    surface_normals += ceiling_surface_normals
    faces += ceiling_faces

    # create tall box
    tb_verteces, tb_faces, tb_surface_normals = obj.generate_cube()

    # cutout invisible faces
    tb_faces = tb_faces[2:10]
    tb_surface_normals = tb_surface_normals[2:10]

    # update faces
    updated_tb_faces = []
    for face in tb_faces:
        updated_face = list(face)
        for i, vertex_idx in enumerate(face):
            updated_face[i] = vertex_idx + len(verteces)
        updated_tb_faces.append(tuple(updated_face))
    tb_faces = updated_tb_faces

    # translate and scale
    tb_verteces = obj.convert_to_homogeneous_vertex(tb_verteces)
    tb_verteces = obj.convert_to_numpy(tb_verteces)
    tb_surface_normals = obj.convert_to_homogeneous_vector(tb_surface_normals)
    tb_surface_normals = obj.convert_to_numpy(tb_surface_normals)

    ttb1 = obj.translate((-0.5, -0.5, -0.5))
    rtb = obj.rotate((0., 30., 0.))
    stb = obj.scale_and_mirror((1., 3., 1.))
    ttb2 = obj.translate((6., -1.5, 1.))
    nrtb = obj.normal_matrix(rtb)
    nstb = obj.normal_matrix(stb)
    mtb = ttb2 @ stb @ rtb @ ttb1
    nmtb = nstb @ nrtb

    tb_verteces = [obj.clean(mtb @ vertex.T) for vertex in tb_verteces]
    tb_verteces = obj.convert_to_cartesians(tb_verteces)
    tb_surface_normals = [obj.clean(nmtb @ surface_normal.T) for surface_normal in tb_surface_normals]
    tb_surface_normals = obj.convert_to_cartesians(tb_surface_normals)
    tb_surface_normals = [obj.normalize(surface_normal) for surface_normal in tb_surface_normals]

    verteces += tb_verteces
    surface_normals += tb_surface_normals
    faces += tb_faces

    # create samll box
    sb_verteces, sb_faces, sb_surface_normals = obj.generate_cube()

    # cutout invisible faces
    sb_faces = sb_faces[2:10]
    sb_surface_normals = sb_surface_normals[2:10]

    # update faces
    updated_sb_faces = []
    for face in sb_faces:
        updated_face = list(face)
        for i, vertex_idx in enumerate(face):
            updated_face[i] = vertex_idx + len(verteces)
        updated_sb_faces.append(tuple(updated_face))
    sb_faces = updated_sb_faces

    # translate and scale
    sb_verteces = obj.convert_to_homogeneous_vertex(sb_verteces)
    sb_verteces = obj.convert_to_numpy(sb_verteces)
    sb_surface_normals = obj.convert_to_homogeneous_vector(sb_surface_normals)
    sb_surface_normals = obj.convert_to_numpy(sb_surface_normals)

    tsb1 = obj.translate((-0.5, -0.5, -0.5))
    ssb = obj.scale_and_mirror((1., 3., 1.))
    tsb2 = obj.translate((6., -2.25, -1.))
    nssb = obj.normal_matrix(ssb)
    msb = tsb2 @ ssb @ tsb1

    sb_verteces = [obj.clean(msb @ vertex.T) for vertex in sb_verteces]
    sb_verteces = obj.convert_to_cartesians(sb_verteces)
    sb_surface_normals = [obj.clean(nssb @ surface_normal.T) for surface_normal in sb_surface_normals]
    sb_surface_normals = obj.convert_to_cartesians(sb_surface_normals)
    sb_surface_normals = [obj.normalize(surface_normal) for surface_normal in sb_surface_normals]

    verteces += sb_verteces
    surface_normals += sb_surface_normals
    faces += sb_faces

    # colors and materials
    wall_surface_atributes = [[np.array([.9, .9, .9]), 1 / np.pi, 1 / np.pi, 1 / np.pi, 8] for i in range(len(room_faces))]
    light_box_surface_atributes = [[np.array([1., .95, .65]), 1 / np.pi, 1 / np.pi, 1 / np.pi, 8] for i in range(2 * len(ll_faces))]
    ceiling_surface_atributes = [[np.array([.9, .9, .9]), 1 / np.pi, 1 / np.pi, 1 / np.pi, 8] for i in range(len(ceiling_faces))]
    tb_surface_atributes = [[np.array([0., 0., 1.]), 1 / np.pi, 1 / np.pi, 1 / np.pi, 8],
                            [np.array([0., 0., 1.]), 1 / np.pi, 1 / np.pi, 1 / np.pi, 8],
                            [np.array([0., 1., 1.]), 1 / np.pi, 1 / np.pi, 1 / np.pi, 8],
                            [np.array([0., 1., 1.]), 1 / np.pi, 1 / np.pi, 1 / np.pi, 8],
                            [np.array([0., 1., 0.]), 1 / np.pi, 1 / np.pi, 1 / np.pi, 8],
                            [np.array([0., 1., 0.]), 1 / np.pi, 1 / np.pi, 1 / np.pi, 8],
                            [np.array([1., 1., 0.]), 1 / np.pi, 1 / np.pi, 1 / np.pi, 8],
                            [np.array([1., 1., 0.]), 1 / np.pi, 1 / np.pi, 1 / np.pi, 8]]
    sb_surface_atributes = list(reversed(tb_surface_atributes))
    surface_atributes = wall_surface_atributes + light_box_surface_atributes + ceiling_surface_atributes + tb_surface_atributes + sb_surface_atributes

    # lights:
    light_positions = [np.array([7.25, 3.2, 2.5]),
                       np.array([7.25, 3.2, -2.5]),
                       np.array([-1., 0., 0.])]
    light_atributes = [np.array([1., 1., 1.]),
                       np.array([1., 1., 1.]),
                       np.array([1., 1., 1.])]
    indirect_light = [np.array([.3, .3, .3])]
    background_color = np.array([0., 0., 0.])

    # camera:
    focal_point_x = -1.25
    width = 400
    height = 304
    framerate = 1
    save_path = "room_scene4.png"

    return verteces, surface_normals, faces, surface_atributes, light_positions, light_atributes, indirect_light, focal_point_x, background_color, width, height, framerate, save_path


def special_scene():

    def generate_p():
        p_front_verteces = [(0., 0., 0.),
                            (0., 5., 0.),
                            (0., 5., 1.),
                            (0., 5., 2.),
                            (0., 5., 3.),
                            (0., 2., 3.),
                            (0., 2., 2.),
                            (0., 2., 1.),
                            (0., 0., 1.),
                            (0., 3., 1.),
                            (0., 4., 1.),
                            (0., 4., 2.),
                            (0., 3., 2.)]
        p_back_verteces = [(1., vertex[1], vertex[2]) for vertex in p_front_verteces]
        p_verteces = p_front_verteces + p_back_verteces

        p_front_faces = [(0, 1, 2),
                         (0, 2, 8),
                         (2, 3, 10),
                         (3, 10, 11),
                         (3, 4, 5),
                         (3, 5, 6),
                         (6, 7, 9),
                         (6, 9, 12)]
        p_side_faces = [(0, 1, 13),
                        (1, 13, 14),
                        (1, 4, 14),
                        (4, 14, 17),
                        (4, 5, 17),
                        (5, 17, 18),
                        (5, 7, 18),
                        (7, 18, 20),
                        (7, 8, 20),
                        (8, 20, 21),
                        (0, 8, 13),
                        (8, 13, 21),
                        (9, 10, 22),
                        (10, 22, 23),
                        (10, 11, 23),
                        (11, 23, 24),
                        (11, 12, 24),
                        (12, 24, 25),
                        (9, 12, 22),
                        (12, 22, 25)]
        p_back_faces = [(face[0] + len(p_front_verteces), face[1] + len(p_front_verteces), face[2] + len(p_front_verteces)) for face in p_front_faces]
        p_faces = p_front_faces + p_side_faces + p_back_faces

        p_front_surface_normals = [(-1., 0., 0.) for i in range(len(p_front_faces))]
        p_side_surface_normals = [(0., 0., -1.),
                                  (0., 0., -1.),
                                  (0., 1., 0.),
                                  (0., 1., 0.),
                                  (0., 0., 1.),
                                  (0., 0., 1.),
                                  (0., -1., 0.),
                                  (0., -1., 0.),
                                  (0., 0., 1.),
                                  (0., 0., 1.),
                                  (0., -1., 0.),
                                  (0., -1., 0.),
                                  (0., 0., 1.),
                                  (0., 0., 1.),
                                  (0., -1., 0.),
                                  (0., -1., 0.),
                                  (0., 0., -1.),
                                  (0., 0., -1.),
                                  (0., 1., 0.),
                                  (0., 1., 0.)]
        p_back_surface_normals = [(1., 0., 0.) for i in range(len(p_back_faces))]
        p_surface_normals = p_front_surface_normals + p_side_surface_normals + p_back_surface_normals

        return p_verteces, p_faces, p_surface_normals

    def generate_a():
        a_front_verteces = [(0., 0., 0.),
                            (0., 4., 1.2),
                            (0., 5., 1.5),
                            (0., 5., 2.5),
                            (0., 4., 2.8),
                            (0., 0., 4.),
                            (0., 0., 3.),
                            (0., 2., 2.5),
                            (0., 2., 1.5),
                            (0., 0., 1.),
                            (0., 3., 1.75),
                            (0., 4., 2.),
                            (0., 3., 2.25)]
        a_back_verteces = [(1., vertex[1], vertex[2]) for vertex in a_front_verteces]
        a_verteces = a_front_verteces + a_back_verteces

        a_front_faces = [(0, 1, 9),
                         (1, 9, 11),
                         (1, 2, 11),
                         (2, 3, 11),
                         (3, 4, 11),
                         (4, 5, 6),
                         (4, 6, 11),
                         (7, 8, 10),
                         (7, 10, 12)]
        a_side_faces = [(0, 2, 13),
                        (2, 13, 15),
                        (2, 3, 15),
                        (3, 15, 16),
                        (3, 5, 16),
                        (5, 16, 18),
                        (5, 6, 18),
                        (6, 18, 19),
                        (6, 7, 19),
                        (7, 19, 20),
                        (7, 8, 20),
                        (8, 20, 21),
                        (8, 9, 21),
                        (9, 21, 22),
                        (9, 0, 22),
                        (0, 22, 13),
                        (10, 11, 23),
                        (11, 23, 24),
                        (11, 12, 24),
                        (12, 24, 25),
                        (12, 10, 25),
                        (10, 25, 23)]
        a_back_faces = [(face[0] + len(a_front_verteces), face[1] + len(a_front_verteces), face[2] + len(a_front_verteces)) for face in a_front_faces]
        a_faces = a_front_faces + a_side_faces + a_back_faces

        v1 = np.array([0., 5., 1.5])
        v2 = np.array([1., 0., 0.])
        normal = np.cross(v1, v2)
        normal_unit = normal / np.linalg.norm(normal)
        normal_neg1 = ()
        normal_pos1 = ()
        if normal_unit[2] < 0:
            normal_neg1 = (normal_unit[0], normal_unit[1], normal_unit[2])
            normal_pos1 = (-normal_unit[0], -normal_unit[1], -normal_unit[2])
        else:
            normal_neg1 = (-normal_unit[0], -normal_unit[1], -normal_unit[2])
            normal_pos1 = (normal_unit[0], normal_unit[1], normal_unit[2])
        normal_neg2 = (normal_neg1[0], -normal_neg1[1], normal_neg1[2])
        normal_pos2 = (normal_pos1[0], -normal_pos1[1], normal_pos1[2])

        a_front_surface_normals = [(-1., 0., 0.) for i in range(len(a_front_faces))]
        a_side_surface_normals = [normal_neg1,
                                  normal_neg1,
                                  (0., 1., 0.),
                                  (0., 1., 0.),
                                  normal_pos2,
                                  normal_pos2,
                                  (0., -1., 0.),
                                  (0., -1., 0.),
                                  normal_neg2,
                                  normal_neg2,
                                  (0., -1., 0.),
                                  (0., -1., 0.),
                                  normal_pos1,
                                  normal_pos1,
                                  (0., -1., 0.),
                                  (0., -1., 0.),
                                  normal_pos1,
                                  normal_pos1,
                                  normal_neg2,
                                  normal_neg2,
                                  (0., 1., 0.),
                                  (0., 1., 0.)]
        a_back_surface_normals = [(1., 0., 0.) for i in range(len(a_front_faces))]
        a_surface_normals = a_front_surface_normals + a_side_surface_normals + a_back_surface_normals

        return a_verteces, a_faces, a_surface_normals

    def update_faces(faces, num_previous_verteces):
        updated = []
        for face in faces:
            updated.append((face[0] + num_previous_verteces, face[1] + num_previous_verteces, face[2] + num_previous_verteces))
        return updated

    def transform(verteces, surface_normals, offset):
        cverteces = verteces.copy()
        csurface_normals = surface_normals.copy()
        cverteces = obj.convert_to_homogeneous_vertex(cverteces)
        cverteces = obj.convert_to_numpy(cverteces)
        csurface_normals = obj.convert_to_homogeneous_vector(csurface_normals)
        csurface_normals = obj.convert_to_numpy(csurface_normals)

        t1 = obj.translate(offset)

        cverteces = [obj.clean(t1 @ vertex.T) for vertex in cverteces]
        cverteces = obj.convert_to_cartesians(cverteces)
        csurface_normals = [obj.clean(surface_normal) for surface_normal in csurface_normals]
        csurface_normals = obj.convert_to_cartesians(csurface_normals)
        csurface_normals = [obj.normalize(surface_normal) for surface_normal in csurface_normals]

        return cverteces, csurface_normals

    p1_verteces, p1_faces, p1_surface_normals = generate_p()
    p1_verteces, p1_surface_normals = transform(p1_verteces, p1_surface_normals, (12., -2.5, -8.5))

    verteces = p1_verteces.copy()
    faces = p1_faces.copy()
    surface_normals = p1_surface_normals.copy()

    a1_verteces, a1_faces, a1_surface_normals = generate_a()
    a1_faces = update_faces(a1_faces, len(verteces))
    a1_verteces, a1_surface_normals = transform(a1_verteces, a1_surface_normals, (12., -2.5, -4.5))

    verteces += a1_verteces
    faces += a1_faces
    surface_normals += a1_surface_normals

    p2_verteces, p2_faces, p2_surface_normals = generate_p()
    p2_faces = update_faces(p2_faces, len(verteces))
    p2_verteces, p2_surface_normals = transform(p2_verteces, p2_surface_normals, (12., -2.5, 0.5))

    verteces += p2_verteces
    faces += p2_faces
    surface_normals += p2_surface_normals

    a2_verteces, a2_faces, a2_surface_normals = generate_a()
    a2_faces = update_faces(a2_faces, len(verteces))
    a2_verteces, a2_surface_normals = transform(a2_verteces, a2_surface_normals, (12., -2.5, 4.5))

    verteces += a2_verteces
    faces += a2_faces
    surface_normals += a2_surface_normals

    # colors and materials
    # colors = [np.array([0.88, 0.20, 0.25]),
    #           np.array([0.92, 0.50, 0.12]),
    #           np.array([0.88, 0.70, 0.10]),
    #           np.array([0.25, 0.70, 0.35]),
    #           np.array([0.55, 0.80, 0.20]),
    #           np.array([0.10, 0.65, 0.60]),
    #           np.array([0.20, 0.45, 0.85]),
    #           np.array([0.35, 0.30, 0.75]),
    #           np.array([0.60, 0.25, 0.70]),
    #           np.array([0.90, 0.30, 0.55])]
    # colors = [np.array([0.25, 0.70, 0.35]),
    #           np.array([0.55, 0.80, 0.20]),
    #           np.array([0.10, 0.65, 0.60]),
    #           np.array([0.20, 0.45, 0.85]),
    #           np.array([0.35, 0.30, 0.75]),
    #           np.array([0.60, 0.25, 0.70]),
    #           np.array([0.90, 0.30, 0.55])]
    colors = [np.array([0.6, .0, 0.8]),
              np.array([1., 0., 1.]),
              np.array([0.08235, 0.8, 1.0]),
              np.array([0., 0.28235, 0.])]
    surface_atributes = []
    for face_idx in range(len(faces)):
        color = colors[face_idx % len(colors)]
        surface_atributes.append([color, 1 / np.pi, 1 / np.pi, 1 / np.pi, 8])

    # lights:
    light_positions = [np.array([-1., 0., 0.])]
    light_atributes = [np.array([1., 1., 1.])]
    # light_atributes = [np.array([0.8, 0.75, 1.]),
    #                    np.array([1., 0.5, 0.5])]
    indirect_light = [np.array([.3, .3, .3])]
    background_color = np.array([0., 0., 0.])

    # camera:
    focal_point_x = -1
    width = 400
    height = 304
    framerate = 1
    save_path = "papa_scene4.png"

    return verteces, surface_normals, faces, surface_atributes, light_positions, light_atributes, indirect_light, focal_point_x, background_color, width, height, framerate, save_path


def special_scene2():
    def create_sloped_normal(v1, v2):
        normal = np.cross(v1, v2)
        normal_unit = normal / np.linalg.norm(normal)
        normal_neg1 = ()
        normal_pos1 = ()
        if normal_unit[2] < 0:
            normal_neg1 = (normal_unit[0], normal_unit[1], normal_unit[2])
            normal_pos1 = (-normal_unit[0], -normal_unit[1], -normal_unit[2])
        else:
            normal_neg1 = (-normal_unit[0], -normal_unit[1], -normal_unit[2])
            normal_pos1 = (normal_unit[0], normal_unit[1], normal_unit[2])
        normal_neg2 = (normal_neg1[0], -normal_neg1[1], normal_neg1[2])
        normal_pos2 = (normal_pos1[0], -normal_pos1[1], normal_pos1[2])
        return normal_pos1, normal_neg1, normal_pos2, normal_neg2

    def generate_d():
        d_front_verteces = [(0., 0., 0.),
                            (0., 5., 0.),
                            (0., 5., 1.),
                            (0., 5., 2.),
                            (0., 4., 3.),
                            (0., 1., 3.),
                            (0., 0., 2.),
                            (0., 0., 1.),
                            (0., 1., 1.),
                            (0., 4., 1.),
                            (0., 4., 1.5),
                            (0., 3.5, 2.),
                            (0., 1.5, 2.),
                            (0., 1., 1.5)]
        d_back_verteces = [(1., vertex[1], vertex[2]) for vertex in d_front_verteces]
        d_verteces = d_front_verteces + d_back_verteces

        d_front_faces = [(0, 1, 2),
                         (0, 2, 7),
                         (2, 9, 10),
                         (2, 3, 10),
                         (3, 4, 10),
                         (4, 10, 11),
                         (4, 11, 12),
                         (4, 5, 12),
                         (5, 12, 13),
                         (5, 6, 13),
                         (6, 7, 13),
                         (7, 8, 13)]
        d_side_faces = [(0, 1, 14), (1, 14, 15),
                        (1, 3, 15), (3, 15, 17),
                        (3, 4, 17), (4, 17, 18),
                        (4, 5, 18), (5, 18, 19),
                        (5, 6, 19), (6, 19, 20),
                        (0, 6, 14), (6, 14, 20),
                        (8, 9, 22), (9, 22, 23),
                        (9, 10, 23), (10, 23, 24),
                        (10, 11, 24), (11, 24, 25),
                        (11, 12, 25), (12, 25, 26),
                        (12, 13, 26), (13, 26, 27),
                        (8, 13, 27), (8, 22, 27)]
        d_back_faces = [(face[0] + len(d_front_verteces), face[1] + len(d_front_verteces), face[2] + len(d_front_verteces)) for face in d_front_faces]
        d_faces = d_front_faces + d_side_faces + d_back_faces

        normal_pos1, normal_neg1, normal_pos2, normal_neg2 = create_sloped_normal(np.array([0., -1., 1.]), np.array([1., 0., 0.]))
        d_front_surface_normals = [(-1., 0., 0.) for i in range(len(d_front_faces))]
        d_side_surface_normals = [(0., 0., -1.), (0., 0., -1.),
                                  (0., 1., 0.), (0., 1., 0.),
                                  normal_pos1, normal_pos1,
                                  (0., 0., 1.), (0., 0., 1.),
                                  normal_pos2, normal_pos2,
                                  (0., -1., 0.), (0., -1., 0.),
                                  (0., 0., 1.), (0., 0., 1.),
                                  (0., -1., 0.), (0., -1., 0.),
                                  normal_neg1, normal_neg1,
                                  (0., 0., -1.), (0., 0., -1.),
                                  normal_neg2, normal_neg2,
                                  (0., 1., 0.), (0., 1., 0.)]
        d_back_surface_normals = [(1., 0., 0.) for i in range(len(d_back_faces))]
        d_surface_normals = d_front_surface_normals + d_side_surface_normals + d_back_surface_normals

        return d_verteces, d_faces, d_surface_normals

    def generate_a():
        a_front_verteces = [(0., 0., 0.),
                            (0., 4., 1.2),
                            (0., 5., 1.5),
                            (0., 5., 2.5),
                            (0., 4., 2.8),
                            (0., 0., 4.),
                            (0., 0., 3.),
                            (0., 2., 2.5),
                            (0., 2., 1.5),
                            (0., 0., 1.),
                            (0., 3., 1.75),
                            (0., 4., 2.),
                            (0., 3., 2.25)]
        a_back_verteces = [(1., vertex[1], vertex[2]) for vertex in a_front_verteces]
        a_verteces = a_front_verteces + a_back_verteces

        a_front_faces = [(0, 1, 9),
                         (1, 9, 11),
                         (1, 2, 11),
                         (2, 3, 11),
                         (3, 4, 11),
                         (4, 5, 6),
                         (4, 6, 11),
                         (7, 8, 10),
                         (7, 10, 12)]
        a_side_faces = [(0, 2, 13),
                        (2, 13, 15),
                        (2, 3, 15),
                        (3, 15, 16),
                        (3, 5, 16),
                        (5, 16, 18),
                        (5, 6, 18),
                        (6, 18, 19),
                        (6, 7, 19),
                        (7, 19, 20),
                        (7, 8, 20),
                        (8, 20, 21),
                        (8, 9, 21),
                        (9, 21, 22),
                        (9, 0, 22),
                        (0, 22, 13),
                        (10, 11, 23),
                        (11, 23, 24),
                        (11, 12, 24),
                        (12, 24, 25),
                        (12, 10, 25),
                        (10, 25, 23)]
        a_back_faces = [(face[0] + len(a_front_verteces), face[1] + len(a_front_verteces), face[2] + len(a_front_verteces)) for face in a_front_faces]
        a_faces = a_front_faces + a_side_faces + a_back_faces

        v1 = np.array([0., 5., 1.5])
        v2 = np.array([1., 0., 0.])
        normal = np.cross(v1, v2)
        normal_unit = normal / np.linalg.norm(normal)
        normal_neg1 = ()
        normal_pos1 = ()
        if normal_unit[2] < 0:
            normal_neg1 = (normal_unit[0], normal_unit[1], normal_unit[2])
            normal_pos1 = (-normal_unit[0], -normal_unit[1], -normal_unit[2])
        else:
            normal_neg1 = (-normal_unit[0], -normal_unit[1], -normal_unit[2])
            normal_pos1 = (normal_unit[0], normal_unit[1], normal_unit[2])
        normal_neg2 = (normal_neg1[0], -normal_neg1[1], normal_neg1[2])
        normal_pos2 = (normal_pos1[0], -normal_pos1[1], normal_pos1[2])

        a_front_surface_normals = [(-1., 0., 0.) for i in range(len(a_front_faces))]
        a_side_surface_normals = [normal_neg1,
                                  normal_neg1,
                                  (0., 1., 0.),
                                  (0., 1., 0.),
                                  normal_pos2,
                                  normal_pos2,
                                  (0., -1., 0.),
                                  (0., -1., 0.),
                                  normal_neg2,
                                  normal_neg2,
                                  (0., -1., 0.),
                                  (0., -1., 0.),
                                  normal_pos1,
                                  normal_pos1,
                                  (0., -1., 0.),
                                  (0., -1., 0.),
                                  normal_pos1,
                                  normal_pos1,
                                  normal_neg2,
                                  normal_neg2,
                                  (0., 1., 0.),
                                  (0., 1., 0.)]
        a_back_surface_normals = [(1., 0., 0.) for i in range(len(a_front_faces))]
        a_surface_normals = a_front_surface_normals + a_side_surface_normals + a_back_surface_normals

        return a_verteces, a_faces, a_surface_normals

    def update_faces(faces, num_previous_verteces):
        updated = []
        for face in faces:
            updated.append((face[0] + num_previous_verteces, face[1] + num_previous_verteces, face[2] + num_previous_verteces))
        return updated

    def transform(verteces, surface_normals, offset):
        cverteces = verteces.copy()
        csurface_normals = surface_normals.copy()
        cverteces = obj.convert_to_homogeneous_vertex(cverteces)
        cverteces = obj.convert_to_numpy(cverteces)
        csurface_normals = obj.convert_to_homogeneous_vector(csurface_normals)
        csurface_normals = obj.convert_to_numpy(csurface_normals)

        t1 = obj.translate(offset)

        cverteces = [obj.clean(t1 @ vertex.T) for vertex in cverteces]
        cverteces = obj.convert_to_cartesians(cverteces)
        csurface_normals = [obj.clean(surface_normal) for surface_normal in csurface_normals]
        csurface_normals = obj.convert_to_cartesians(csurface_normals)
        csurface_normals = [obj.normalize(surface_normal) for surface_normal in csurface_normals]

        return cverteces, csurface_normals

    p1_verteces, p1_faces, p1_surface_normals = generate_p()
    p1_verteces, p1_surface_normals = transform(p1_verteces, p1_surface_normals, (12., -2.5, -8.5))

    verteces = p1_verteces.copy()
    faces = p1_faces.copy()
    surface_normals = p1_surface_normals.copy()

    a1_verteces, a1_faces, a1_surface_normals = generate_a()
    a1_faces = update_faces(a1_faces, len(verteces))
    a1_verteces, a1_surface_normals = transform(a1_verteces, a1_surface_normals, (12., -2.5, -4.5))

    verteces += a1_verteces
    faces += a1_faces
    surface_normals += a1_surface_normals

    p2_verteces, p2_faces, p2_surface_normals = generate_p()
    p2_faces = update_faces(p2_faces, len(verteces))
    p2_verteces, p2_surface_normals = transform(p2_verteces, p2_surface_normals, (12., -2.5, 0.5))

    verteces += p2_verteces
    faces += p2_faces
    surface_normals += p2_surface_normals

    a2_verteces, a2_faces, a2_surface_normals = generate_a()
    a2_faces = update_faces(a2_faces, len(verteces))
    a2_verteces, a2_surface_normals = transform(a2_verteces, a2_surface_normals, (12., -2.5, 4.5))

    verteces += a2_verteces
    faces += a2_faces
    surface_normals += a2_surface_normals

    # colors and materials
    # colors = [np.array([0.88, 0.20, 0.25]),
    #           np.array([0.92, 0.50, 0.12]),
    #           np.array([0.88, 0.70, 0.10]),
    #           np.array([0.25, 0.70, 0.35]),
    #           np.array([0.55, 0.80, 0.20]),
    #           np.array([0.10, 0.65, 0.60]),
    #           np.array([0.20, 0.45, 0.85]),
    #           np.array([0.35, 0.30, 0.75]),
    #           np.array([0.60, 0.25, 0.70]),
    #           np.array([0.90, 0.30, 0.55])]
    # colors = [np.array([0.25, 0.70, 0.35]),
    #           np.array([0.55, 0.80, 0.20]),
    #           np.array([0.10, 0.65, 0.60]),
    #           np.array([0.20, 0.45, 0.85]),
    #           np.array([0.35, 0.30, 0.75]),
    #           np.array([0.60, 0.25, 0.70]),
    #           np.array([0.90, 0.30, 0.55])]
    colors = [np.array([0.6, .0, 0.8]),
              np.array([1., 0., 1.]),
              np.array([0.08235, 0.8, 1.0])]
    surface_atributes = []
    for face_idx in range(len(faces)):
        color = colors[face_idx % len(colors)]
        surface_atributes.append([color, 1 / np.pi, 1 / np.pi, 1 / np.pi, 8])

    # lights:
    light_positions = [np.array([-1., 0., 0.])]
    light_atributes = [np.array([1., 1., 1.])]
    # light_atributes = [np.array([0.8, 0.75, 1.]),
    #                    np.array([1., 0.5, 0.5])]
    indirect_light = [np.array([.3, .3, .3])]
    background_color = np.array([0., 0.28235, 0.])

    # camera:
    focal_point_x = -1
    width = 100
    height = 100
    framerate = 1
    save_path = "test.png"

    return verteces, surface_normals, faces, surface_atributes, light_positions, light_atributes, indirect_light, focal_point_x, background_color, width, height, framerate, save_path
