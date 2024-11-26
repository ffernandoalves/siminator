## Exemplo 

```python
import pygame

from siminator import inator_engine as ie
from siminator import Ellipsoid
from siminator.camera import Camera
from siminator.vec3 import Vector3


# Constants
SCREEN_COLOR = "#DCDDD8"
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)


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
        ellipsoid = Ellipsoid(Vector3([0, 0, 15]), WHITE, self.camera)
        self.add_models([ellipsoid])
        self.add_callback((quit, self))


if __name__ == "__main__":
    screen_info = ie.ScreenInfo(SCREEN_WIDTH,
                                SCREEN_HEIGHT,
                                "Siminator",
                                SCREEN_COLOR)

    Inator(screen_info).run()
```
