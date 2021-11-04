from typing import Iterable, Tuple
import math


def convert_to_celsius(fahrenheit_temp: float) -> float:
    """
    Given a float representing a temperature in fahrenheit, return the corresponding value in celsius.

    :param fahrenheit_temp: A float representing a temperature in fahrenheit
    :return: A float representing the corresponding value of the fahrenheit_temp parameter in celsius
    """
    form = fahrenheit_temp - 32
    new_celc = float(form / 1.8000)
    return math.ceil(new_celc*100)/100



def convert_to_fahrenheit(celsius_temp: float) -> float:
    """
    Given a float representing a temperature in celsius, return the corresponding value in fahrenheit.

    :param celsius_temp: A float representing a temperature in celsius
    :return:  A float representing the corresponding value of the celsius_temp parameter in fahrenheit
    """
    form = celsius_temp * 1.8000
    new_celc = float(form + 32)
    return math.ceil(new_celc * 10000) / 10000


def temperature_tuple(temperatures: Iterable, input_unit_of_measurement: str) -> Tuple[Tuple[float, float]]:
    """
    Given a tuple or a list of temperatures, this function returns a tuple of tuples.
    Each tuple contains two values. The first is the value of the temperatures parameter. The second is the the value of
    the first converted to the unit of measurement specified in the input_unit_of_measurement parameter.

    :param temperatures: An iterable containing temperatures
    :param input_unit_of_measurement: The unit a measure to use to convert the values in the temperatures parameter
    :return: A tuple of tuples
    """
    while True:
        for element in temperatures:
            tuple = ''
            if input_unit_of_measurement == 'celsius':
                form = element - 32
                new_celc = float(form / 1.8000)
                formated_celc = math.ceil(new_celc * 100) / 100
                new = element, formated_celc
                return tuple, new
            elif input_unit_of_measurement == 'fahrenheit':
                form = element * 1.8000
                new_fahr = float(form + 32)
                formated_fahr = math.ceil(new_fahr * 10000) / 10000
                new = element, formated_fahr
                return(new + (element, formated_fahr))




temps_input = (32, 68, 100, 104)
print(temperature_tuple(temps_input, 'celsius'))