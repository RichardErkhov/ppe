import argparse
from time import sleep
def run():
    args = argparse.ArgumentParser()
    args.add_argument('--file', default='main.py', help='File to read')
    filename = args.parse_args().file
    with open(filename, mode='r') as f:
        exec(f.read())
    print("Portable executor: program finished")
    while True:
        sleep(1)
if __name__ == '__main__':
    run()