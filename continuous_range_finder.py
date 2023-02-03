def get_sorted_array(input_samples):
    input_samples.sort()
    return input_samples

def check_status_of_continuity_or_repeatidity_of_data(value):
    if(value <= 1):
        return True
    return False

def get_difference_between_the_consecutive_samples(samples , diff_of_samples):
    for i in range(len(samples) - 1):
        diff_of_samples.append(samples[i +1] - samples[i])
    diff_of_samples.insert(0 , 0)   #to make length equal to samples
    return diff_of_samples

def calculate_continuous_range(samples, continuous_range):
    continuous_range_indexes = []
    diff_of_samples = []
    sorted_samples = get_sorted_array(samples)
    diff_of_samples = get_difference_between_the_consecutive_samples(sorted_samples, diff_of_samples)
    for value in range(len(diff_of_samples)):
        if(check_status_of_continuity_or_repeatidity_of_data(diff_of_samples[value])):
            continuous_range_indexes.append(value)
        else:
            continuous_range.append([sorted_samples[continuous_range_indexes[0]], sorted_samples[continuous_range_indexes[-1]]])
            continuous_range_indexes = []
            continuous_range_indexes.append(value)
    continuous_range.append([sorted_samples[continuous_range_indexes[0]], sorted_samples[continuous_range_indexes[-1]]])
    return continuous_range

def get_continuous_range(samples):
    continuous_range = []
    if (len (samples) > 1):
        continuous_range = calculate_continuous_range(samples, continuous_range)
    return
