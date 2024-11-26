import numpy as np
import pygame
from scipy.spatial import ConvexHull

from siminator import Model, si_math
from siminator.camera import Camera
from siminator.si_types import ModelShape
from siminator.vec3 import Vector3

def generate_ellipsoid_points(a, b, c, n, x0, y0, z0):
    p = 1.6075
    ap = (4 * np.pi * (((a**p * b**p + b**p * c**p + a**p * c**p) / 3)**(1 / p))) / n
    d = np.sqrt(ap)
    nphi = round(np.pi / d)
    dphi = np.pi / nphi
    ltheta = ap / dphi
    points = []

    if np.min([a, b, c], axis=0) == c:
        for i in range(nphi):
            phi = np.pi * (i + 0.5) / nphi
            myz = c * np.cos(phi)
            if a >= b:
                myr = a * np.sqrt(1 - myz**2 / c**2)
            else:
                myr = b * np.sqrt(1 - myz**2 / c**2)
            ntheta = round(2 * np.pi * myr / ltheta)
            for j in range(ntheta):
                theta = 2 * np.pi * j / ntheta
                x = x0 + a * np.sin(phi) * np.cos(theta)
                y = y0 + b * np.sin(phi) * np.sin(theta)
                z = z0 + c * np.cos(phi)
                points.append([round(x, 5), round(y, 5), round(z, 5)])
    
    return np.array(points)


class Ellipsoid(Model):
    def __init__(self, position: Vector3, color, camera: Camera, amplitude: int = 5):
        super().__init__(camera)
        self.color = color
        a, b, c = 2, 2, 2
        n = 500

        self.amp = amplitude

        self.vertices = generate_ellipsoid_points(a, b, c, n, position.x, position.y, position.z)
        hull = ConvexHull(self.vertices)
        self.triangles = hull.simplices
        self.position = position # vertice_center
        self.centered_points: ModelShape = self.vertices - self.position

    def motion(self, delta_time: float):
        self.position[0] = np.sin(delta_time) * self.amp
        self.position[1] = np.cos(delta_time) * self.amp
        self.position[2] = np.sin(delta_time) * np.cos(delta_time) / self.amp
        final_points = self.rotate([self.angle_y, self.angle_x], "yx")
        self.projected_points = [si_math.project_3d_to_2d(x, y, z, self.camera.screen_info.center, self.camera.position.z, self.camera.fov) for x, y, z in final_points]

    def draw(self, delta_time: float):
        self.motion(delta_time)

        for triangle in self.triangles:
            points = [self.projected_points[i] for i in triangle]
            pygame.draw.polygon(self.camera.screen, self.color, points, 1)

        self.angle_x += 0.01
        self.angle_y += 0.01
        self.angle_z += 0.01
    
    