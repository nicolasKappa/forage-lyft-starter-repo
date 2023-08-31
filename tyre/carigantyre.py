from tyre.tyres import TYRE
"""imports Tyre class from tyre file"""


class CariganTyre(TYRE):
    """for only carigan_tyre system, helps when service is necessary"""
    
    def __init__(self, tyre_sensor_info):
        self.tyre_sensor_info = tyre_sensor_info

    def needs_service(self):
        total_wear = sum(self.tyre_sensor_info)
        if total_wear >= 0.9:
            return True
        else:
            return False
        