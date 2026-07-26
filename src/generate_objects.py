import numpy as np


def generate_cube():
    cube_verteces = []
    for i in range(8, 16):
        vertex = tuple(bin(i)[3:])
        vertex = tuple([float(i) for i in vertex])
        cube_verteces.append(vertex)
    cube_faces = [(0, 1, 4),
                  (1, 4, 5),
                  (0, 1, 2),
                  (1, 2, 3),
                  (1, 3, 5),
                  (3, 5, 7),
                  (0, 2, 4),
                  (2, 4, 6),
                  (2, 3, 6),
                  (3, 6, 7),
                  (4, 5, 6),
                  (5, 6, 7)]
    cube_surface_normals = [(0., -1., 0.),
                            (0., -1., 0.),
                            (-1., 0., 0.),
                            (-1., 0., 0.),
                            (0., 0., -1.),
                            (0., 0., -1.),
                            (0., 0., 1.),
                            (0., 0., 1.),
                            (0., 1., 0.),
                            (0., 1., 0.),
                            (1., 0., 0.),
                            (1., 0., 0.)]
    return cube_verteces, cube_faces, cube_surface_normals


def convert_to_homogeneous_vertex(verteces: list[tuple[float, float, float]]):
    return [(vertex[0], vertex[1], vertex[2], 1.0) for vertex in verteces]


def convert_to_homogeneous_vector(vectors: list[tuple[float, float, float]]):
    return [(vector[0], vector[1], vector[2], 0.0) for vector in vectors]


def convert_to_cartesians(verteces):
    return [np.array([vertex[0] / vertex[3], vertex[1] / vertex[3], vertex[2] / vertex[3]]) if abs(vertex[3]) > 1e-10 else vertex[:3] for vertex in verteces]


def convert_to_cartesian(vertex):
    return np.array([vertex[0] / vertex[3], vertex[1] / vertex[3], vertex[2] / vertex[3]]) if abs(vertex[3]) > 1e-10 else vertex[:3]


def convert_to_numpy(verteces: list[tuple]):
    res = []
    for vertex in verteces:
        res.append(np.array(vertex))
    return res


def translate(vector: tuple[float, float, float]):
    return np.array([[1., 0., 0., vector[0]],
                     [0., 1., 0., vector[1]],
                     [0., 0., 1., vector[2]],
                     [0., 0., 0., 1.]])


def rotate(vector: tuple[float, float, float]):
    vector = np.radians(np.array(vector))  # type: ignore
    rx = np.array([[1., 0., 0., 0.],
                   [0., np.cos(vector[0]), -np.sin(vector[0]), 0.],
                   [0, np.sin(vector[0]), np.cos(vector[0]), 0.],
                   [0., 0., 0., 1.]])
    ry = np.array([[np.cos(vector[1]), 0., np.sin(vector[1]), 0.],
                   [0., 1., 0., 0.],
                   [-np.sin(vector[1]), 0., np.cos(vector[1]), 0.],
                   [0., 0., 0., 1.]])
    rz = np.array([[np.cos(vector[2]), -np.sin(vector[2]), 0., 0.],
                   [np.sin(vector[2]), np.cos(vector[2]), 0., 0.],
                   [0., 0., 1., 0.],
                   [0., 0., 0., 1.]])
    return rx @ ry @ rz


def scale_and_mirror(vector: tuple[float, float, float]):
    return np.array([[vector[0], 0., 0., 0.],
                     [0., vector[1], 0., 0.],
                     [0., 0., vector[2], 0.],
                     [0., 0., 0., 1.]])


def shear(vector: tuple):
    assert len(vector) == 6
    return np.array([[1., vector[0], vector[1], 0.],
                     [vector[2], 1., vector[3], 0.],
                     [vector[4], vector[5], 1., 0.],
                     [0., 0., 0., 1.]])


def normal_matrix(M):
    return np.linalg.inv(M).T


def normalize(vector):
    length = np.linalg.norm(vector[:3])
    result = vector.copy()
    result[:3] = vector[:3] / length
    return result


def clean(array, tol=1e-10):
    array = np.where(np.abs(array) < tol, 0.0, array)
    return array


if __name__ == "__main__":
    cube_verteces, cube_faces, cube_surface_normals = generate_cube()

    cube_verteces = convert_to_homogeneous_vertex(cube_verteces)
    cube_verteces = convert_to_numpy(cube_verteces)
    cube_surface_normals = convert_to_homogeneous_vector(cube_surface_normals)
    cube_surface_normals = convert_to_numpy(cube_surface_normals)

    t1 = translate((-0.5, -0.5, -0.5))
    r = rotate((90., 90., 0.))
    s = scale_and_mirror((2., 2., 2.))
    t2 = translate((1.5, 1.5, 1.5))
    m = t2 @ s @ r @ t1

    nr = normal_matrix(r)
    ns = normal_matrix(s)
    nm = ns @ nr

    cube_verteces = [clean(m @ vertex.T) for vertex in cube_verteces]
    cube_surface_normals = [clean(normalize(nm @ surface_normal.T)) for surface_normal in cube_surface_normals]
    print(f"{cube_verteces}\n{cube_surface_normals}")
