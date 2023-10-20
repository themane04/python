def splitlist(mixed_list):
    result_dict = {}
    for element in mixed_list:
        element_type = type(element)
        if element_type in result_dict:
            result_dict[element_type].append(element)
        else:
            result_dict[element_type] = [element]
    return result_dict

mixedlist = [1,4,"Hallo",3.5,False,2,True,"Cat"]
lists = splitlist(mixedlist)
print(lists)