from dataclasses import dataclass
from datetime import datetime

@dataclass
class InputRead:
    value: float
    timestamp: datetime
    source: str

@dataclass
class AggregtedRead:
    mean_value: float
    change_rate: float
    source: str
