import numpy as np
import time
import HamTx
import HamRx
import RepTx
import RepRx

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
            [1,0,1,1]]

# HAMMING
decode_time_taken = []
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
    syndrome = HamRx.calculate_syndrome(codeword, H)
    print(syndrome, " "*8, "syndrome")
    codeword = HamRx.fix_error(codeword, syndrome)
    print(codeword, " codeword with fix")
    message = HamRx.convert_codeword_to_message(codeword)
    print(message, " "*6, "message\n")
    decode_time_taken.append(time.time() - initial_t)
print("Average time taken to decode with hamming(7,4): ", sum(decode_time_taken)/len(decode_time_taken), "\n")

# REPETITION
decode_time_taken = []
deg_repetition = 3
for message in messages:
    # Encode
    print(message, " "*24, "message")
    codeword = RepTx.convert_message_to_codeword(message, deg_repetition)
    print(codeword, " codeword")

    # Insert error
    codeword = RepTx.insert_error_to_codeword(codeword, error_pose)
    print(codeword, " codeword with error at position", error_pose)

    # Decode
    initial_t = time.time()
    codeword = RepRx.fix_error(codeword, deg_repetition)
    print(codeword, " codeword with fix")
    message = RepRx.convert_codeword_to_message(codeword, deg_repetition)
    print(message, " message\n")
    decode_time_taken.append(time.time() - initial_t)
print("Average time taken to decode with repition(3): ", sum(decode_time_taken)/len(decode_time_taken))
