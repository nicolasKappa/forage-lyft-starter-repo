"""imports info how dates should be added and info about
spindel batterys service
"""

from battery.battery import Battery
from utils import add_years_to_date


class SpindlerBattery(Battery):
    """spindel batterys last service date. according to time usage
    tells wether it should be changed ot not"""
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        date_which_battery_should_be_serviced_by = add_years_to_date(self.last_service_date, 2)
        if date_which_battery_should_be_serviced_by + 1 < self.current_date:
            return True
        else:
            return False
        