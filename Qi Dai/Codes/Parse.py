import re
from gtts import gTTS
filename = 'Sample.txt'
file = open(filename, 'r')
text = file.read()
file.close()
lst = re.split(',|\*',text)
i = 1
with open("Sorted.txt",'w') as file:
    for st in lst:
        file.write(st+'\n')
        mytext = st
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save('%s.wav' % i)
        print('File save!')
        i+=1
file.close()








