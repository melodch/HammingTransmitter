import numpy as np

def fix_error(codeword, deg_repetition):
    """
    Fix error by iterating through codeword and flipping minority bit.
    """
    fixed_codeword = []
    for group in range(deg_repetition+1):
        zero_count = 0
        one_count = 0
        for bit in range(group*deg_repetition, (group+1)*deg_repetition):
            if codeword[bit] == 0: zero_count+=1
            else: one_count+=1
        if zero_count > one_count:
            fixed_codeword += [0]*deg_repetition
        else:
            fixed_codeword += [1]*deg_repetition
    return np.asarray_chkfinite(fixed_codeword)

def convert_codeword_to_message(codeword, deg_repetition):
    message = []
    groups = int(len(codeword)/deg_repetition)
    for i in range(groups):
        message.append(codeword[i*deg_repetition])
    return np.asarray_chkfinite(message)
