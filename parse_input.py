import language
def get_input(input_file):
    program_file = open(input_file)
    languages = program_file.readlines()

    valid_char_raw = languages[0]
    valid_char = []

    i = 0
    while i < len(valid_char_raw):
        if(valid_char_raw[i] == "x"):
            valid_char.append(valid_char_raw[i:i+3].lower())
            i+=2
        elif valid_char_raw[i]!= " ":
           valid_char.append(language.convert_to_ascii(valid_char_raw[i]))

        i+=1
    valid_char.pop(len(valid_char)-1)
    languages.pop(0)
    languages_output = []

    for l in languages:
        args = l.split()
        #print(l, ", ", args)
        if(len(args) != 0):
            tmp_file = open(args[0])
            lines = tmp_file.readlines()
            tmp_dfa = []
            for i in lines:
                tmp_dfa.append(i.split())
            if(len(args) == 3):
                languages_output.append(language.Language(tmp_dfa, valid_char, args[1], args[2]))
            else:
                languages_output.append(language.Language(tmp_dfa,valid_char, args[1]))
    return languages_output








