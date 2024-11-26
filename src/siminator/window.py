import pygame

from siminator.screen_info import ScreenInfo
from siminator.si_types import pgVideoInfo


class Window:
    def __init__(self, screen_info: ScreenInfo):
        self.infos = screen_info
        self.width = self.infos.init_width
        self.height = self.infos.init_height
        self.screen = pygame.display.set_mode((self.infos.init_width,
                                            self.infos.init_height),
                                            pygame.RESIZABLE)
        self.pg_info: pgVideoInfo = None
        self.set_title()

    def set_title(self, title: str="") -> None:
        if title:
            self.infos.current_title = title
        pygame.display.set_caption(self.infos.current_title)
    
    def update(self):
        self._update_size()
        self.width = self.infos._current_width
        self.height = self.infos._current_height

    def _update_size(self):
        self.pg_info = pygame.display.Info()
        if self.pg_info.current_h != self.infos._current_height:
            self.infos._current_height = self.pg_info.current_h
        if self.pg_info.current_w != self.infos._current_width:
            self.infos._current_width = self.pg_info.current_w


