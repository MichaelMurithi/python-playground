# strings and bytes are not directly interchangeable
# strings contain unicode, bytes are raw 8-bit values

def main():
    # define some starting values
    byte = bytes([0x41, 0x42, 0x43, 0x44])
    # print(byte)
    
    string = "This is a string"
    # print(string)
    
    #  Trying combining them raises an error. 
    # print(string+byte)
    # Bytes and strings need to be properly encoded and decoded
    decoded_byte = byte.decode('utf-8') 
    # a string and en encoded byte can be concatenated.
    encoded_string = string.encode('utf-16')
    print(encoded_string + byte)
    print(string + decoded_byte)
    # TODO: encode the string as UTF-32
    
if __name__ == "__main__":
    main()
