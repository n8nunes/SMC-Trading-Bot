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

    def is_valid(self, current_price: float) -> bool:
        '''
        Check if zone is still valid (unmitigated)
        '''

        if self.mitigated:
            return False
        
        if self.type == 'demand':
            if current_price <= self.high:
                self.mitigated = True
                return False
            
        else: # supply
            if current_price >= self.low:
                self.mitigated = True
                return False
        
        return True