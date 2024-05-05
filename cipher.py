print("1.To Encrypt\n2.To Decrypt")
op = int(input("Enter Option: "))

if op == 1:
    key = input("Enter Text: ")
    result = ""
    s = int(input("Enter number of Shifts: "))
    for char in key:
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + s - 97) % 26 + 97)
        else:
            result += char
    print("Encrypted Text: " + result)
    
elif op == 2:
    ciphertext = input("Enter encrypted Text: ")
    decrypted_text = ""
    s = int(input("Enter number of Shifts: "))
    for char in ciphertext:
        if char.isupper():
            shifted_char = chr(((ord(char) - s - 65) % 26) + 65)
        elif char.islower():
            shifted_char = chr(((ord(char) - s - 97) % 26) + 97)
        else:
            shifted_char = char
        decrypted_text += shifted_char
    print("Decrypted Text: " + decrypted_text)
    
else:
    print("Wrong option entered! Please try again.")
