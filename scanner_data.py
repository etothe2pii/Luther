import language



class Data:

    #loc: 0: line 1: char
    def __init__(self, ch_loc, token_set,  best_match = None, best_matched_string = None):
        self.ch_loc = ch_loc
        self.token_set = token_set
        self.best_match = best_match
        self.best_matched_string = best_matched_string
        self.end_loc = self.ch_loc.copy()
        self.best_loc = self.end_loc.copy()

    #returns bool: token set empty, language: best match, string: best_matched_string, start location for the match
    def check_next(self, character, new_line, line, char_num, fail):
        changed = False
        i = 0

        self.end_loc[1] += 1
        if (new_line):
            self.end_loc[0] += 1
            self.end_loc[1] = 0


        while(i < len(self.token_set)):
            match, accept, current = self.token_set[i].match_char(character)



            if(not match or fail):
                self.token_set.pop(i)
                i -= 1
            elif(accept and match and not changed):
                self.best_match = self.token_set[i]
                self.best_matched_string = current
                self.best_loc = self.end_loc.copy()
                changed = True

            i += 1



        return (len(self.token_set) == 0), self.best_match, self.best_matched_string, self.ch_loc, self.best_loc
