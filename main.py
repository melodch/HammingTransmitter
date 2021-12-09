import numpy as np
import Tx

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

message = np.asarray_chkfinite([0,0,0,1])
print("message: ", message)
codeword = Tx.convert_message_to_codeword(message, G)
print("codeword: ", codeword)
codeword = Tx.insert_error_to_codeword(codeword, 4)
print("codeword with error: ", codeword)
syndrome = Tx.calculate_syndrome(codeword, H)
print("syndrome: ", syndrome)
