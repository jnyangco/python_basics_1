# ======================================
# Long form
foo = ['dog', 'cat', 'bird']
bar = []
for pet in foo:
    bar.append(pet)
print(bar)

# Short form
foo = ['dog', 'cat', 'bird']
bar = [pets for pets in foo]
print(bar)

# ======================================
# with text.strip()
# Long form
hello = ['one  ', 'two  ', '  three']
world = []
for word in hello:
    world.append(word.strip())
print(world)

# Short form
hello = ['one  ', 'two  ', '  three']
world = [word.strip() for word in hello]
print(world)