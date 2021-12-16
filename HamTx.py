# image
import numpy as np
from PIL import Image

def convert_message_to_codeword(message, generator_mat):
    """
    Convert a 4-bit message into an 7-bit codeword.
    """
    codeword = np.matmul(message, generator_mat)
    codeword = codeword % 2
    return codeword

def insert_error_to_codeword(codeword, error_index):
    """
    Insert error into codeword at given index pose.
    """
    error_index -= 1
    codeword[error_index] = (codeword[error_index] + 1) % 2
    return codeword

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
    return list(map(int,list(format(num,'08b'))))
    



