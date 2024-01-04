print("Instructions:\ninput cancel to stop\notherwise it will keep going\n")
def numberDetect(text):
    nonum = None
    blacklist = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    for letters in text:
        for number in blacklist:
            if number != letters:
                nonum = True
            elif number == letters:
                return False
    return nonum

def reversal(text):
    text_length = int(len(text))
    if numberDetect(text):
        for number in range(1, text_length+1):
            print(text[number*-1], end="")
        print("")
    else:
        print("Number in the text! enter text only")
    print("")

while True:
    strings = input("Please enter a text to reverse!: ")
    if strings.lower() != "cancel":
        reversal(strings)
    else:
        print("Have a nice day")
        break

