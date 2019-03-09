import sys
import os

def test(message):
    print(message)

if __name__=="__main__":
    #message=input("Enter your message to print on screen")
    message=sys.argv[1]
    test(message)
