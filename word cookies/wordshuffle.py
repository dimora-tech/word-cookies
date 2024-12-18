import math
import random
from mine import numbers

random.seed(6)
with open('words_alpha.txt') as file:
    words_list = file.read()

def permt(string, n):
    fact = 1
    count_ = {i:string.count(i) for i in string}
    for num in count_.values(): fact *= math.factorial(num)
    result = math.perm(len(string), n)/fact
    return result

while True:
    word = input('Enter word: ')
    if word == '': break
    while True:
        count = int(input('How many letters: '))
        
        temp = []
        three_letter_words = []
        four_letter_words = []
        five_letter_words = []
        six_letter_words = []
        seven_letter_words = []
        eight_letter_words = []
        letters = list(word)
        letters.sort()
        size = len(word)

        while True:
            random.shuffle(letters)
            string = ''
            for l in letters: string += l
            if string[:count] in temp: continue
            temp.append(string[:count])
            if f'\n{string[:count]}\n' in words_list: locals()[f'{numbers[count]}_letter_words'].append(string[:count])
            
            if len(temp) >= permt(word, count):
                locals()[f'{numbers[count]}_letter_words'].sort()
                #print(temp)
                print(f'{numbers[count]}_letter_words:\n',locals()[f'{numbers[count]}_letter_words'])
                break
        answer = input('Same word? ')
        if answer in ('y','yes','Yes','YES'): continue
        else: break
