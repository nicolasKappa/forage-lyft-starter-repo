"""imports ABC"""
from abc import ABC


class Battery(ABC):
    """with help of ABC defines service status"""
    def needs_service(self):
        """defines if battery needs service"""
        