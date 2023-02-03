from validate_input_data import check_input_data_is_ok
from continuous_range_finder import get_continuous_range,\
    get_sorted_array, check_status_of_continuity_or_repeatidity_of_data,\
        get_difference_between_the_consecutive_samples,\
            calculate_continuous_range
from number_of_readings_in_continuous_range_finder\
    import get_number_of_readings_in_continuous_range
from continuous_range_and_number_of_readings_finder\
    import get_continuous_range_and_number_of_readings_and_generate_output
from output_in_csv_format import create_csv_format_string

# check validity of data
assert check_input_data_is_ok([]) == True
assert check_input_data_is_ok('') == False

#continuous range test
assert get_continuous_range([]) == []
assert get_continuous_range([1]) == []
assert get_continuous_range([4, 5]) == [[4, 5]]
assert get_continuous_range([4, 5, 6]) == [[4, 6]]
assert get_continuous_range([4, 6, 5, 7]) == [[4, 7]]
assert get_continuous_range([4, 5, 6, 9, 8, 10]) == [[4, 6], [8, 10]]

#Refactored continuous range test
assert get_sorted_array([]) == []
assert get_sorted_array([1]) == [1]
assert get_sorted_array([4, 5]) == [4, 5]
assert get_sorted_array([4, 6, 5, 7]) == [4, 5, 6, 7]

assert check_status_of_continuity_or_repeatidity_of_data(4) == False
assert check_status_of_continuity_or_repeatidity_of_data(1) == True

assert get_difference_between_the_consecutive_samples([4, 5], []) == [0, 1]
assert get_difference_between_the_consecutive_samples([4, 5, 6], []) == [0, 1, 1]
assert get_difference_between_the_consecutive_samples([4, 5, 6, 8, 9, 10], []) == [0, 1, 1, 2, 1, 1]

assert calculate_continuous_range([4, 5], []) == [[4, 5]]
assert calculate_continuous_range([4, 5, 6], []) == [[4, 6]]
assert calculate_continuous_range([4, 6, 5, 7], []) == [[4, 7]]
assert calculate_continuous_range([4, 5, 6, 9, 8, 10], []) == [[4, 6], [8, 10]]


#number of readings test
assert get_number_of_readings_in_continuous_range([]) == []
assert get_number_of_readings_in_continuous_range([[4, 5]]) == [2]
assert get_number_of_readings_in_continuous_range([[4, 6]]) == [3]
assert get_number_of_readings_in_continuous_range([[4, 7]]) == [4]
assert get_number_of_readings_in_continuous_range([[4, 6] , [8, 10]]) == [3, 3]

#creating output in csv format test
assert create_csv_format_string([[4, 5]], [2]) == "Range, Readings\n4-5, 2"
assert create_csv_format_string([[4, 5], [7, 8]], [2, 2]) == "Range, Readings\n4-5, 2\n7-8, 2"

#continuous_range_and_number_of_readings test
assert get_continuous_range_and_number_of_readings_and_generate_output([]) == ([],[])
assert get_continuous_range_and_number_of_readings_and_generate_output('') == ([],[])
assert get_continuous_range_and_number_of_readings_and_generate_output([1]) == ([],[])
assert get_continuous_range_and_number_of_readings_and_generate_output([4, 5]) == ([[4, 5]],[2])
assert get_continuous_range_and_number_of_readings_and_generate_output([4, 5, 6]) == ([[4, 6]],[3])
assert get_continuous_range_and_number_of_readings_and_generate_output([4, 6, 5, 7]) == ([[4, 7]],[4])
assert get_continuous_range_and_number_of_readings_and_generate_output([4, 5, 6, 9, 8, 10]) == ([[4, 6], [8, 10]],[3, 3])
