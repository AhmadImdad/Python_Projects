import random

def encode(input_string):
    encode_string=""
    key=list()
    for i in range(len(input_string)):
        temp=random.randint(0,9)
        encode_string+=chr(ord(input_string[i])+temp)
        key.append(temp)
    print(f"\n---------'{"".join(encode_string)}'-----------\n")
    key_string=list()
    for i in range(len(key)):
        key_string.append(str(key[i]))
    print(f"This is the Key to decode '{"".join(key_string)}'.")
    

def decode(decode_string,key_String):
    if len(key_string)!=len(decode_string):
            print("Key length must match the decode string length!!!!!")
    else:
        result=""
        for i in range(len(decode_string)):
            temp=int(key_string[i])
            result+=chr(ord(decode_string[i])-temp)
        print(f"\n-----------{result}-----------")
        

while True:
    choice=int(input("""\nDo you want to encode,Press 1:
                     \nDo you want to decode,Press 2:"""))
    if choice==1:
        input_string=input("\nEnter what you want to encode:")
        encode(input_string)
    else:
        decode_string=input("\nEnter the Text now = ")
        key_string=input("Enter the Key first = ")
        decode(decode_string,key_string)
        