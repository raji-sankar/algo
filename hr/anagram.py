'''
Sample Input

cde
abc
Sample Output

4
'''

def number_needed(a, b):
    num = 0
    x = get_string_dict(a)
    y = get_string_dict(b)

    keys_to_delete_a = set(x.keys()) - set(y.keys())
    keys_to_delete_b = set(y.keys()) - set(x.keys())
    for key in keys_to_delete_a:
        num += x.pop(key)
    for key in keys_to_delete_b:
        num += y.pop(key)

    # now dict_a only has the matching keys with b
    for key in x.keys():
        if x[key] != y[key]:
            num += abs(x[key] - y[key])
    return num


def get_string_dict(a):
    dict_a = {}
    for x in a:
        dict_a[x] = dict_a.get(x, 0) + 1
    return dict_a



a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)