import formulas as fp
import numpy as np
from dataclasses import dataclass


@dataclass
class StepperData():
    manufacturer: str = ''
    modelnumber: str = ''
    nema: int = 0
    length: float = 0
    stepangle: float = 0
    ratedcurrent_amp: float = 0
    ratedtorque_ncm: float = 0
    inductance_mh: float = 0
    resistance_ohm: float = 0
    rotorinertia_gcm2: float = 0
    datasheet: str = ''
