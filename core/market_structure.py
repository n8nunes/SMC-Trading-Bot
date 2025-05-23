# core/market_structure.py
from dataclasses import dataclass
from typing import Tuple, List, Dict
import datetime

@dataclass
class StructurePoint:
    price: float
    time: datetime
    type: str # high or low
    degree: str # swing, internal, fractal