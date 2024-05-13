sentence = "the kenyan gorverment is not really poor but it's bad in it's leardership"

if 'not' in sentence and 'poor' in sentence:
    not_word = sentence. find ('not')
    poor_word =sentence. find ('poor')
if not_word  != -1 and poor_word != -1 and not_word < poor_word:
    sentence1 = sentence[:not_word] + 'good' + sentence[poor_word+4:]

print(sentence)