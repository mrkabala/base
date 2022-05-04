#!/usr/bin/python3
# Author: Mike Kabala
# Date: may 3, 2022
# Version: 1.0

# Define a function to convert from any number base not greater than 36
# to another base which is also not greater than to 36.
# 
# Parameters:
#     frombase = a string representing the current base of the number
#     tobase = a string representing the number base to convert to
#     num = a string representing the number to be converted
def numconvert(frombase,tobase,num):
    # The following code converts the original number to a decimal string. 
    if (frombase != 10):
        dec = base2dec(frombase,num)
    else:
        dec = num

    # The following code converts the number from decimal 
    # to a string in the desired base.
    if (tobase != 10):
        result = dec2base(dec,tobase)
    else:
        result = dec
 
    # Return the converted number as a string. 
    return str(result)

# Define a function to convert an integer from a specified base
# to decimal.
#
# Parameters:
#     base = a string representing the base of the number
#     num = a string representing the number to be converted
def base2dec(base,num):
    # The following line defines the digits of the number base.
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # The next two lines normalize the number to uppercase
    # and initialize the multiplier to the base.
    number = num.upper()
    multiplier = int(base)

    # This line initializes the result to zero.
    dec_val = 0

    # The following loop uses the index of each digit as the decimal
    # value and adds it to the previous result times the number base,  
    for i in range(0,len(number)):
        basedigit = number[i]
        dec_val = multiplier * dec_val + digits.index(basedigit) 

    # The result is returned as a string.
    return str(dec_val)

# Define a function to convert a decimal integer to an integer
# in the specified base.
#
# Parameters:
#     num = a string representing the decimal number
#     base = a string representing the base of the desired output
def dec2base(num,base):
    # The following line defines the digits of the number base.
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # The next two lines retain the integer portion of the number entered
    # and set the divisor/modulus equal to the number base. 
    tempnumb = int(num)
    modulus = int(base)

    # This line initializes the result to an empty string.
    base_output = ""

    # The following loop repeatedly divides the number by the base,
    # placing the remainder into the result going from right to left
    # and keeping the quotient for calculating the remaining digits.
    while(tempnumb > 0):
        base_output = digits[tempnumb % modulus] + base_output
        tempnumb = int(tempnumb / modulus)

    # The result is returned as a string.
    return str(base_output)

#--------------------------------------------------------------------------
if __name__ == '__main__':
    print("dec2base(255,16) = " + dec2base(255,16))
    print ("base2dec(16,""FF"") = " + base2dec(16,"FF"))
    print("numconvert(16,8,\"FE\") = " + numconvert(16,8,"FE"))
