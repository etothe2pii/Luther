# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import language
import parse_input
import sys
import scanner_data


def check_char(data, line, char_num, character, new_line, output, languages, fail = False):
    empty, match, matched_string, match_start, match_end = data.check_next(language.convert_to_ascii(character), new_line, line, char_num, fail)
    if (empty and match != None):
        if (match.value != None):
            matched_string = match.value

        output.append([match.token_id, matched_string, match_start[0] + 1, match_start[1] + 1])
        line = match_end[0]
        char_num = match_end[1]


        data = scanner_data.Data(match_end, languages.copy())

    return line, char_num, data, empty




scanning_input_string = sys.argv[1]
token_input_string = sys.argv[2]
output_string = sys.argv[3]


languages = parse_input.get_input(scanning_input_string)
token_stream_raw = open(token_input_string)
token_stream = token_stream_raw.readlines() + [-1]
line = 0
char_num = 0
output = []
data = scanner_data.Data([0,0], languages.copy())



while(line < len(token_stream)):

    while(line < len(token_stream) and token_stream[line] != -1 and char_num < len(token_stream[line])):
        print(output)
        line, char_num, data, empty = check_char(data, line, char_num, token_stream[line][char_num] , char_num == len(token_stream[line])-1, output, languages)
        if(not empty):
            char_num += 1

    if token_stream[line] == -1:
        line, char_num, data, empty = check_char(data, line, char_num, languages[0].valid_char[0], False, output, languages, fail = True)
        if(line == len(token_stream) - 1):
            break
    #line, char_num, data, empty = check_char(data, line, char_num, "\n", True, output, languages)
    else:
        char_num = 0
        line += 1
    #new_line = True


output_file = open(output_string, "w")


for o in output:
    s = ""
    for u in o:
        s += str(u) + " "
    output_file.write(s + "\n")