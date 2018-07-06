import string
myfile = open('names.txt', 'r')
contents = myfile.read()
#print(contents)
split = contents.split("\",\"")
split[0] = split[0].split("\"")[1]
for i in range(len(split)):
    split[i] = split[i].replace('"', '')
#sort
split.sort()
score = 0
for a in range(len(split)):
    thisScore = 0
    for i in split[a]:
        thisScore = thisScore + string.ascii_uppercase.index(i) + 1
    thisScore = thisScore * (a+1)
    score = score + thisScore
print(score)
