#Cryptographically secure random ascii string using system CSPRNG
#rather than random's, which is not cryptographically secure and
#was not intended for this purpose. SystemRandom() calls
#CryptGenRandom() on Windows and /dev/urandom on *nix.
# 
# TODO: Incorporate secrets module
# TODO: Make this a proper command-line application
# without require user editing for string length. 
#
# (c) 2018 Christian Giliberto. MIT License.

import random
import string
#import secrets TODO

#Set n to desired string length
print(''.join(random.SystemRandom().choice(
    string.ascii_uppercase + string.digits + string.ascii_lowercase + string.punctuation) 
    for _ in range(n)))