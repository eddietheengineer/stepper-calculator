import numpy as np


def f_coil(stepper_rps: float, stepper_degrees: float, steps_cycle=4):
    """ Return the electrical frequency for the stepper motor

    Parameters:
    ----------------
        stepper_rps: float
            The stepper motor rotational speed in revolutions per second
        stepper_degrees: float
            The stepper motor step angle in degrees (ie, 0.9 or 1.8)
        steps_cycle: int
            The number of steps per full electrical cycle (ie, 4 for bipolar steppers)

    Return:
    ----------------
        coil_frequency: float
            The frequency of the electrical signal in Hz
    """
    f_coil = stepper_rps * (360 / stepper_degrees)/steps_cycle
    return f_coil


def x_coil(stepper_inductance: float, coil_frequency: float):
    """ Return the inductive reactance X_L of a stepper motor
    https://www.electronics-tutorials.ws/accircuits/ac-inductance.html

    Parameters:
    ----------------
        stepper_inductance: float
            The inductance of the stepper motor coil in mH
        coil_frequency: float
            The frequency of the electrical signal in Hz

    Return:
    ----------------
        X: float
            The inductive reactance of the coil in Ohms
    """
    x_coil = 2 * np.pi * coil_frequency * stepper_inductance / 1000
    return x_coil


def z_coil(XL: float, R: float):
    """ Return the total Z impedance of the coil
    https://www.allaboutcircuits.com/textbook/alternating-current/chpt-3/ac-resistor-circuits-inductive/

    Parameters:
    ----------------
        XL: float
            The  inductive reactance of the stepper coil
        R: float
            The resistance of the stepper motor coil

    Return:
    ----------------
        Z: float
            The impedance of the stepper motor coil
    """
    Z = np.sqrt(XL**2 + R**2)
    return Z


def v_gen(rps, ratedcurrent_A, ratedtorque_Ncm):
    """ Return the generated backemf voltage 
    https://www.oyostepper.com/article-1102-Back-emf-due-to-rotation-of-stepper-motor.html
    Parameters:
    ----------------
        rps: float
            The stepper motor rotational speed in revolutions per second
        ratedcurrent_A: float
            The rated current in Amps
        ratedtorque_Ncm: float
            The rated tqrue in Ncm

    Return:
    ----------------
        backemf_peakV: float
            The peak backemf due to rotation in Volts
    """
    ratedtorque_Nm = ratedtorque_Ncm / 100
    omega = 2 * np.pi * rps
    # Assume rated torque is with both coils energized = use sqrt(2)
    # If only one coil is energized for datasheed, do not divide by sqrt(2)
    v_gen = omega * ratedtorque_Nm / ratedcurrent_A / np.sqrt(2)
    return v_gen


def i_actual(v_supply: float, v_gen: float, z_coil: float, i_target: float):
    """ Return the actual current going through the windings
    Parameters:
    ----------------
        v_supply: float
            The power supply voltage in Volts
        v_gen: float
            The backemf voltage in Volts
        z_coil: float
            The impedance of the stepper coil in Ohms
        i_target: float
            The target current in Amps

    Return:
    ----------------
        i_actual: float
            The actual current through the stepper windings in Volts
    """
    v_available = v_supply - v_gen
    i_available = v_available/z_coil
    i_actual = min(i_available, i_target)
    return i_actual


def torque(i_rated: float, i_actual: float, ratedtorque_Ncm: float):
    """ Return the actual torque output of the stepper motor
    Parameters:
    ----------------
        i_rated: float
            The rated current in Amps
        i_actual: float
            The actual current in Amps
        ratedtorque_Ncm: float
            The rated torque in Ncm

    Return:
    ----------------
        torque: float
            The actual torque output of the stepper motor in Ncm
    """
    torque_ratio = i_actual/i_rated
    torque_1coil = torque_ratio * ratedtorque_Ncm / np.sqrt(2)
    return torque_1coil