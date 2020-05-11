## Conversions between the PLC analog input data of sensor and the physical measured values 

#Chosing construction model (2 different models in the laboratory), If VT1 choose true, if VT2 choose false! 
#tempV1 and tempV1 are defined temperture for each model, the temperature that should be reached
#temp_should are the PLC analog input data of sensor - needs to be imported 
# Output are the physical value of temperature in °C and wished for temperature depending on model


def conversion_values(VT_1, tempV1,tempV2, temp_measured):
    if VT_1 == True:
        temp_should = tempV1
        temp = temp_measured/320
    else:
        temp_should = tempV2
        temp = temp_measured / (100 + 10 / 3)
    return [temp, temp_should]

## Temperature Controller with hysteresis (range)

# heating_ON checks current status for heating Unit: True if ON, False if Heating Off
# temp and temp_should should be taken from previous function - no new input
# temperture range defines to hysteresis of the controller
# Output of the function is the signal to heater if ON or OFF


def temperature_controller(heating_ON, temp, temp_should, temp_range):
    if  heating_ON == False and temp < (temp_should - temp_range):
        heating_ON = True
    elif heating_ON == True and temp > (temp_should + temp_range):
        heating_ON = False
    return heating_ON


