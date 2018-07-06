"""
Project Euler Problem 22
========================

Using names.txt, a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the
alphabetical value for each name, multiply this value by its alphabetical
position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which
is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So,
COLIN would obtain a score of 938 * 53 = 49714.

What is the total of all the name scores in the file?
"""


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

# Checking "022.py" against solution: 871198282
# Time elapsed: user: 61.3 ms, sys: 11.8 ms, total: 73.1 ms
