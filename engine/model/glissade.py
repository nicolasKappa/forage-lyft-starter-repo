"""imports date and data for Willoughby engine on Glissade car model"""

from datetime import datetime

from engine.willoughby_engine import WilloughbyEngine


class Glissade(WilloughbyEngine):
    """united data for Willoughby engine on Glissade car model"""
    def needs_service(self: any) -> bool:
        """tells if service is needed for Willoughby engine on Glissade car model"""
        service_threshold_date = self.last_service_date.replace(
              year=self.last_service_date.year + 2)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False
