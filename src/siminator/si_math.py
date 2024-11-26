import numpy as np
import numba as nb
from numba.experimental import jitclass

from siminator.si_types import ModelShape

__all__ = [
    "project_3d_to_2d",
    "rotate_x",
    "rotate_y",
    "rotate_z",
    "rotations",
    "rotate",
    "normalize"
]

spec = [
    ("x", nb.float64),
    ("y", nb.float64),
    ("z", nb.float64),
]
@jitclass(spec)
class Vector3(object):
    def __init__(self, array):
        self.x = array[0]
        self.y = array[1]
        self.z = array[2]
    
    def to_array(self):
        return np.array([self.x, self.y, self.z])

@nb.njit
def project_3d_to_2d(x, y, z, screen_center: tuple[int, int], camera_distance: int, FOV: int):
    factor = FOV / (camera_distance + z)
    x_2d = int(x * factor) + screen_center[0]
    y_2d = int(-y * factor) + screen_center[1]
    return x_2d, y_2d

def rotate_x(vertices: np.ndarray, angle):
    rotation_matrix_x = np.array([[1, 0, 0],
                                  [0, np.cos(angle), -np.sin(angle)],
                                  [0, np.sin(angle), np.cos(angle)]])
    return np.dot(vertices, rotation_matrix_x)

def rotate_y(vertices: np.ndarray, angle):
    rotation_matrix_y = np.array([[np.cos(angle), 0, np.sin(angle)],
                                  [0, 1, 0],
                                  [-np.sin(angle), 0, np.cos(angle)]])
    return np.dot(vertices, rotation_matrix_y)

def rotate_z(vertices: np.ndarray, angle):
    rotation_matrix_z = np.array([[np.cos(angle), 0, -np.sin(angle)],
                                  [np.sin(angle), 0, np.cos(angle)],
                                  [0, 0, 1]])
    return np.dot(vertices, rotation_matrix_z)

rotations = {
    "x": rotate_x,
    "y": rotate_y,
    "z": rotate_z,
}

def rotate(positions: ModelShape, angles: tuple[float], axes: str) -> ModelShape:
    """
    Args:
        positions (ModelShape):
        angles (tuple[float]): 
        axes (str):
        example:
            >>> rotate(0., 'x')

            >>> rotate([0., 1.], 'xy')

            >>> rotate([0., 1., 0.], 'yxy')

            >>> rotate(0., 'xy')
    """
    _angles = angles
    if isinstance(_angles, float):
        _angles = [_angles] * len(axes)
    elif isinstance(_angles, list):
        if len(_angles) != len(axes):
            _angles = [_angles[0]] * len(axes) # aceita apenas o primeiro angulo
            
    rotated_points = rotations[axes[0]](positions, _angles[0])
    for i in range(1, len(axes)):
        rotated_points = rotations[axes[i]](rotated_points, _angles[i])

    return rotated_points

@nb.jit(nopython=True)
def normalize1d(v: Vector3) -> Vector3:
    v = Vector3(v)
    length_of_v = np.sqrt((v.x * v.x) + (v.y * v.y) + (v.z * v.z))
    return Vector3([v.x / length_of_v, v.y / length_of_v, v.z / length_of_v]).to_array()

@nb.jit(nopython=True)
def normalize3d(vs: list[Vector3]) -> list[Vector3]:
    minX = vs[0].x
    maxX = vs[0].x
    minY = vs[0].y
    maxY = vs[0].y
    minZ = vs[0].z
    maxZ = vs[0].z

    for v in vs:
        minX = min(minX, v.x)
        maxX = max(maxX, v.x)
        minY = min(minY, v.y)
        maxY = max(maxY, v.y)
        minZ = min(minZ, v.z)
        maxZ = max(maxZ, v.z)

    centerX = (minX + maxX) / 2.0
    centerY = (minY + maxY) / 2.0
    centerZ = (minZ + maxZ) / 2.0

    amplitudeX = maxX - minX
    amplitudeY = maxY - minY
    amplitudeZ = maxZ - minZ
    max_amplitude = max([amplitudeX, amplitudeY, amplitudeZ])

    for v in vs:
        v.x = (v.x - centerX) / max_amplitude
        v.y = (v.y - centerY) / max_amplitude
        v.z = (v.z - centerZ) / max_amplitude
    return v
    
@nb.njit
def lookAt(eye: Vector3, center: Vector3, up: Vector3):
    f = normalize1d(eye - center)
    s = normalize1d(Vector3(np.cross(up, f)))
    u = normalize1d(Vector3(np.cross(f, s)))
    mat4 = np.identity(4)
    mat4[0][0] = s.x
    mat4[1][0] = s.y
    mat4[2][0] = s.z
    mat4[0][1] = u.x
    mat4[1][1] = u.x
    mat4[2][1] = u.x
    mat4[0][2] = f.x
    mat4[1][2] = f.x
    mat4[2][2] = f.x
    mat4[3][0] =-np.dot(s, eye)
    mat4[3][1] =-np.dot(u, eye)
    mat4[3][2] = np.dot(f, eye)
    return mat4

# @nb.njit
# def projection():
#     return

# @nb.njit
# def pvm(projection, view, position: Vector3):
#     return projection * view * np.array([position, 1.0], dtype=float)
