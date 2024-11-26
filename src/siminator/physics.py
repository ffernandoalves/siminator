from siminator import Vector3
from siminator import Model


class Particle:
    mass: float
    force: Vector3
    velocity: Vector3
    position: Vector3
    init_position: Vector3


class DeformableModel(Model):
    pass


class ApplyPhysic:
    def __init__(self):
        pass