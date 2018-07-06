myfile = open("one-hundred-50-digit-numbers")
contents = myfile.read();
split = contents.split("\n")
s = 0
for i in range(100):
    s = s + int(split[i])
    print(split[i])
print("The sum of the above numbers is:")
print(s)
s = str(s)
for i in range(10):
    print(s[i])
