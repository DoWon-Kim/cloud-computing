import boto3
import sys
import pprint

def menu():
    while True:
        print("-------------------------------------------------")
        print("1. list instance           2. available zone")
        print("3. start instance          4. available regions")
        print("5. stop instance           6. create instance")
        print("7. reboot instance         8. list images")
        print("9.                         99. quit")
        print("-------------------------------------------------")

if __name__=='__main__':
    menu()