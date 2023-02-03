def create_csv_format_string(continuous_range, number_of_readings):
    csv_string = "Range, Readings"
    for value in range(len(continuous_range)):
        value_key = "{}-{}".format(continuous_range[value][0],continuous_range[value][1])
        csv_string += "\n{}, {}".format(value_key, number_of_readings[value])

    return csv_string
