"""imports date and data for Sternman engine on Palindrome car model"""

from datetime import datetime

from engine.sternman_engine import SternmanEngine


class Palindrome(SternmanEngine):
    """united data about Sternman engine on Palindrome car model"""
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date, current_mileage, last_service_mileage)
        self.last_service_date = last_service_date
    def needs_service(self) -> bool:
        """tells if service is needed for Sternman engine on Palindrome car model"""
        service_threshold_date = self.last_service_date.replace(
            year=self.last_service_date.year + 4)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False
