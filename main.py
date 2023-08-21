from formulas import calctorque
import numpy as np
import matplotlib.pyplot as plt
from input import StepperData, PrinterData, importdatabase


def generateaxis(lowspeed: int, highspeed: int):
    speedaxis = range(lowspeed, highspeed)
    return speedaxis


def calculatetorquearray(stepper: StepperData, printer: PrinterData, speedaxis):
    torque = []
    for _, mms in enumerate(speedaxis):
        torque.append(calctorque(stepper, printer, mms))
    plt.plot(speedaxis, torque,
             label=f'{stepper.manufacturer} {stepper.modelnumber}')


def plotall():
    speed = generateaxis(0, 1000)
    motordatabase = importdatabase()

    plt.rcParams['figure.figsize'] = [8, 4.5]
    plt.margins(0)
    plt.grid(visible=True)

    for _, stepper in enumerate(motordatabase):
        calculatetorquearray(stepper, printertest, speed)

    plt.legend(fontsize=4)
    plt.title('Torque vs Speed')
    plt.xlabel('Speed (mm/s)')
    plt.ylabel('Torque (N-cm)')
    plt.ylim(bottom=0, top=100)
    plt.savefig('Testimage.png', dpi=240)
    plt.clf()
    plt.close()


printertest = PrinterData()
plotall()
