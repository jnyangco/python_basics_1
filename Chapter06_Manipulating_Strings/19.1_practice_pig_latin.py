print('Enter the English message to translate into Pig Latin: ')

message = 'My name is AL SWEIGART and I am 4,000 years old.'
vowels = ('a', 'e', 'i', 'o', 'u')
pig_latin = []

for word in message.split():
    # print(word)

    prefix_non_letters = ''

    while len(word) > 0 and not word[0].isalpha():
        prefix_non_letters += word[0]
        word = word[1:]

    if len(word) == 0:
        pig_latin.append(prefix_non_letters)
        continue

    suffix_non_letters = ''
    while not word[-1].isalpha():
        suffix_non_letters = word[-1] + suffix_non_letters
        word = word[:-1]

    was_upper = word.isupper()
    was_title = word.istitle()

    word = word.lower()

    # Separate the consonants at the start of this word:
    prefix_consonants = ''
    while len(word) > 0 and not word[0] in vowels:
        prefix_consonants += word[0]
        word = word[1:]

    if prefix_consonants != '':
        word += prefix_consonants + 'ey'
    else:
        word += 'yay'

        # Set the word back to uppercase or title case:
    if was_upper:
        word = word.upper()

    if was_title:
        word = word.title()

    pig_latin.append(prefix_non_letters + word)

print(pig_latin)
