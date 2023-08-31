"""imports ABC"""
from abc import ABC, abstractmethod


class Serviceable(ABC):
    """with help of ABC defines service status"""
    @abstractmethod
    def needs_service(self):
        """tells if car needs service"""
        pass
