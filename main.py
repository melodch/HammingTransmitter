import numpy as np
import time
import HamTx
import HamRx
import RepTx
import RepRx
import Ch
from PIL import Image


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

print("G: ", G)
print("H: ", H)
# print(np.matmul(G,np.transpose(H)))

messages = [[0,0,0,1],
            [0,1,0,1],
            [1,0,0,1],
            [1,1,0,1],
            [1,0,0,0],
            [1,0,1,1]]

def check_hamming_timing():
    ham_decode_time_taken = []
    for message in messages:
        # Encode
        message = np.asarray_chkfinite(message)
        print(message, " "*6, "message")
        codeword = HamTx.convert_message_to_codeword(message, G)
        print(codeword, " codeword")

        # Insert error
        error_pose = 2
        codeword = HamTx.insert_error_to_codeword(codeword, error_pose)
        print(codeword, " codeword with error at position", error_pose)

        # Decode
        initial_t = time.time()
        codeword = HamRx.fix_error(codeword, H)
        print(codeword, " codeword with fix")
        message = HamRx.convert_codeword_to_message(codeword)
        print(message, " "*6, "message\n")
        ham_decode_time_taken.append(time.time() - initial_t)
    ham_average_time_taken = sum(ham_decode_time_taken)/len(ham_decode_time_taken)
    print("Average time taken to decode with hamming(7,4): ", ham_average_time_taken, "\n")

def transfer_image_with_hamming(prop,image_name):
    """ 
    Transfer image through noise channel but with hamming code.
    Final image is saved with .png format

    """ 
    # convert image to pixel data with RGB info
    image_matrix = HamTx.image_to_pixels(image_name)
    for i in range(len(image_matrix)):
        for j in range(len(image_matrix[0])):
            for k in range(6):
                #convert message to hamming codeword with generator matrix
                image_matrix[i][j][k] = HamTx.convert_message_to_codeword(image_matrix[i][j][k],G)
                #go through noise channel and cause error
                image_matrix[i][j][k] = Ch.channel(image_matrix[i][j][k], prop)
                #fix error with parity check matrix
                image_matrix[i][j][k] = HamRx.fix_error(image_matrix[i][j][k],H)
                #convert hamming codeword back to message
                image_matrix[i][j][k] = HamRx.convert_codeword_to_message(image_matrix[i][j][k])

    # convert message back to RGB data
    for i in range(len(image_matrix)):
        for j in range(len(image_matrix[0])):
            redlist = list(image_matrix[i][j][0]) + list(image_matrix[i][j][1])
            redstr = "".join([str(elem) for elem in redlist])
            red = int(redstr,2)

            greenlist = list(image_matrix[i][j][2]) + list(image_matrix[i][j][3])
            greenstr = "".join([str(elem) for elem in greenlist])
            green = int(greenstr,2)

            bluelist = list(image_matrix[i][j][4]) + list(image_matrix[i][j][5])
            bluestr = "".join([str(elem) for elem in bluelist])
            blue = int(bluestr,2)

            image_matrix[i][j] = (red,green,blue)

    # create new image
    img = Image.new('RGB', (len(image_matrix[0]), len(image_matrix)), color = 'red')

    # update each pixel for the new image
    for i in range(len(image_matrix)):
        for j in range(len(image_matrix[0])):
            img.putpixel((j,i),image_matrix[i][j])

    # save new image
    new_name = image_name + "_hamming" + "_prop_" + str(prop)[:5] + '.png'
    img.save(new_name)

def transfer_image_without_hamming(prop, image_name):
    """ 
    Transfer image through noise channel without hamming code.
    Final image is saved with .png format

    """ 
    # convert image to pixel data with RGB info
    image_matrix = HamTx.image_to_pixels(image_name)
    for i in range(len(image_matrix)):
        for j in range(len(image_matrix[0])):
            for k in range(6):
                #go through noise channel and cause error
                image_matrix[i][j][k] = Ch.channel(image_matrix[i][j][k], prop)

    # convert message back to RGB data
    for i in range(len(image_matrix)):
        for j in range(len(image_matrix[0])):
            redlist = list(image_matrix[i][j][0]) + list(image_matrix[i][j][1])
            redstr = "".join([str(elem) for elem in redlist])
            red = int(redstr,2)

            greenlist = list(image_matrix[i][j][2]) + list(image_matrix[i][j][3])
            greenstr = "".join([str(elem) for elem in greenlist])
            green = int(greenstr,2)

            bluelist = list(image_matrix[i][j][4]) + list(image_matrix[i][j][5])
            bluestr = "".join([str(elem) for elem in bluelist])
            blue = int(bluestr,2)

            image_matrix[i][j] = (red,green,blue)

    # create new image
    img = Image.new('RGB', (len(image_matrix[0]), len(image_matrix)), color = 'red')
    
    # update each pixel for the new image
    for i in range(len(image_matrix)):
        for j in range(len(image_matrix[0])):
            img.putpixel((j,i),image_matrix[i][j])

    # save new image
    new_name = image_name + "_no_hamming" + "_prop_" + str(prop)[:5] + '.png'
    img.save(new_name)


prop = 1 - 0.97854
image_name = 'octo.jpg'

transfer_image_with_hamming(prop,image_name)
transfer_image_without_hamming(prop,image_name)