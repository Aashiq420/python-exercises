f = open('file.txt', 'r')
max_num = 0
line_counter = 0
max_word = ''
for line in f:
    line_counter+=1
    for word in line.split():
        if len(word)>max_num:
            max_num = len(word)
            max_word = word
print("Longest word:",max_word,"with", max_num,"letters")
print("Number of lines:",line_counter)

f.close()
