import numpy as np

def fix_error(codeword, parity_check_mat):
    """
    Find syndrome and fix single error in the codeword.
    """
    # Find syndrome
    syndrome = np.matmul(codeword,np.transpose(parity_check_mat))
    # Convert error position from binary to decimal
    error_pos = sum((val%2)*(2**idx) for idx, val in enumerate(reversed(syndrome)))
    if error_pos == 0: return codeword
    else:
        # Flip bit in codeword at error position
        codeword[error_pos-1] = (codeword[error_pos-1] + 1) % 2
        return codeword

def convert_codeword_to_message(codeword):
    """
    Convert codeword to message by removing redundant bits.
    """
    message = np.delete(codeword, [0, 1, 3])
    return message
