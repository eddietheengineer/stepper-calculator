from dataclass_csv import DataclassWriter, DataclassReader
import os
from dataclasses import dataclass

filename = 'motordatabase.csv'


@dataclass
class StepperData():
    manufacturer: str = 'OMC'
    modelnumber: str = '17HS19-2004S1'
    nema: int = 17
    length: float = 48
    stepangle: float = 1.8
    ratedcurrent_amp: float = 2
    ratedtorque_ncm: float = 59
    inductance_mh: float = 3
    resistance_ohm: float = 1.4
    rotorinertia_gcm2: float = 82


class PrinterData():
    supplyvoltage: float = 24
    rotationdistance: float = 40
    targetcurrent_amp: float = 2.0


def importmotor():
    new = StepperData()
    print("Input New Stepper Motor Record")
    new.manufacturer = input('   Manufacturer: ') or 'OMC'
    new.modelnumber = input('   Model Number: ') or '17HS19-2004S1'
    new.nema = int(input('   Nema Size (14, 17, 23): ') or 17)
    new.length = float(input('   Length (mm): ') or 48)
    new.stepangle = float(input('   Step Angle (0.9, 1.8): ') or 1.8)
    new.ratedcurrent_amp = float(input('   Rated Current (A): ') or 2)
    new.ratedtorque_ncm = float(input('   Rated Torque (N-cm): ') or 59)
    new.inductance_mh = float(input('   Inductance (mH): ') or 3)
    new.resistance_ohm = float(input('   Phase Resistance (Ohm): ') or 1.4)
    new.rotorinertia_gcm2 = float(input('   Rotor Inertia (g-cm^2): ') or 82)
    writedata(new)


def writedata(newdata: StepperData):
    if os.path.isfile(filename):
        with open(filename, "a", encoding='utf-8') as f:
            w = DataclassWriter(f, [newdata], StepperData)
            w.write(skip_header=True)

    else:
        with open(filename, "w", encoding='utf-8') as f:
            w = DataclassWriter(f, [newdata], StepperData)
            w.write(skip_header=False)


def importdatabase():
    with open(filename, encoding='utf-8') as data_csv:
        reader = DataclassReader(data_csv, StepperData)
        motordatabase = []
        for row in reader:
            motordatabase.append(row)
    return motordatabase
