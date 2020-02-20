from gtts import gTTS
# save text file to memory
filename = 'engineering.txt'
file = open(filename, 'r')
text = file.read()
file.close()
# convert text file to audio file and save it to mp3 format
mytext = text
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save('engineering.mp3')
print('File save!')







