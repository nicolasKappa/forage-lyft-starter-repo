"""imports how service status is assesed"""

from serviceable import Serviceable

class Car(Serviceable):
    """tells if it is servicable according to engine and battery info"""
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()
    