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


def generate_password(salt, password):
    # 派生方式与bitcoin HD wallt 助记词派生方式一样，同为Sha512，同为2048次
    seed = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt.encode('utf-8'), 2048,dklen=11) # 6 9 12 15 18 , 此处故意不取整，使最终base64编码后含=
                                                                                                        # 密码熵值：2^88
    result = base64.b64encode(bytes.fromhex(seed.hex())).decode()
    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate password with special data.")
    parser.add_argument("--salt", help="Input the salt.")
    parser.add_argument("--password", help="Input the password in plain.")
    args = parser.parse_args()

    if args.salt :
        if args.password :
            password1 = args.password
        else :
            password1 = getpass.getpass("Input secret password please : ")
            password2 = getpass.getpass("Input secret password again  : ")
            if password1 != password2 :
                print("Secret password is NOT matched !")
                exit()
        
        password = generate_password(args.salt,password1)
        print("Password: %s" %password)

    else :
        print("Usage: ")
        print("    ./strongpwd --salt test@example.com                     # Generate a strong password.")
        print("    ./strongpwd --salt test@example.com --password abc123   # For the f**k shell.")
