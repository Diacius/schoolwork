
from time import sleep

print("""
Welcome To:
Proteus Connect
THIS SOFTWARE IS PROTECTED BY PROTEUS SECURITY
UNAUTHORISED USE WILL RESULT IN IMMEDIATE TERMINATION via term4.5a
""")
input("Press enter to ACCEPT")

import sys
for i in range(2):
    sys.stdout.write("\r" + "Loading..." + "/")
    sleep(1)
    sys.stdout.write("\r" + "Loading..." + "—")
    sleep(1)
    sys.stdout.write("\r" + "Loading..." + "\\")
    sleep(1)
    sys.stdout.write("\r" + "Loading..." +
                     "|")
    sleep(1)
