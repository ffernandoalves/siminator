import pygame

# 3D projection settings
FOV = 700  # Field of View
CAMERA_DISTANCE = 1  # Distance of camera from origin


class Draw:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.fov = FOV
        self.camera_distance = CAMERA_DISTANCE

    def project_3d_to_2d(self, x, y, z):
        screen_center = (self.screen.width//2, self.screen.height//2)
        factor = FOV / (self.camera_distance + z)
        x_2d = int(x * factor) + screen_center[0]
        y_2d = int(-y * factor) + screen_center[1]
        return x_2d, y_2d
