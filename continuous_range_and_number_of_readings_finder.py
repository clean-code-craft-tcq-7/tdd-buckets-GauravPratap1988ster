from validate_input_data import check_input_data_is_ok
from continuous_range_finder import get_continuous_range
from number_of_readings_in_continuous_range_finder\
    import get_number_of_readings_in_continuous_range
from output_in_csv_format import create_csv_format_string


def get_continuous_range_and_number_of_readings_and_generate_output(samples):
    continuous_range = []
    number_of_readings = []
    csv_output = ""
    if (check_input_data_is_ok(samples)):
        continuous_range = get_continuous_range(samples)
        number_of_readings = get_number_of_readings_in_continuous_range(continuous_range)
        csv_output = create_csv_format_string(continuous_range, number_of_readings)
        print(csv_output)
    return (continuous_range, number_of_readings)
