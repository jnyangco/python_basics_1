def eggs(some_parameter):
    some_parameter.append('Hello')  # modifies the list directly


spam = [1, 2, 3]
eggs(spam)
print(spam)