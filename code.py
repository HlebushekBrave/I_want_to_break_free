#Case-study 7
#Adristi Fauzi (60%)
#Raspopova Alexandra (40%)
#Belozertseva Maria (30%)
file_in = open ("input.txt", 'r')
file_out = open ("output.txt", 'w')
text = file_in.readlines()
textarray = []
wordsarray = []
punct = '''()[]{}'@#$%:"\/^;*_'''
punct_ok = ['.',',','!','?']
new_text = ''
for s in text: #every one line
    s = s.replace('\n', ' ')
    for i in s: #every char
        if i in punct:
            s = s.replace(i, "")
    new_text = new_text+s
new_text = list(new_text)
for x in range (len(new_text)):
    if new_text[x] in punct_ok:
        if new_text[x-1] == ' ':
            new_text[x-1] = ''
all_text = ''
for m in new_text:
    all_text = all_text+m
wordsarray = all_text.split(' ')
uniq_words = []
for y in wordsarray:
    if y in uniq_words:
        y = y
    else:
        uniq_words.append(y)
for y in uniq_words:
    array1 = []
    for u in range(len(wordsarray)):
        if wordsarray[u] != wordsarray[-1]:
            if wordsarray[u] == y:
                array1.append(wordsarray[u + 1])
        else:
            wordsarray[u] = wordsarray[u]
    if len(array1) > 0:
        print(y, end=' ', file = file_out)
        print(array1, file = file_out)
for i in wordsarray:
    if i.istitle() == True:
        start_list.append(i)
number_sentences=int(input())
for i in range(0, number_sentences):
    o = random.randint(0, len(start_list)-1)
    sentence = start_list[o]
    print(sentence)
file_in.close()
file_out.close()