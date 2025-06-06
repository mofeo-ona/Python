
def display_menu():
    print("welcome to txt2speech")
    print("""
        c = convert sentence
        a = add word
        p = print sentence
        d = delete
        q = quit

""")
    
def convert():
    sentence = input("Enter a sentence to translate\n").upper() 
    for char in ",.!'":
          sentence = sentence.replace(char,"")

    translated = " "
    wrd2Translate = sentence.split()

    for word in wrd2Translate:
        if word in txt2speech:
            translated += txt2speech[word] + " "
    else:
        translated += word + " "
    print(translated)

def prnt():
    print(txt2speech)

def add():
    print("what is the word")
    wrd=input().upper()
    print("what does it mean?")
    mean=input()
    txt2speech[wrd]=mean

def delete():
    print("what do you want to delete")
    dele=input().upper()
    del txt2speech[dele]



txt2speech = {
    "BRB": "Be Right Back",
    "FYI": "For Your Information",
    "OYO":"On Your Own"

}

y = True
display_menu()
while y == True:
    ques=input().lower()
    if ques == "c":
        convert()
    elif ques == "a":
        add()
    elif ques == "p":
        prnt()
    elif ques == "d":
        delete()
    elif ques == "q":
        y=False
    else:
        print("choose a valid option")

#x=True
#while x == True:
    #print("what do you want to translate")
    #abbr=input().upper()

    #if abbr=="BRB":
        #print(txt2speech["BRB"])
    #elif abbr == 'FYI':
        #print(txt2speech["FYI"])
    #elif abbr == "OYO":
        #print(txt2speech["OYO"])
    #else:
        #print("no")

    #print("do you want to continue (y/n)")
    #ans=input().lower()

    #if ans == "n":
        #x=False



