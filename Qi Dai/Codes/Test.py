from playsound import playsound
import timeit
from gtts import gTTS

count = 12
with open("Word.txt") as file_in:
    lines = []
    for line in file_in:
        if count < 15:
            for word in line.split():
                start = timeit.default_timer()
                print(word)
                stop = timeit.default_timer()
                print('\nTime for each word: ', stop - start)
                start = timeit.default_timer()
                playsound('%s.wav' % count)
                stop = timeit.default_timer()
                print('\nTime for each audio: ', stop - start)
                count=count+1
        else:
            break

