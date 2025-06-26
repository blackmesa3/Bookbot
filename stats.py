def get_book_wc(filepath):
    with open(filepath) as f:
        Text = f.read()         
        count = str(len(Text.split()))
    return count

def get_book_cc(filepath):
    dictionary = {}
    with open(filepath) as f:
        readtext = f.read()
        flist = [c for c in readtext.lower()]
        for i in flist:
            if i in dictionary:
                dictionary[i] += 1
            else:
                dictionary[i] = 1
    return dictionary

def sort_on(items):
    return items["num"]

def dicksorter(dictionary):

    newlist = []

    for i in dictionary:
        newdict = {"char": i, "num": dictionary[i]}
        newlist.append(newdict)

    newlist.sort(reverse=True, key=sort_on)
        
    for letter in newlist:
        if str(letter["char"]).isalpha():
            print (letter["char"] + ": " + str(letter["num"]) )
    return