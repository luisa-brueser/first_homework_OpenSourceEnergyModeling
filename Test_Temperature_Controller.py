from utils import conversion_values, temperature_controller

def test_conversion():
    assert conversion_values(True, 25, 28, 8320) [0] == 26
    assert conversion_values(True, 25, 28, 8320) [1] == 25


outputs_conversion = conversion_values(True, 25, 28, 8320)
temp=outputs_conversion[0]
temp_should=outputs_conversion[1]

    
def test_controller():
    assert temperature_controller(True, temp, temp_should, 0.5) == False
  