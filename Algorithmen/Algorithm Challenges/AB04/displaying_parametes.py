def displaying_parameters(**kwargs):
    list_elements = []
    for key, value in kwargs.items():
        print(type(value).__name__)
        key_value_pair = []
        key_value_pair.append([key, value])
        list_elements.append(key_value_pair)
    return list_elements


displaying_parameters()
