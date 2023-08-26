"""tells when sterman engine should have service according to service date and milage."""

from abc import ABC

from car import Car


class SternmanEngine(Car, ABC):
    """tells service date and warning light status for Sterman engine"""
    def __init__(self, last_service_date, warning_light_is_on):
        super().__init__(last_service_date)
        self.warning_light_is_on = warning_light_is_on

    def engine_should_be_serviced(self) -> bool:
        """tells when engine should be serviced for sterman engine."""
        if self.warning_light_is_on:
            return True
        else:
            return False
