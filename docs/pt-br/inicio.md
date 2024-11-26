## Exemplo

```python
import pygame
import siminator as si

# Colors
WHITE = (255, 255, 255)

# Callbacks
def quit(self: si.InatorEngine):
    """custom exit"""
    if self.pg_event.type == pygame.KEYDOWN:
        if self.pg_event.key == pygame.K_ESCAPE:
            self.running = False


class MyInator(si.InatorEngine):
    def start(self):
        self.camera = si.Camera(si.Vector3([0, 0, 20]), self.window, 700)
        ellipsoid = si.Ellipsoid(si.Vector3([0, 0, 15]), WHITE, self.camera)
        self.add_models([ellipsoid])
        self.add_callback((quit, self))


if __name__ == "__main__":
    screen_info = si.ScreenInfo(600, 600, "Siminator", "#DCDDD8")
    Inator(screen_info).run()
```
