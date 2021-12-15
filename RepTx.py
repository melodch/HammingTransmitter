import numpy as np

def convert_message_to_codeword(message, deg_repetition):
    codeword = []
    for digit in message:
        for _ in range(deg_repetition):
            codeword.append(digit)
    return np.asarray_chkfinite(codeword)

def insert_error_to_codeword(codeword, error_index):
    """
    Insert error into codeword at given index pose.
    """
    error_index -= 1
    codeword[error_index] = (codeword[error_index] + 1) % 2
    return codeword
