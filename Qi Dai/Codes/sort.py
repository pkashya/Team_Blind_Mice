import re
from gtts import gTTS
filename = 'engineering.txt'
file = open(filename, 'r')
text = file.read()
file.close()
lst = re.split(',|\*|\n',text)
with open("sorted.txt",'w') as file:
    for st in lst:
        file.write(st+'\n\n')
file.close()








