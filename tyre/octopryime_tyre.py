"""imports Tyre class from tyre file"""

from tyre.tyres import TYRE

class OctopryimeTyre(TYRE):
    """octopryme tyre sensor data for service""" 
    def __init__(self, tyre_sensor_info):
        self.tyre_sensor_info = tyre_sensor_info

    def needs_service(self) -> bool:
        total_wear = sum(self.tyre_sensor_info)
        if total_wear >= 3.0:
            return True
        else:
            return False
        