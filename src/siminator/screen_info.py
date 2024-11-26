from typing import final


@final
class ScreenInfo:
    __slots__ = [
        "init_width",
        "init_height",
        "__init_title",
        "color",
        "_current_width",
        "_current_height",
        "current_title",
    ]

    def __init__(self,
                init_width: int,
                init_height: int,
                init_title: str,
                color: tuple):

        self.init_width: int = init_width
        self.init_height: int = init_height
        self.__init_title: str = init_title
        self.color: tuple = color

        self._current_width: int = self.init_width
        self._current_height: int = self.init_height
        self.current_title: str = self.__init_title

    def __str__(self):
        return self.__repr__() 

    def __repr__(self):
        return f"""ScreenInfo(init_width={self.init_width}, """\
            f"""init_height={self.init_height}, init_title={self.init_title}"""\
            f""", color={self.color}, current_width={self.current_width}, current_height={self.current_height}"""\
            f""", current_title={self.current_title}"""\

    @property
    def current_width(self):
        return self._current_width
    
    # @current_width.setter
    # def current_width(self, v):
    #     self._current_width = v

    @property
    def current_height(self):
        return self._current_height
    
    # @current_height.setter
    # def current_height(self, v):
    #     self._current_height = v

    @property
    def center(self):
        return (self.current_width//2, self.current_height//2)

    @property
    def init_title(self):
        return self.__init_title

