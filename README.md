# Simple two-level temperature controller

Copyright 2020 Maria-Luisa Brüser

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

## Description
This repo was created as a homework for a class of on Open Source Energy Modeling (May 2020)

The code descripts a simple two-level temperature controller. The functions can be used for the first laboratory excercise for the lecture "Automatisierungs- und Steuerungssysteme" at TU Vienna. 

The code consists of 2 functions: The "conversion_values" function allows you to convert the analog signal of an external temperatur sensor into the physical measured value in °C. As the laboratory has two different models of senors, you can choose whether you are working with VT_1 or VT_2. As input you need to know with which model you are working (VT1 or VT2), what temperatures are wished for and you need to import the analog sigal from the temperature senor. 
The secound function "temperature_controller" is the temperture controller itself. It sets the Heater on ON or OFF. As an input it gets the signal if the Heater is already on (True or False), the physical value of the temperature from the "conversion_values" function, the wished for temperture and the range of temperature for the hysteresis.
