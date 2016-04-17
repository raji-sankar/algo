import sys


def read_file(filename):
    with open(filename, 'rt') as f:
        data = []
        for line in f:
            data.append(line)
        n = data[0]
        print n
        things, chunk = data[1:], 3
        cases = zip(*[iter(things)]*chunk)
        for case in cases:
            c = case[0]
            i = case[1]
            items = map(int, case[2].strip().split(' '))
            print c
            print i
            print items

def main():
    read_file('C:\\Users\\Raji\\Downloads\\A-small-practice.in')