import numpy as np


H = np.asarray_chkfinite([
[0,0,0,1,1,1,1],
[0,1,1,0,0,1,1],
[1,0,1,0,1,0,1],
],) 
# dtype=bool)

G = np.asarray_chkfinite([
    [1,1,1,0,0,0,0],
    [1,0,0,1,1,0,0],
    [0,1,0,1,0,1,0],
    [1,1,0,1,0,0,1],
    ], )
    # dtype=bool)

def convert_message_to_codeword(message):
    """
    Convert a 4-bit message into an 8-bit codeword.
    """
    return np.matmul(message, G)

def insert_error_to_codeword(codeword, error_index):
    """
    Insert error into codeword at given index pose.
    """
    error_index -= 1
    codeword[error_index] = (codeword[error_index] + 1) % 2
    return codeword

def calculate_syndrome(codeword):
    """
    Calculate syndrome of given codeword.
    """
    syndrome = np.matmul(codeword,np.transpose(H))
    for i in range(len(syndrome)):
        syndrome[i] = syndrome[i] % 2
    return syndrome

print("G: ", G)
print("H: ", H)
# print(np.matmul(G,np.transpose(H)))

message = np.asarray_chkfinite([0,0,0,1])
print("message: ", message)
codeword = convert_message_to_codeword(message)
print("codeword: ", codeword)
codeword = insert_error_to_codeword(codeword, 4)
print("codeword with error: ", codeword)
syndrome = calculate_syndrome(codeword)
print("syndrome: ", syndrome)
