import numpy as np
from generate_objects import normalize


def compute_rays(num_x: int, num_y: int, focal_point_x: float):
    pixel_width = 2 / max(num_x, num_y)
    sensor_pixel_top_left_x = -(num_x * pixel_width) / 2 + 0.5 * pixel_width
    sensor_pixel_top_left_y = -(num_y * pixel_width) / 2 + 0.5 * pixel_width

    rays = []
    for x in range(num_x):
        for y in range(num_y):
            sensor_pixel_x_pos = sensor_pixel_top_left_x + x * pixel_width
            sensor_pixel_y_pos = sensor_pixel_top_left_y + y * pixel_width

            sensor_pixel_pos = np.array([0., sensor_pixel_y_pos, sensor_pixel_x_pos, 1.])
            focal_point = np.array([focal_point_x, 0., 0., 1.])
            direction = normalize(sensor_pixel_pos - focal_point)
            rays.append((sensor_pixel_pos, direction))
    return rays


def ray_triangle_intersect(origin, direction, verteces, epsilon=1e-8):
    edge1 = verteces[1] - verteces[0]
    edge2 = verteces[2] - verteces[0]

    h = np.cross(direction, edge2)
    a = np.dot(edge1, h)

    if abs(a) < epsilon:
        return None

    f = 1.0 / a
    s = origin - verteces[0]
    u = f * np.dot(s, h)

    if u < 0.0 or u > 1.0:
        return None

    q = np.cross(s, edge1)
    v = f * np.dot(direction, q)

    if v < 0.0 or u + v > 1.0:
        return None

    t = f * np.dot(edge2, q)

    if t > epsilon:
        return t
    else:
        return None


def compute_intersections(rays: list, verteces: list, faces: list):
    res = []
    for ray in rays:
        intersections = []
        for face_index, face in enumerate(faces):
            origin, direction = ray
            face_verteces = [verteces[face[i]] for i in range(len(face))]
            t = ray_triangle_intersect(origin, direction, face_verteces)
            intersections += [(t, face_index)] if t is not None else []
        if len(intersections) != 0:
            intersection = min(intersections, key=lambda x: x[0])
            res += [intersection]
        else:
            res += [None]
    return res


def compute_light(direction, light_positions, point, verteces, normal, faces, face_index, surface_atributes, light_atributes):
    rho = surface_atributes[face_index][0]
    rho_white = np.array([1., 1., 1.])
    L_indirect = np.array([0.1, 0.1, 0.1])
    alpha = surface_atributes[face_index][1]
    beta = surface_atributes[face_index][2]
    gamma = surface_atributes[face_index][3]
    m = surface_atributes[face_index][4]
    v = -direction
    n = normal

    light_sum = np.array([0., 0., 0.])
    for light_index, light_pos in enumerate(light_positions):
        blocked = False
        raw_l_i = light_pos - point
        l_i = normalize(raw_l_i)
        for face in faces:
            face_verteces = [verteces[face[i]] for i in range(len(face))]
            t = ray_triangle_intersect(point, raw_l_i, face_verteces, epsilon=1e-8)
            if t is not None and t < 1.0:
                blocked = True
                break
        if blocked:
            continue

        L_i = light_atributes[light_index]
        r_i = 2 * np.dot(n, l_i) * n - l_i

        n_dot_l = max(np.dot(n, l_i), 0)
        r_dot_v = max(np.dot(r_i, v), 0)

        tmp = beta * rho + gamma * rho_white * (r_dot_v ** m)
        light_sum += L_i * n_dot_l * tmp

    return alpha * rho * L_indirect + light_sum


# TODO MUSS NOCH GETESTET WERDEN!
def compute_image(intersections, num_x, num_y, rays, verteces, light_positions, faces, face_normals, surface_atributes, light_atributes, background_color):
    image = [[] for i in range(num_x)]
    for x in range(num_x):
        for y in range(num_y):
            idx = x + y * num_x
            color = background_color
            if intersections[idx] is not None:
                direction = rays[idx][1]
                t = intersections[idx][0]
                point = rays[0] + t * direction
                face_index = intersections[idx][1]
                normal = face_normals[face_index]
                color = compute_light(direction, light_positions, point, verteces, normal, faces, face_index, surface_atributes, light_atributes)
            image[x].append(color)
