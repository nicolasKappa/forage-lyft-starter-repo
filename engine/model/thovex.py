"""imports date and data for Capulet engine on Thovex car model"""

from datetime import datetime

from engine.capulet_engine import CapuletEngine


class Thovex(CapuletEngine):
    """united data for for Capulet engine on Thovex car model"""
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date, current_mileage, last_service_mileage)
        self.last_service_date = last_service_date

    def needs_service(self):
        """tells if service is needed for Capulet engine on Thovex car model"""
        service_threshold_date = self.last_service_date.replace(
            year=self.last_service_date.year + 4)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False
