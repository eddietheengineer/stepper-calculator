from main import StepperData
from dataclass_csv import DataclassWriter
import os

filename = 'motordatabase.csv'


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
    new.datasheet = input(
        '   Datasheet URL: ') or 'https://www.omc-stepperonline.com/download/17HS19-2004S1.pdf'
    writedata(new)


def writedata(newdata: StepperData):
    if os.path.isfile(filename):
        with open(filename, "a") as f:
            w = DataclassWriter(f, [newdata], StepperData)
            w.write(skip_header=True)

    else:
        with open(filename, "w") as f:
            w = DataclassWriter(f, [newdata], StepperData)
            w.write(skip_header=False)
