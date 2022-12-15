from __future__ import annotations
from dataclasses import dataclass



@dataclass
class Point:
    x: int
    y: int

    def __lt__(self, other: Point) -> bool:
        return (self.y, self.x) < (other.y, other.x)

    def __sub__(self, p: Point) -> Point:
        return Point(self.x - p.x, self.y - p.y)

    def len2(self) -> int:
        return self.x * self.x + self.y * self.y


def cross_product(p1: Point, p2: Point, p3: Point) -> int:
    # calculates z-coordinate of cross product of vectors p1p2 and p1p3
    # clock wise direction will be negative and the output will be True
    # (p2-p1) * (p3-p1)
    return (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x)


def mapping_point(p: Point) -> list:
    return [p.x, 800 - p.y]
