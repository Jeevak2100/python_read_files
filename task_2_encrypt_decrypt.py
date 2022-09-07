import logging


"""""
Encription and Decryption Functions
"""""


def encrypt(str,num):
    print('encrypt')
    logging.warning('Watch out!')  # will print a message to the console
    logging.info('I told you so')  # will not print anything


    str

def decrypt(str,num):
    print('decrypt')
    logging.warning('Watch out!')  # will print a message to the console
    logging.info('I told you so')  # will not print anything

    str


def print_hi(name):
    print(f'Hi, {name}')
    # 1. Send string to encrypt and an integer to encrypt
    # 2. Send string to decrypt and an integer to decrypt
    str="My Name is Jk"
    num=5

    encrypted_str=encrypt(str,num)
    print(encrypted_str)

    decrypted_str=decrypt(encrypted_str,num)
    print(decrypted_str)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Factory-Pattern')

