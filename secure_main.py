#security update for the main program
import argparse
from time import sleep
import pyAesCrypt
import io
def create(filename, password='password'):
    bufferSize = 64 * 1024
    #put the code into pyaescrypt archive
    pyAesCrypt.encryptFile(filename, filename+'.aes', password, bufferSize)

def execute(filename, password='password'):
    if not filename.endswith(".aes"):
        filename += ".aes"
    bufferSize = 64 * 1024
    #decrypt the code from pyaescrypt archive
    filek = io.BytesIO()
    with open(filename, mode='rb') as f:
        length = len(f.read())
        f.seek(0)
        #decrypt f to bytes
        pyAesCrypt.decryptStream(f, filek, password, bufferSize, length)
    filek.seek(0)
    exec(filek.read())

def decode(filename, password='password'):
    if not filename.endswith(".aes"):
        filename += ".aes"
    bufferSize = 64 * 1024
    #decrypt the code from pyaescrypt archive
    filek = io.BytesIO()
    with open(filename, mode='rb') as f:
        length = len(f.read())
        f.seek(0)
        #decrypt f to bytes
        pyAesCrypt.decryptStream(f, filek, password, bufferSize, length)
    filek.seek(0)
    return filek.read()

def user():
    args = argparse.ArgumentParser()
    args.add_argument('--file', default='main.py', help='File to read')
    args.add_argument('--action', default='create', help='Action to perform [create, execute, decode]')
    args.add_argument('--password', default='password', help='Password to use')
    filename = args.parse_args().file
    action = args.parse_args().action
    password = args.parse_args().password

    if action == 'create':
        create(filename, password)
    elif action == 'execute':
        execute(filename, password)
    elif action == 'decode':
        with open(filename, mode='w') as f:
            f.write(decode(f"decoded+{filename}.py", password))




if __name__ == "__main__":
    #user()
    create("test.py")
    execute("test.py")