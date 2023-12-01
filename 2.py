def ethereum_address(address): #Function to check for validity of address
    valid_char = set("0123456789abcdefABCDEF")#Ethereum address will have only these characters

    if len(address)!=42: #Ethereum address should have a length of 42
        return False

    if not address.startswith("0x"): #All ethereum addresses start with 0x
        return False


    for char in address[2:]:#First two characters will be 0x so checking only for characters after
        if char not in valid_char:
            return False

    return True#Returns True only after checking the three conditions for it to be etherum address



address=input("Enter ethereum address: ")#Just inputting an address

print(ethereum_address(address))#Checking for validity using the above defined function.
