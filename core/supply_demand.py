from datetime import datetime

class SupplyDemandZone:
    def __init__(self, zone_type: str, high: float, low: float, origin_time: datetime, strength: int=0):
        self.type = zone_type # supply or demand
        self.high = high
        self.low = low
        self.origin_time = origin_time
        self.strength = strength
        self.mitigated = False
        self.tests = 0