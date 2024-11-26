from siminator import Vector3
from siminator import si_math
from siminator.camera import Camera
from siminator.si_types import ModelShape


class Drawable:
    position: Vector3 # ou vertice_center
    to_draw = True

    def draw(self, delta_time: float):
        pass


class Model(Drawable):
    vertices: ModelShape
    centered_points: ModelShape
    projected_points: list
    def __init__(self, camera: Camera):
        self.angle_x: float = 0.
        self.angle_y: float = 0.
        self.angle_z: float = 0.
        self.camera = camera

    def rotate(self, angle: tuple[float], axes: str):
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
        rotated_points = si_math.rotate(self.centered_points, angle, axes)
        final_points = rotated_points + self.position
        return final_points

