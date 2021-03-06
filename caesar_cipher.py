# https://inventwithpython.com/invent4thed/chapter14.html

##############################################################################
# A Caesar Cipher is a type of substitution cipher in which each letter in the
# plaintext is 'shifted' a certain number of places down the alphabet.
# For example, with a shift of 1, A would be replaced by B, B would become C,
# and so on.
##############################################################################

# Global variables
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
MAX_KEY_SIZE = len(SYMBOLS)

def getMode():
    while True:
        print("Are you (e)ncrypting or (d)ecrypting a message?")
        mode = input().lower()
        if mode in ['e', 'd']:
            return mode
        else:
            print("Please enter 'e' or 'd'.")

def getMessage():
    print('Please enter your message:')
    return input()

def getKey():
    key = 0
    while True:
        print('Enter the key number: 1-%s' % (MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key

def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''
    # If a symbol isn't found, just enter the character as it is.
    for symbol in message:
        symbolIndex = SYMBOLS.find(symbol)
        if symbolIndex == -1:
            translated += symbol
        else:
            symbolIndex += key
            # Encrypt or decrypt
            if symbolIndex >= len(SYMBOLS):
                symbolIndex -= len(SYMBOLS)
            elif symbolIndex < 0:
                symbolIndex += len(SYMBOLS)
            translated += SYMBOLS[symbolIndex]
    return translated

mode = getMode()
message = getMessage()
key = getKey()
print('Your translated text is: ')
print(getTranslatedMessage(mode, message, key))
