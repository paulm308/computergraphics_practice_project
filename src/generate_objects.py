import numpy as np


verteces = []
faces = []


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
    return cube_verteces, cube_faces


def convert_to_homegeneous(verteces: list[tuple[float, float, float]]):
    return [(vertex[0], vertex[1], vertex[2], 1.0) for vertex in verteces]


def convert_to_cartesian(verteces: list[tuple[float, float, float, float]]):
    return [(vertex[0] / vertex[3], vertex[1] / vertex[3], vertex[2] / vertex[3]) for vertex in verteces]


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


if __name__ == "__main__":
    cube_verteces, cube_faces = generate_cube()
    cube_verteces = convert_to_homegeneous(cube_verteces)
    cube_verteces = convert_to_numpy(cube_verteces)
    tm1 = translate((-0.5, -0.5, -0.5))
    rx = rotate((90., 90., 0.))
    tm2 = translate((1.5, 1.5, 1.5))
    m = tm2 @ rx @ tm1
    cube_verteces = [m @ vertex.T for vertex in cube_verteces]
    print(cube_verteces)
