import numpy as np
from siminator.si_types import ArrayLike

class Vector3(np.ndarray):
    def __new__(cls, input_array: ArrayLike):
        shape = 3
        dtype = float
        input_array = input_array[: shape]
        obj = np.asarray(input_array, dtype=dtype).view(cls)
        obj.__x = obj[0]
        obj.__y = obj[1]
        obj.__z = obj[2]
        return obj
    def __array_finalize__(self, obj):
        if obj is None:
            return
        self.__x: float = getattr(obj, 'x', None)
        self.__y: float = getattr(obj, 'y', None)
        self.__z: float = getattr(obj, 'z', None)

    def cross(self, array, **unused_kwargs):
        return np.cross(self, array).view(Vector3)

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, v):
        self.__x = v
        self[0] = v
        
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, v):
        self.__y = v
        self[1] = v

    @property
    def z(self):
        return self.__z

    @z.setter
    def z(self, v):
        self.__z = v
        self[2] = v


