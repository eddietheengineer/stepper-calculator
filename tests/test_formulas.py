# test formulas.py
import formulas as fp

def test_f_coil():
    assert fp.f_coil(3, 1.8, 4) == 150
    assert fp.f_coil(17, 1.8) == 850

def test_x_coil():
    assert round(fp.x_coil(3, 150),2) == 2.83

def test_z_coil():
    assert round(fp.z_coil(8.4823, 1.4), 3) == 8.597

def test_v_gen():
    assert round(fp.v_gen(20, 2, 59),2) == 26.21

def test_i_actual():
    assert round(fp.i_actual(24, 15.73, 11.40, 1.2),2) == 0.73

def test_torque():
    assert round(fp.torque(2, 0.92, 59),2) == 19.19