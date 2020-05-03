def get_name_neatly(list_name):
    result = ""
    number_volunteer = len(list_name)
    if number_volunteer < 10:
        return "\n".join(list_name)
    cols = int(number_volunteer / 10)
    counter = 0
    for name in list_name:
        result += name + "\t"
        counter += 1
        if counter == 3:
            counter = 0
            result += "\n"
    return result
