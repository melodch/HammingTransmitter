# image
import numpy as np
from PIL import Image

def convert_message_to_codeword(message, generator_mat):
    """
    Convert a 4-bit message into an 7-bit codeword.
    """
    codeword = np.matmul(message, generator_mat)
    for i in range(len(codeword)):
        codeword[i] = codeword[i] % 2
    return codeword

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

def image_to_pixels(imgname):
    im = Image.open(imgname)
    img = im.load()
    width, height = im.size
    output_matrix = [[0 for j in range(width)] for i in range(height)]
    for i in range(height):
        for j in range(width):
            current = img[j,i]
            red = int_to_list(current[0])
            green = int_to_list(current[1])
            blue = int_to_list(current[2])
            output_matrix[i][j] = [red[:4], red[4:], green[:4], green[4:], blue[:4], blue[4:]]
    
    return output_matrix

def int_to_list(num):
    return list(format(num,'08b'))
    

out = image_to_pixels('icon.jpg')

