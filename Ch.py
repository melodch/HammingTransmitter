import numpy as np
import random


def finding_bit_prob_error(total_p):
    """Finding bit probability error given we want 1 error in 4 bits"""
    p = 1 - 0.97372
    return p


def channel(half_byte, bit_prop_error):
    """ Use probability to indroduce one error
    
        Args: 
            half_byte: 4 bit number  
            bit_prop_error: bit probability error which between 0 adn 1
        Returns : 4 bit number with one error introduced
    """
    
    # Converting to list
    lst_byte = list(map(int, half_byte))    
    
    # Flipping the bits with the calculated probability
    for i in range(len(lst_byte)):
        if random.random() <= bit_prop_error:
            lst_byte[i] = (lst_byte[i] + 1) % 2

    # Converting integer list to string list
    s = [str(i) for i in lst_byte]      
    # Join list items using join()
    error_bit = "".join(s)
    return error_bit


def rand_key(p):
    """ Function to create the random binary string"""
   
    # Variable to store the
    # string
    key1 = ""

    # Loop to find the string
    # of desired length
    for _ in range(p):         
        # randint function to generate
        # 0, 1 randomly and converting
        # the result into str
        temp = str(random.randint(0, 1))
 
        # Concatenation the random 0, 1
        # to the final result
        key1 += temp         
    return(key1)

def check_error(og_bit, error_bit):
    """ Check the number of places where the two bits differ"""
    return sum ( og_bit[i] != error_bit[i] for i in range(len(og_bit)) )

    
    
num_errors = 0
num_half_bytes = 200
for _ in range(num_half_bytes):
    og_bit = rand_key(4)
    error_bit = channel(og_bit, finding_bit_prob_error(0.996))
    num_errors += check_error(og_bit, error_bit)
    print("Original bit: ", og_bit, " Error bit: ", error_bit)
print("Number of bits with an error: ", num_errors, "for ", num_half_bytes)




        
        



