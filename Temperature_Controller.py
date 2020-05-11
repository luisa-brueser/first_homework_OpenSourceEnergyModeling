# Measured Temperature from Sensor, Input variable
#temp_measured = 2000 
# Output variable to heating Unit, True if on, False if Heating Off
#heating_ON = False

# Definition of tempertures
#tempV1 = 25
#tempV2 = 28
#temp_should = 0


# Definition of hysteresis 
#temp_range= 0.5

# Chosing construction model (2 different models in the laboratory), If VT1 choose true, if VT2 choose false!
#VT_1 = True

#Conversions between the PLC analog input data and the physical measured values

def conversion_values(VT_1, tempV1,tempV2, temp_measured):
    if VT_1 == True:
        temp_should = tempV1
        temp = temp_measured/320
    else:
        temp_should = tempV2
        temp = temp_measured / (100 + 10 / 3)
    return [temp, temp_should]


def temperature_controller(heating_ON, temp, temp_should, temp_range):
    if  heating_ON == False and temp < (temp_should - temp_range):
        heating_ON = True
    elif heating_ON == True and temp > (temp_should + temp_range):
        heating_ON = False
    return heating_ON


