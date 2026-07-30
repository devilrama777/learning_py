"""
THIS IS THE PROGRAMME USED TO ENCRYPT OR DECRYPT THE STRING OR PASSWORD AS YOU WANTED
BUT HAS LIMITATION TO 0 TO 25 IT MEANS ONE TYPE OF WORD OR CHARACTER CAN BE ENCRYPTED 25 TIMES ONLY
"""
def input_user2():
    # from pydoc import text
    print("Here is the function of encryption and decryption!!")
    text = input("Enter a string: ")
    shift = int(input("Enter a number between 1 and 25: "))

    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    elif shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    def caesar(text, shift, encrypt=True):

        alphabet = 'abcdefghijklmnopqrstuvwxyz'

        if not encrypt:
            shift = -shift

        shifted_alphabet = alphabet[shift:] + alphabet[:shift]
        translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
        encrypted_text = text.translate(translation_table)
        return encrypted_text


    def encrypt(text, shift):
        return caesar(text, shift)


    def decrypt(text, shift):
        return caesar(text, shift, encrypt=False)


    num1 = input("What do you want to encrypt/decrypt? press(E/D) \n")

    if num1 == 'e' or num1 == 'E':
        print(encrypt(text, shift))
    elif num1 == 'd' or num1 == 'D':
        print(decrypt(text, shift))
    else:
        print('Please enter a valid input')

input_user2()