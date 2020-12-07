#!/usr/bin/env python3


freq_test = 1900   # used to find power, with this val, as the given freq.
freq_near = 1740   # used for finding the nearest frequency test.


freq_power_set = [(700, -5), (800, -4), (850, -2), (1700, -1), (1900, 1), (2300, 3), (2500, 5)]


def find_power(fr_map, f):
    for i in fr_map:
        if i[0] == f:
            return i[1]


def find_power_with_list_compr(fr_map, f):
    # same soluiton as find_power, but using a list comprehension.
    #print("With list comprehension and convert one-element-list to number representing freq")
    #  One liner: alternatively we could use second line to convert 0th element in the list to integer.
    return([i[1] for i in fr_map if i[0] == f][0])


def find_closest(fr_map, f):
    min_diff = 9999
    
    # if the value is not in the list, use find_closest()
    for i in fr_map:
        if (abs(i[0]-freq_near) < min_diff):
            min_diff = abs(i[0]-freq_near)
            #freq = i[0]
            powr = i[1]
    return powr



pwr = find_power(freq_power_set, freq_test)
print(pwr)


pwr = find_power_with_list_compr(freq_power_set, freq_test)
print(pwr)


pwr = find_closest(freq_power_set, freq_near)
print(pwr)


# PyTest example:
# Use "pytest" to call the below function(s):
# This will get executed if we call using, "pytest freq_power.py"


def test_basic_assert():
    assert(2+2 == 4)

def test_verify_freq_in_list():
    assert(freq_power_set[4][1] == find_power(freq_power_set, 1900))




