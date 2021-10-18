from abc import ABC, abstractmethod


class GeometricShape(ABC):
    """Nothing"""

    @abstractmethod
    def calculate_square(self):
        pass
