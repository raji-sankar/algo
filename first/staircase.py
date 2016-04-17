import sys

def main():
    n = int(raw_input().strip())
    for i in range(n):
        print '{:>{n}}'.format('#'*(i+1), n=n)