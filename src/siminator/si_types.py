from typing import (
    Generic,
    Tuple,
    TypeVarTuple,
    final,
    TypeVar
)
from collections.abc import Callable, Sequence

import numpy as np


__all__ = [
    "PyGame",
    "pgEvent",
    "Callback",
    "pgVideoInfo",
    "ScreenInfo"
]

Args = TypeVar("Args")
PyGame = TypeVar("PyGame")
Callback = TypeVar("Callback", bound=Callable[..., None])
ArrayLike = TypeVar("ArrayLike", covariant=True, bound=(Sequence[float]|np.ndarray[float]))
ArrayLikeType = TypeVar("ArrayLikeType", covariant=True, bound=float)
ArrayLikes = TypeVarTuple("ArrayLikes")


@final
class pgEvent:
    """Pygame Event"""
    pass


@final
class pgVideoInfo:
    """Pygame Video Info"""
    hw: int
    wm: int
    video_mem: int
    bitsize: int
    bytesize: int
    masks: Tuple[int, int, int, int]
    shifts: Tuple[int, int, int, int]
    losses: Tuple[int, int, int, int]
    blit_hw: int
    blit_hw_CC: int
    blit_hw_A: int
    blit_sw: int
    blit_sw_CC: int
    blit_sw_A: int
    current_h: int
    current_w: int
    pixel_format: str


class ModelShape(np.ndarray, Generic[*ArrayLikes, ArrayLikeType]):
    def __new__(cls, input_array: ArrayLike):
        obj = np.asarray(input_array, dtype=float).view(cls)
        return obj

