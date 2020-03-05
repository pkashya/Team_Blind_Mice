from playsound import playsound

count = 1
i = 0
with open("Chapters.txt") as file_in:
    lines = []
    for line in file_in:
        lines.append(line)
    while count < 13:
         print(lines[i])
         playsound('%s.mp3' % count)
         i +=2
         count+=1

