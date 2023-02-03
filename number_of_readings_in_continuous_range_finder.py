def get_number_of_readings_in_continuous_range(continuousrange):
    number_of_readings = []
    for value in continuousrange:
        number_of_readings.append(value[1] - value[0] + 1)
    return number_of_readings
