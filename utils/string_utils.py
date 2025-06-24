def capitalize_first_letter(string):
    """
    Capitalize the first letter of a string
    """
    return string[0].upper() + string[1:]

def capitalize_last_letter(string):
    return string[:-1] + string[-1].upper()

def capitalize_first_and_last_letter(string):
    return string[0].upper() + string[1:-1] + string[-1].upper()
