import numpy as np
import time
import Tx
import Rx
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

# HAMMING
decode_time_taken = []
for i in range(7):
    # Encode
    message = np.asarray_chkfinite([0,0,0,1])
    print(message, " "*6, "message")
    codeword = Tx.convert_message_to_codeword(message, G)
    print(codeword, " codeword")

    # Insert error
    error_pose = i+1
    codeword = Tx.insert_error_to_codeword(codeword, error_pose)
    print(codeword, " codeword with error at position", error_pose)

    # Decode
    initial_t = time.time()
    syndrome = Rx.calculate_syndrome(codeword, H)
    print(syndrome, " "*8, "syndrome")
    codeword = Rx.fix_error(codeword, syndrome)
    print(codeword, " codeword with fix\n")
    # message = Rx.convert_codeword_to_message(codeword, G)
    # print(message, " message\n")
    decode_time_taken.append(time.time() - initial_t)
print("Average time taken to decode with hamming(7,4): ", sum(decode_time_taken)/len(decode_time_taken))

# REPETITION
# decode_time_taken = []
# deg_repetition = 3
# for i in range(7):
#     # Encode
#     message = np.asarray_chkfinite([0,0,0,1])
#     print(message, " "*27, "message")
#     codeword = RepTx.convert_message_to_codeword(message, deg_repetition)
#     print(codeword, " codeword")

#     # Insert error
#     error_pose = i+1
#     codeword = RepTx.insert_error_to_codeword(codeword, error_pose)
#     print(codeword, " codeword with error at position", error_pose)
    # Decode
    # initial_t = time.time()
    # syndrome = RepRx.calculate_syndrome(codeword, H)
    # print(syndrome, " "*8, "syndrome")
    # codeword = RepRx.fix_error(codeword, syndrome)
    # print(codeword, " codeword with fix\n")
    # decode_time_taken.append(time.time() - initial_t)
# print("Average time taken to decode with repition(3): ", sum(decode_time_taken)/len(decode_time_taken))
