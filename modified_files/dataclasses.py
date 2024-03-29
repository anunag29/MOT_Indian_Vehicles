from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple
import numpy as np

@dataclass
class Point:
    x: float
    y: float

    def as_xy_int_tuple(self) -> Tuple[int, int]:
        return int(self.x), int(self.y)

    def as_xy_float_tuple(self) -> Tuple[float, float]:
        return self.x, self.y


@dataclass
class Vector:
    start: Point
    end: Point

    def magnitude(self):
        return np.sqrt(((self.end.x - self.start.x)**2) + ((self.end.y - self.start.y)**2))

    def is_in(self, point: Point) -> bool:
        v1 = Vector(self.start, self.end)
        v2 = Vector(self.start, point)
        cross_product = (v1.end.x - v1.start.x) * (v2.end.y - v2.start.y) - (
            v1.end.y - v1.start.y
        ) * (v2.end.x - v2.start.x)
        return cross_product < 0


@dataclass
class Rect:
    x: float
    y: float
    width: float
    height: float

    @property
    def top_left(self) -> Point:
        return Point(x=self.x, y=self.y)

    @property
    def bottom_right(self) -> Point:
        return Point(x=self.x + self.width, y=self.y + self.height)

    def pad(self, padding) -> Rect:
        return Rect(
            x=self.x - padding,
            y=self.y - padding,
            width=self.width + 2 * padding,
            height=self.height + 2 * padding,
        )
