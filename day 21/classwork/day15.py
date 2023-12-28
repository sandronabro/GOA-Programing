def abbrev_name(name):
    words = name.split()
    first_name = words[0][0].upper()
    last_name = words[-1][0].upper()
    return str(first_name+"."+last_name)


result = abbrev_name("Sandro Zabakhidze")
print(result)