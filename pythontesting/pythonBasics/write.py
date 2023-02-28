with open('text.txt', 'r') as reader: # no need to write file.close()
    content = reader.readlines()
    reversed(content)
    print(content)
    with open('text.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)
