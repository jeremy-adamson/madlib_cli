
def read_template(fileToRead):
    with open(fileToRead, "r") as file:
        return file.read()

def parse_template(madLib):
    parts_of_speech = []
    stripped_string = madLib
    length = len(madLib)
    index = 0
    while index < length:
        if madLib[index] == "{":
            close = index + 1
            while madLib[close] != "}":
                close+=1
            parts_of_speech.append(madLib[index+1:close])
            stripped_string = stripped_string[0:index+1] + stripped_string[close:]
        index+=1
    return_parts = tuple(parts_of_speech)
    return stripped_string, return_parts

def user_inputs(parts_of_speech):
    user_answers = []
    for term in parts_of_speech:
        ans = input(f"Please enter a {term}: ")
        user_answers.append(ans)
    return tuple(user_answers)

def merge(stripped_string, answers):
    string_to_return = stripped_string
    length = len(stripped_string)
    index = 0
    occurence = 0
    while index < length:        
        if string_to_return[index] == "{":
            close = index + 1
            string_to_return = string_to_return[0:index] + answers[occurence] + string_to_return[close+1:]
            occurence+=1
        index+=1
    return string_to_return


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
        print (madLib)
    return madLib

def savetofile(filetoread, madLib):
    newfile = filetoread[0:-4] + "_output.txt"
    with open(newfile, "w") as file:
        file.write(madLib)
    return newfile

if __name__ == "__main__":
    nameoffile = "short_example_template.txt"
    madlib_string = read_template(nameoffile)
    parsed, parts = parse_template(madlib_string)
    answers = user_inputs(parts)
    filled_string = merge(parsed, answers)
    savetofile(nameoffile, filled_string)





