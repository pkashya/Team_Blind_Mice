from playsound import playsound

count = 1

with open("Sorted.txt") as file_in:
    lines = []
    for line in file_in:
        if count < 4:
            for word in line.split():
                print(word)
            playsound('%s.wav' % count)
            count = count + 1
        else:
            break