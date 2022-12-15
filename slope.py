from __future__ import annotations
from fractions import Fraction
from dataclasses import dataclass

@dataclass
class Slope:
    dx: int
    dy: int
    
    def __lt__(self, other: Slope) -> bool:  # True means that self is less than other
        if self.dx * other.dx < 0:  # one of the slopes has negative dx
            return self.dx > 0
        if self.dx * other.dx > 0:
            return Fraction(self.dy/self.dx) < Fraction(other.dy/other.dx)
        if self.dx == 0:
            return other.dx < 0
        if other.dx == 0:
            return self.dx > 0

    def __eq__(self, other: Slope) -> bool:
        if self.dx * other.dx < 0:
            return False
        if self.dx * other.dx > 0:
            return Fraction(self.dy/self.dx) == Fraction(other.dy/other.dx)
        return self.dx == 0 and other.dx == 0
