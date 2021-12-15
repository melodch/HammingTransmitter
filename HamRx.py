import numpy as np


def calculate_syndrome(codeword, parity_check_mat):
    """
    Calculate syndrome of given codeword.
    """
    syndrome = np.matmul(codeword,np.transpose(parity_check_mat))
    for i in range(len(syndrome)):
        syndrome[i] = syndrome[i] % 2
    return syndrome

def fix_error(codeword, syndrome):
    """
    Fix a single error in the codeword given the syndrome.
    """
    syndrome_len = len(syndrome)
    # Convert error position from binary to decimal
    error_pos = 0
    for i in range(syndrome_len):
        error_pos += (2**i)*syndrome[syndrome_len-i-1]
    # Correct the bit in codeword at error position
    codeword[error_pos-1] = (codeword[error_pos-1] + 1) % 2
    return codeword

def convert_codeword_to_message(codeword):
    """
    Convert codeword to message by removing redundant bits.
    """
    message = np.delete(codeword, [0, 1, 3])
    return message
