#If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
def convert(number):
    total = ""
    # print(len(number))
    if len(number) == 1:
        if number == "1":
            total = total + "one"
        if number == "2":
            total = total + "two"
        if number == "3":
            total = total + "three"
        if number == "4":
            total = total + "four"
        if number == "5":
            total = total + "five"
        if number == "6":
            total = total + "six"
        if number == "7":
            total = total + "seven"
        if number == "8":
            total = total + "eight"
        if number == "9":
            total = total + "nine"
    if len(number) == 2:
        if number == "10":
            total = total + "ten"
        if number == "11":
            total = total + "eleven"
        if number == "12":
            total = total + "twelve"
        if number == "13":
            total = total + "thirteen"
        if number == "14":
            total = total + "fourteen"
        if number == "15":
            total = total + "fifteen"
        if number == "16":
            total = total + "sixteen"
        if number == "17":
            total = total + "seventeen"
        if number == "18":
            total = total + "eighteen"
        if number == "19":
            total = total + "nineteen"
        #consider the second digit    
        if number[0] == "0":
            total = total + convert(number[1])
        if number[0] == "2":
            total = total + "twenty" + convert(number[1])
        if number[0] == "3":
            total = total + "thirty" + convert(number[1])
        if number[0] == "4":
            total = total + "forty" + convert(number[1])
        if number[0] == "5":
            total = total + "fifty" + convert(number[1])
        if number[0] == "6":
            total = total + "sixty" + convert(number[1])
        if number[0] == "7":
            total = total + "seventy" + convert(number[1])
        if number[0] == "8":
            total = total + "eighty" + convert(number[1])
        if number[0] == "9":
            total = total + "ninety" + convert(number[1])
    if len(number) == 3:
        if number[0] == "1":
            total = total + "onehundred"
            if convert(number[1:]) != "":
                total = total +"and"+ convert(number[1] + number[2])
    if len(number) == 3:
        if number[0] == "2":
            total = total + "twohundred"
            if convert(number[1:]) != "":
                total = total +"and"+ convert(number[1] + number[2])
    if len(number) == 3:
        if number[0] == "3":
            total = total + "threehundred"
            if convert(number[1:]) != "":
                total = total +"and"+ convert(number[1] + number[2])
    if len(number) == 3:
        if number[0] == "4":
            total = total + "fourhundred"
            if convert(number[1:]) != "":
                total = total +"and"+ convert(number[1] + number[2])
    if len(number) == 3:
        if number[0] == "5":
            total = total + "fivehundred"
            if convert(number[1:]) != "":
                total = total +"and"+ convert(number[1] + number[2])
    if len(number) == 3:
        if number[0] == "6":
            total = total + "sixhundred"
            if convert(number[1:]) != "":
                total = total +"and"+ convert(number[1] + number[2])
    if len(number) == 3:
        if number[0] == "7":
            total = total + "sevenhundred"
            if convert(number[1:]) != "":
                total = total +"and"+ convert(number[1] + number[2])
    if len(number) == 3:
        if number[0] == "8":
            total = total + "eighthundred"
            if convert(number[1:]) != "":
                total = total +"and"+ convert(number[1] + number[2])
    if len(number) == 3:
        if number[0] == "9":
            total = total + "ninehundred"
            if convert(number[1:]) != "":
                total = total +"and"+ convert(number[1] + number[2])
    if len(number) == 4:
        if number == "1000":
            total = total + "onethousand"
    return total

mystring = ""
for i in range(1, 1001):
    mystring = mystring + convert(str(i))
print(mystring)
print(len(mystring))
# print(convert("101"))
