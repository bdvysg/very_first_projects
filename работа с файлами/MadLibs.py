with open('sample.txt', 'r') as sampleText:
    initialText = sampleText.read()

while (initialText.find('NOUN') > 0) or (initialText.find('VERB') > 0) or (initialText.find('ADJECTIVE') > 0) or (initialText.find('ADVERB') > 0):
    if initialText.find('NOUN') > 0:
        word = input('Input noun: ')
        initialText = initialText.replace('NOUN', word, 1)

    if initialText.find('VERB') > 0:
        word = input('Input verb: ')
        initialText = initialText.replace('VERB', word, 1)

    if initialText.find('ADJECTIVE') > 0:
        word = input('Input adjective: ')
        initialText = initialText.replace('ADJECTIVE', word, 1)

    if initialText.find('ADVERB') > 0:
        word = input('Input adverb: ')
        initialText = initialText.replace('ADVERB', word, 1)

with open('sample.txt', 'w') as sampleText:
    sampleText.write(initialText)

print(' '*15 + 'Finish text')
print(initialText)





