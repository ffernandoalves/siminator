import random

import pygame

from siminator import inator_engine as ie
from siminator import Ellipsoid
from siminator.camera import Camera
from siminator.vec3 import Vector3


# Constants
SCREEN_COLOR = "#DCDDD8"
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

lastX = SCREEN_WIDTH/2
lastY = SCREEN_HEIGHT/2

# Colors
WHITE = (255, 255, 255)
COLORS = ["#3c887e", "#190e4f", "#fb8b24", "#04a777", "#b10f2e"]

# Callbacks
def quit(self: ie.InatorEngine):
    """custom exit"""
    if self.pg_event.type == pygame.KEYDOWN:
        if self.pg_event.key == pygame.K_ESCAPE:
            self.running = False


class Inator(ie.InatorEngine):
    def update(self):
        self.window.set_title(f"{self.window.infos.init_title} | FPS {round(self.clock.get_fps())}")

    def start(self):
        self.camera = Camera(Vector3([0, 0, 20]), self.window, 700)

        pos_min = 0
        pos_max = 20
        ellipsoids = [Ellipsoid(Vector3([random.uniform(pos_min, pos_max),
                                         random.uniform(pos_min, pos_max),
                                         random.uniform(pos_min, pos_max)]),
                                random.choice(COLORS), self.camera,
                                random.uniform(1, 9)) for i in range(3)]

        self.add_models(ellipsoids)
        self.add_callback((quit, self))


if __name__ == "__main__":
    screen_info = ie.ScreenInfo(SCREEN_WIDTH,
                                SCREEN_HEIGHT,
                                "Siminator",
                                SCREEN_COLOR)

    Inator(screen_info).run()

