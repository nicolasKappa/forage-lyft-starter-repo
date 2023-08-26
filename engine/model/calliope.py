"""imports date and data for Capulet engine on Calliope car model"""
from datetime import datetime

from engine.capulet_engine import CapuletEngine


class Calliope(CapuletEngine):
    """united data for Capulet engine on Calliope car model"""
    def needs_service(self: any) -> bool:
        """tells for Capulet engine on Calliope car model when service is needed"""
        service_threshold_date = self.last_service_date.replace(
            year=self.last_service_date.year + 2)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False
