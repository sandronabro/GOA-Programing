#1
def find_needle(haystack):
    i=0
    while i<len(haystack):
        if haystack[i]=="needle":
            return "found the needle at position " + str(i)
        i+=1

#2
def make_upper_case(s):
    return s.upper()

#3
def sum_array(a):
    return sum(a)

#4
def are_you_playing_banjo(name):
    if name[0] == "r" or name[0] == "R":
        return str(name) + " plays banjo"
    else:
        return str(name) + " does not play banjo"
    
#5
def invert(lst):
    return[num * -1 for num in lst]