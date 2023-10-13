#!/usr/bin/env python3

import argparse
import os
import hmac
import hashlib
import getpass
import base64

#  Input:
#    P = "password" (8 octets)
#    S = "salt" (4 octets)
#    c = 1
#    dkLen = 20

#  Output:
#    PBKDF2-HMAC-SHA256 = 120fb6cffcf8b32c43e7225256c4f837a86548c9 (20 octets)


def generate_password(salt, data):
    seed = hashlib.pbkdf2_hmac('sha256', data.encode('utf-8'), salt.encode('utf-8'), 2048,dklen=12) # 6 9 12 15 18
    result = base64.b64encode(bytes.fromhex(seed.hex())).decode()

    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate password with special data.")
    parser.add_argument("--data", help="Input the data.")
    args = parser.parse_args()

    if args.data :
        data = args.data
        salt1 = getpass.getpass("Input secret salt please : ")
        salt2 = getpass.getpass("Input secret salt again  : ")
        if salt1 != salt2 :
            print("Secret salt is NOT matched !")
        else:
            password = generate_password(salt1,data)
            print("Password: %s" %password)

        
    else :
        print("Usage: ")
        print("    ./strongpassword --data test@example.com   # Generate a strong password.")
