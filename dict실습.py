# 단어의 빈도수 구하기
word_vec = ['love', 'word', 'love', 'cat', 'word']

# case 01
wc = {}
for word in word_vec:
    wc[word] = wc.get(word, 0) + 1
print('case 01 wc - ', wc)

# case 02
wc = {}
for word in word_vec:
    wc[word] = word_vec.count(word)
print('case 02 wc - ', wc)

# case 03
wc = {}
for word in word_vec:
    if word in wc:
        wc[word] += 1
    else:
        wc[word] = 1
print('case 03 wc - ', wc)

# case 04
print('set - ', set(word_vec))
print('comp - ', [word_vec.count(i) for i in set(word_vec)])
zipDict = dict(zip(set(word_vec), [word_vec.count(i) for i in set(word_vec)]))
print(zipDict)