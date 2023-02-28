try:
    with open('text.txt', 'r') as reader:
        reader.read()
       #try catch try except
except:
    print("somehow i reached this block")

try:
    with open('text.txt', 'r') as reader:
        reader.read()
except Exception as e:
    print(e)

finally:
    print("cleaning up records")