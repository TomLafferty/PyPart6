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




def convert_to_kelvin(celsius_temp: float) -> float:
    form = celsius_temp + 273.15
    new_celc = float(form)
    return math.ceil(form*100)/100

# form = fahrenheit_temp - 32
#     new_celc = float(form / 1.8000)
#     return math.ceil(new_celc*100)/100

def temperature_tuple(temperatures, input_unit_of_measurement):

    answer = []
    temp_tup = tuple()
    for i in temperatures:

        if input_unit_of_measurement == 'c':
            converted_temp = convert_to_fahrenheit(i)

        elif input_unit_of_measurement == 'f':
            converted_temp = convert_to_celsius(i)

        elif input_unit_of_measurement == 'k':
            converted_temp = convert_to_kelvin(i)

        else:
            break

        temp_tup = (i, converted_temp)
        answer.append(temp_tup)

    return tuple(answer)