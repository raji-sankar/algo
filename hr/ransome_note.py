def ransom_note(magazine, ransom):
    answer = False
    mag = get_word_dict(magazine)
    ran = get_word_dict(ransom)
    y = set(ran.keys())
    x = set(mag.keys())

    if y.issubset(x):
        answer = True
        for key in y:
            if mag[key] < ran[key]:
                return False


    return answer




def get_word_dict(sentence):
    dict_word = {}
    for word in sentence:
        dict_word[word] = dict_word.get(word, 0) + 1
    return dict_word


m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if (answer):
    print "Yes"
else:
    print "No"