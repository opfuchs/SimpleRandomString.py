#Cryptographically secure random ascii string using system CSPRNG
#rather than random's, which is not cryptographically secure and
#was not intended for this purpose. SystemRandom() calls
#CryptGenRandom() on Windows and /dev/urandom on *nix.
# 
# TODO: Update for python 3.6 using secrets module.
# TODO: Make this a proper command-line application
# without require user editing for string length. 

import random
import string
#import secrets TODO

#Set N to desired string length
print(''.join(random.SystemRandom().choice(
    string.ascii_uppercase + string.digits + string.ascii_lowercase + string.punctuation) 
    for _ in range(36)))