import numpy as np
import random
def finding_bit_prob_error(total_p):
    """Finding bit probability error given we want 1 error in 4 bits"""
    p = 1 - ((total_p/4) ** (1. / 3))
    print(p)
    return p
finding_bit_prob_error(.996)

def channel(half_byte):
    """ Use probability to indroduce one error
    
        Args: half_byte: 4 bit number 
        Returns : 4 bit number with one error introduced
    """
    bit_prop_error = finding_bit_prob_error(0.996)
    lst_byte = list(half_byte)
    for i in range(len(half_byte)):
        if random.random() <= bit_prop_error:
            half_byte[i]

        
        



