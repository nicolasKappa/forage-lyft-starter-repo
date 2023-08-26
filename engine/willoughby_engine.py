"""tells when willoughby engine should have service according to service date and milage."""

from abc import ABC

from car import Car


class WilloughbyEngine(Car, ABC):
    """tells service date and milage for Willoughby engine"""
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def engine_should_be_serviced(self) -> None:
        """tells when engine should be serviced for Willoughby engine"""
        return self.current_mileage - self.last_service_mileage > 60000
