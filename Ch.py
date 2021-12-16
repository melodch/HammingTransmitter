import numpy as np
import random

def finding_bit_prob_error(p_total):
    """Finding bit probability error given we want 1 error in 4 bits
        Look at prob_math.jpg"""
    p = 1 - 0.97854
    return p

def channel(seven_bit, bit_prop_error):
    """ Use probability to indroduce one error
    
        Args: 
            half_byte: 7 bit list  
            bit_prop_error: bit probability error which between 0 adn 1
        Returns : 7 bit number with one error introduced
    """    
    # Flipping the bits with the calculated probability
    error_bit = []
    for i in range(len(seven_bit)):
        if random.random() <= bit_prop_error:
            error_bit.append((seven_bit[i] + 1) % 2) 
        else:
            error_bit.append(seven_bit[i])
    return error_bit

def rand_key(p):
    """ Function to create the random binary string"""
   
    # Variable to store the
    # string
    key1 = []

    # Loop to find the string
    # of desired length
    for _ in range(p):         
        # randint function to generate
        # 0, 1 randomly and converting
        # the result into str
        key1.append(random.randint(0, 1))         
    return key1

def check_error(og_bit, error_bit):
    """ Check the number of places where the two bits differ"""
    return sum ( og_bit[i] != error_bit[i] for i in range(len(og_bit)) )

    

num_errors = 0
num_seven_bits = 200
for _ in range(num_seven_bits):
    og_bit = rand_key(7)
    error_bit = channel(og_bit, finding_bit_prob_error(0.996))
    num_errors += check_error(og_bit, error_bit)
    print("Original bit: ", og_bit, " Error bit: ", error_bit)
print("Number of bits with an error: ", num_errors, "for ", num_seven_bits)




        
        



