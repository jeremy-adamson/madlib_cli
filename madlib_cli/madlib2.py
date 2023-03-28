def readfile(fileToRead):
    with open(fileToRead, "r") as file:
        return file.read()

def identifylocations(madLib):
    locations = []
    length = len(madLib)
    index = 0
    while index < length:
        if madLib[index] == "{":
            close = index + 1
            while madLib[close] != "}":
                close+=1
            term = madLib[index+1:close]
            locations.append({"index_open":index, "index_close":close, "term": term})
        index+=1
    return locations

def userinputs(locations):
    for word in locations:
        element = word.get("term")
        term = input (f"Please enter a {element}: ")
        word.update({"replacewith": term})

def replaceinstring(madLib, locations):
    locations.reverse()
    for term in locations:
        madLib = madLib[0:term.get("index_open")] + term.get("replacewith") + madLib[term.get("index_close")+1:]
    return madLib

def savetofile(filetoread, madLib):
    newfile = filetoread[0:-4] + "_complete.txt"
    with open(newfile, "w") as file:
        file.write(madLib)
    return newfile

nameoffile = "short_example_template.txt"
madlib_string = readfile(nameoffile)
userinputlist = identifylocations(madlib_string)
userinputs(userinputlist)
madlib_string = replaceinstring(madlib_string, userinputlist)
print(madlib_string)


savetofile(nameoffile, madlib_string)