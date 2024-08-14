from machine import Pin
from utime import sleep, sleep_ms
import utime

# Define pins for each segment of the 7-segment display and the decimal point (DP)
A = Pin(0, Pin.OUT)
B = Pin(2, Pin.OUT)
C = Pin(18, Pin.OUT)
D = Pin(20, Pin.OUT)
E = Pin(21, Pin.OUT)
F = Pin(1, Pin.OUT)
G = Pin(17, Pin.OUT)
DP = Pin(19, Pin.OUT)

# Define pins for each digit (assuming a 4-digit 7-segment display)
D1 = Pin(15, Pin.OUT)
D2 = Pin(14, Pin.OUT)
D3 = Pin(13, Pin.OUT)
D4 = Pin(16, Pin.OUT)

# Function to deactivate all digits (turn them off, setting them to low)
def activate_all_digits():
    D1.value(0)
    D2.value(0)
    D3.value(0)
    D4.value(0)

# Functions to display numbers 0-9 on a 7-segment display by setting segment values

# Turn on the decimal point (DP)
def dp():
    DP.value(1) 

# Display the digit '0'
def zero():
    A.value(1)
    B.value(1)
    C.value(1)
    D.value(1)
    E.value(1)
    F.value(1)
    G.value(0)
    DP.value(0)  # Optional: turn off the decimal point

# Display the digit '1'
def one():
    A.value(0)
    B.value(1)
    C.value(1)
    D.value(0)
    E.value(0)
    F.value(0)
    G.value(0)
    DP.value(0)

# Display the digit '2'
def two():
    A.value(1)
    B.value(1)
    C.value(0)
    D.value(1)
    E.value(1)
    F.value(0)
    G.value(1)
    DP.value(0)

# Display the digit '3'
def three():
    A.value(1)
    B.value(1)
    C.value(1)
    D.value(1)
    E.value(0)
    F.value(0)
    G.value(1)
    DP.value(0)

# Display the digit '4'
def four():
    A.value(0)
    B.value(1)
    C.value(1)
    D.value(0)
    E.value(0)
    F.value(1)
    G.value(1)
    DP.value(0)

# Display the digit '5'
def five():
    A.value(1)
    B.value(0)
    C.value(1)
    D.value(1)
    E.value(0)
    F.value(1)
    G.value(1)
    DP.value(0)

# Display the digit '6'
def six():
    A.value(1)
    B.value(0)
    C.value(1)
    D.value(1)
    E.value(1)
    F.value(1)
    G.value(1)
    DP.value(0)

# Display the digit '7'
def seven():
    A.value(1)
    B.value(1)
    C.value(1)
    D.value(0)
    E.value(0)
    F.value(0)
    G.value(0)
    DP.value(0)

# Display the digit '8'
def eight():
    A.value(1)
    B.value(1)
    C.value(1)
    D.value(1)
    E.value(1)
    F.value(1)
    G.value(1)
    DP.value(0)

# Display the digit '9'
def nine():
    A.value(1)
    B.value(1)
    C.value(1)
    D.value(1)
    E.value(0)
    F.value(1)
    G.value(1)
    DP.value(0)

# Function to clear the display (turn off all segments)
def clear_display():
    A.value(0)
    B.value(0)
    C.value(0)
    D.value(0)
    E.value(0)
    F.value(0)
    G.value(0)
    DP.value(0)

# Function to activate a specific digit and display a specific number
def activate_digit(digit, number_function, show_dp=False):
    for d in digits:
        d.value(1)  # Set all digits high (off)
    digit.value(0)  # Set the specific digit low (on)
    number_function()  # Display the number on the active digit
    if show_dp:
        dp()
    sleep_ms(5)  # Short delay to maintain persistence of vision
    digit.value(1)  # Turn off the digit after displaying the number

# List of digit pins and number display functions
digits = [D1, D2, D3, D4]
numbers = [zero, one, two, three, four, five, six, seven, eight, nine, dp]

# Main loop to display current hour and minute on the 7-segment display
while True:
    # Get the current hour and minute
    hour = utime.localtime()[3]
    minute = utime.localtime()[4]

    # Split the hour and minute into tens and ones digits
    h1 = hour // 10
    h2 = hour % 10
    m1 = minute // 10
    m2 = minute % 10
    
    # Display the hour and minute digits with a decimal point between hours and minutes
    activate_digit(D1, numbers[h1])
    activate_digit(D2, numbers[h2], show_dp=True)
    activate_digit(D3, numbers[m1])
    activate_digit(D4, numbers[m2])
    
    # Clear the display briefly to avoid ghosting
    clear_display()
    #sleep_ms(1)
