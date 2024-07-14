import random

# random.choice(list)
pets = ['Dog', 'Cat', 'Moose']
print(random.choice(pets))
# You can consider random.choice(someList) to be a shorter form of -> someList[random.randint(0, len(someList) – 1].


# random.shuffle(list) function will reorder the items in a list
people = ['Alice', 'Bob', 'Carol', 'David']
print(people)
random.shuffle(people)
print(people)