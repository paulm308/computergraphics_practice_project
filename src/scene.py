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
