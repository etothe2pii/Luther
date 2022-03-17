class Language:

    dfa = []
    token_id = ""
    value = None
    state = 0
    current_sequence = ""
    valid_char = []
    def __init__(self, dfa, valid_char, token_id):
        self.dfa = dfa
        self.token_id = token_id
        self.valid_char = valid_char


    #Returns bool: did it match bool: is it accepting string: current sequence
    def match_char(self, character):
        if(self.dfa[int(self.state)][self.valid_char.index(character) + 2] == "E"):
            tmp_sequence = self.current_sequence
            self.current_sequence = ""
            self.state = 0
            return False, False, tmp_sequence
        else:
            self.current_sequence += convert_to_ascii(character)
            self.state = self.dfa[int(self.state)][self.valid_char.index(character) + 2]
            return (character in self.valid_char), (self.dfa[int(self.state)][0] == "+"), self.current_sequence

    def __repr__(self):
        s = self.token_id + "\n"
        for d in self.dfa:
            for f in d:
                s += f + " "
            s += "\n"
        s += "\n"
        return s

def convert_to_ascii(character):
    if(len(character) == 3):
        return character
    ascii_value = hex(ord(character))[1:]
    if(len(ascii_value) == 2):
        ascii_value = ascii_value[0] + "0" + ascii_value[1]

    return ascii_value
