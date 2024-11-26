import typing
from collections.abc import Callable

import pygame

from siminator.drawable import Drawable
from siminator.screen_info import ScreenInfo
from siminator.si_types import pgEvent, Callback, Args
from siminator.camera import Camera
from siminator.window import Window

pygame.init()


class InatorEngine:
    """
    InatorEngine
    """
    def __init__(self, screen_info: ScreenInfo):
        # Setup window
        self.window = Window(screen_info)

        # Execution loop
        self.running = False

        # Pygame event
        self.pg_event: pgEvent = None

        # FPS
        self.clock_fps: int = 60
        self.delta_time: float = 0.0
        self.ticks: int = 0
        self.current_time: float = 0.0
        self.clock = pygame.time.Clock()
        self.last_ticks: int = 0

        # Callbacks
        self.callbacks: typing.List[typing.Tuple[Callback, Args]] = []

        # Camera
        self.camera: Camera = None
        
        # Drawables
        self._drawables: typing.List[Drawable] = []
    
    def add_models(self, models: typing.List[Drawable]) -> None:
        for m in models:
            print(m.position)
            self._drawables.append(m)

    def renderer(self) -> None:
        for i, drawable in enumerate(self._drawables):
            if drawable.to_draw:
                drawable.draw(self.current_time)

    def stop(self, pg_event: pgEvent) -> None:
        """
        Encerra a execução do Inator
        
        Args:
            pg_event (pygame.Event)
        """
        if pg_event.type == pygame.QUIT:
            self.running = False

    def timer(self) -> None:
        """
        Inicia o contador (pygame.Clock e o delta time)
        """
        self.clock.tick()
        self.ticks = pygame.time.get_ticks()
        self.current_time = self.ticks / 1000.0
        self.delta_time = (self.ticks - self.last_ticks) / 1000.0
        self.last_ticks = self.ticks

    def get_callbacks(self) -> None:
        """
        Responsável por executar todos os callbacks a cada frame
        """
        for i, callback_arg in enumerate(self.callbacks):
            callback, *args = callback_arg
            callback(*args)

    def add_callback(self, callback: typing.Tuple[Callable[typing.Concatenate[Args, ...], None]]) -> None:
        """
        Adiciona callbacks
        """
        self.callbacks.append(callback)

    def update(self) -> None:
        """
        Método que será chamado a cada frame
        """

    def start(self) -> None:
        """
        Método para fazer inicializações, chamado uma única vez
        """

    def run(self) -> None:
        """
        Executa o Inator
        """

        self.running = True

        self.start()

        while self.running:
            self.window.update()

            self.window.screen.fill((0, 0, 0))
            # self.window.screen.fill(self.screen_info.color)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                self.pg_event = event
                self.get_callbacks()

            # self.window.screen.blit(self._background, (0, 0))

            # Update
            self.update()
            
            # Render
            self.renderer()

            # Update screen all objs in the screen
            pygame.display.flip()

            # Time
            self.timer()
            # self.clock.tick(self.clock_fps)

        pygame.quit()
