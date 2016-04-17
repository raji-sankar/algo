import sys

def main():
    time = raw_input().strip()
    h = time[:2]
    ampm = time[-2]
    if ampm == 'P':
        if int(h) < 12:
            h = int(h) + 12
            h = '{0:0{1}d}'.format(h,2)
    elif ampm == 'A' and h == '12':
        h = '00'
    print h + time[2:-2]

