# image
import numpy as np
from PIL import Image

def convert_message_to_codeword(message, generator_mat):
    """
    Convert a 4-bit message into an 8-bit codeword.
    """
    return np.matmul(message, generator_mat)

def insert_error_to_codeword(codeword, error_index):
    """
    Insert error into codeword at given index pose.
    """
    error_index -= 1
    codeword[error_index] = (codeword[error_index] + 1) % 2
    return codeword

def calculate_syndrome(codeword, parity_check_mat):
    """
    Calculate syndrome of given codeword.
    """
    syndrome = np.matmul(codeword,np.transpose(parity_check_mat))
    for i in range(len(syndrome)):
        syndrome[i] = syndrome[i] % 2
    return syndrome

im = Image.open('tcp.png')
img = im.load()

print('before')
print(img[500,600])
img[500,600] = (0,0,0)
print('after')
print(img[500,600])
# does this update? 
im.save('tcp_updated.png')  # Save the modified pixels as .png
