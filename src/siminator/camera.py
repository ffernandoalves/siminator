import numpy as np
import pygame

from siminator import Vector3, si_math
from siminator.window import Window


class Camera:
    world_up: Vector3
    up: Vector3
    speed: float
    right: Vector3
    forward: Vector3
    target_position: Vector3
    position: Vector3
    zoom: float = 45.0
    yaw: float = -90.0
    roll: float = 0.0
    pitch: float = 0.0
    mouse_sensibility: float = 0.05

    def __init__(self, position: Vector3, window: Window, fov):
        self.position = position
        self.screen_info = window.infos
        self.screen = window.screen
        self.fov = fov
        self.world_up = Vector3([0, 1, 0])
        self.target_position = Vector3([0, 0, 1])
        self.update()
    
    def get_view_mat4(self):
        mat4 = si_math.lookAt(self.position, self.position + self.forward, self.up)
        return mat4

    def update(self):
        front: Vector3 = Vector3([0, 0, 0])
        front.x = np.cos(np.radians(self.yaw)) * np.cos(np.radians(self.pitch))
        front.y = np.sin(np.radians(self.pitch))
        front.z = np.sin(np.radians(self.yaw)) * np.cos(np.radians(self.pitch))
        self.forward = si_math.normalize1d(front.view(np.ndarray))
        self.right = si_math.normalize1d(np.cross(self.world_up, self.forward))
        self.up = np.cross(self.forward, self.right)

    def mouse_event(self, xoffset: float, yoffset: float):
        xoffset *= self.mouse_sensibility
        yoffset *= self.mouse_sensibility
        
        self.yaw += xoffset
        self.pitch += yoffset
        
        if self.pitch > 89.0:
            self.pitch = 89.0
        if self.pitch < -89.0:
            self.pitch = -89.0

        self.update()

    def mouse_scroll(self, yoffset: float):
        self.speed += yoffset
        if self.speed < 0.0:
            self.speed = 0.0

    def keyboard_event(self, key: int, delta_time: float):
        velocity = self.speed * delta_time
        if (key == pygame.K_w):
            self.position += velocity*self.forward
        if (key == pygame.K_s):
            self.position -= velocity*self.forward


