#!/usr/python
#polar conversion with calculator
#DerrickElliott
#does conversions of first calculator plus Polar and Rectangular electrical measurements 
import math

pi = 3.141529

def complexAdd(a, b):
    realAnswer = a[0] + b[0] 
    imagAnswer = a[1] + b[1] 
    return (realAnswer, imagAnswer)


def complexSub(a, b):
    realAnswer = a[0] - b[0]
    imagAnswer = a[1] - b[1]
    return (realAnswer, imagAnswer)


def complexMult(a, b):
    realAnswer = a[0] * b[0]
    imagAnswer = a[1] + b[1]
    return (realAnswer, imagAnswer)



def complexDiv(a, b):
    realAnswer = a[0] / b[0]
    imagAnswer = a[1] - b[1]
    return (realAnswer, imagAnswer)

def rect_to_polar(x, y):

    angle = math.atan((y/x))

    angle = angle * (180/pi)

    magnitude = (math.sqrt((x*x)+(y*y)))

    answer = magnitude, angle

    return answer



# Polar to Rect conversion. Takes a polar format number( r, theta) and returns the x & y lengths



def polar_to_rect(polar_num):

    y = polar_num[0] * (math.sin(polar_num[1] * pi/180))

    x = polar_num[0] * (math.cos(polar_num[1] * pi/180))

    rect = x, y

    return rect



# Magnitude function for later use. Takes a real + j number and returns the magnitude

def magnitude(number):

    absolute = math.sqrt((number[0] * number[0]) + (number[1]* number[1]))

    return absolute



# coordinate_system = raw_input('Hello my Dude! Shall you be working in rectangular or polar format today?:\n')

print('For this particular experiment, I (the pi) am only capable of series AC calculations with one R, L & C.\n')

frequency = input('\nWhat is the frequency of the source? (in Hz): ')

voltage = input('\nWhat is the voltage of the source? (in RMS): ')

resistor_value = input('\nWhat value of resistor is present? (in Ohms): ')

inductor_value = input('\nWhat is the value of your inductor? (in Henrys): ')

capacitor_value = input('\nWhat is the value of your capacitor? (in Farads): ')



#calculations

omega = 2 * pi * frequency

inductance = omega * inductor_value

capacitance = (1/(omega * capacitor_value))

impedance = resistor_value, (inductance + -capacitance)

mag_impedance = magnitude(impedance)

current = float(voltage) / float(mag_impedance)

v_r = current * resistor_value

v_l = current * inductance

v_c = current * capacitance

# Phase angle calculations (tests for positive/negative phase

if inductance > capacitance:

    argument_send = impedance[1] / impedance[0]

else:

    if capacitance > inductance:

        argument_send = impedance[0] / impedance[1]

    else:

        argument_send = 0



phase_radians = math.atan(argument_send)

phase_angle = phase_radians * 180/pi



# Printing out the results

if capacitance > inductance:

    print('Your current will lead your voltage by %f degrees ' % phase_angle)

if inductance > capacitance:

    print('Your current will lag your voltage by %f degrees' % phase_angle)

print('\nYour total impedance is: %.2f + %.2fj' % (impedance[0], impedance[1]))

print('That means the magnitude of your impedance is: %.2f' % mag_impedance)

print('Which then means your current is: %f A' % current)

print('V(R) = %.2f, V(L) = %.2f, V(C) = %.2f' % (v_r, v_l, v_c))
