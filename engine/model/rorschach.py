"""imports date and data for Willoughby engine on Rorschach car model"""

from datetime import datetime

from engine.willoughby_engine import WilloughbyEngine


class Rorschach(WilloughbyEngine):
    """united data for Willoughby engine on Rorschach car model"""
    def needs_service(self) -> bool:
        """tells if service is needed for Willoughby engine on Rorschach car model"""
        service_threshold_date = self.last_service_date.replace(
            year=self.last_service_date.year + 4)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False
