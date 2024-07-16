print(id('Howdy'))  # -> When Python runs id('Howdy'), it creates the 'Howdy' string in the computer’s memory

# Note: Like all strings, 'Howdy' is immutable and cannot be changed. If you “change” the string in a variable,
# a new string object is being made at a different place in memory, and the variable refers to this new string

bacon = 'Hello'
print(id(bacon))

bacon = bacon + 'World'  # A new string is made from 'Hello' and ' world!'
print(id(bacon))  # bacon now refers to a completely different string.
