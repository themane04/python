def displaying_parameters(**kwargs):
    list_elements = []
    for key, value in kwargs.items():
        type_name = type(value).__name__
        key_value_pair = [type_name, value]
        list_elements.append(key_value_pair)
    return list_elements


print(displaying_parameters(arg1="Hi", arg2=True, arg3=42, arg4=0.6))
