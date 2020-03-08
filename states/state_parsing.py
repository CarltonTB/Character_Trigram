# Author: Carlton Brady (solo)
# CISC689 HW1 Q4

import re
import os
import csv


class State:

    def __init__(self, name, nicknames, gsp):
        self.name = name
        self.nicknames = nicknames
        self.gsp = gsp


class StateInfoParser:

    def __init__(self):
        self.state_info = {}
        self.files = get_wikipedia_files()
        self.title_pattern = re.compile('<title>[-a-zA-Z ]+</title>')
        self.gsp_line_pattern = re.compile('([gG]ross|[Tt]otal) state product.+\\$[0-9\\.,]+.*([Tt]rillion|[BbMm]illion)')
        self.gsp_dollar_amount_pattern = re.compile('\\$[0-9\\.,]+')
        self.gsp_magnitude_pattern = re.compile('[Tt]rillion|[BbMm]illion')
        self.nickname_line_pattern = re.compile('[Nn]ickname\(s\).+</tr>.+mottos')
        self.nickname_value_pattern = re.compile('>[a-zA-z ;()]+<')

    def parse_state_info(self):
        for file_name in self.files:
            self.parse_file(file_name)

    def parse_file(self, file_name):
        fobj = open(file_name)
        lines = fobj.readlines()
        gsp_match_count = 0
        state_name = None
        gsp_amount = None
        gsp_magnitude = None
        nicknames = None
        for line in lines:
            title_match = self.title_pattern.search(line)
            if title_match is not None:
                title_line = title_match.group()
                start_index = title_line.index(">") + 1
                end_index = title_line.index("-") - 1
                state_name = title_line[start_index:end_index]

            gsp_line_match = self.gsp_line_pattern.search(line)
            if gsp_line_match is not None:
                gsp_match_count += 1
                if gsp_match_count == 1:
                    gsp_line = gsp_line_match.group()
                    dollar_amount_match = self.gsp_dollar_amount_pattern.search(gsp_line)
                    gsp_amount = dollar_amount_match.group()
                    magnitude_match = self.gsp_magnitude_pattern.search(gsp_line)
                    gsp_magnitude = magnitude_match.group()
                    print(state_name + ":", gsp_amount, gsp_magnitude)

            nickname_line_match = self.nickname_line_pattern.search(line)
            if nickname_line_match is not None:
                nicknames_line = nickname_line_match.group()
                nicknames_match = self.nickname_value_pattern.findall(nicknames_line)
                for name in parse_nicknames(nicknames_match):
                    print(name)

        fobj.close()


def get_wikipedia_files():
    files = os.listdir(os.path.curdir)
    for file_name in files:
        if ".txt" not in file_name:
            files.remove(file_name)

    return files


def parse_nicknames(nicknames_list):
    new_list = []
    carry = None
    for i in range(0, len(nicknames_list)):
        name = nicknames_list[i][1:len(nicknames_list[i])-1]
        name = name.strip()
        name_words = name.split(" ")
        if len(name_words) == 1:
            if ";" in name_words[0]:
                # this word is part of the previous nickname
                new_list[len(new_list)-1] = (new_list[len(new_list)-1] + " " + name).replace(";", "")

            elif i == len(nicknames_list)-1:
                # This is the last single word so it must be part of the previous nickname
                for k in range(len(new_list)-1, 0, -1):
                    if len(new_list[k]) > 0:
                        new_list[k] = (new_list[k] + " " + name).replace(";", "")
            else:
                # this word is part of the next nickname
                carry = name
        else:
            if carry is not None:
                new_list.insert(i, carry + " " + name)
                carry = None
            else:
                semi_colon_split = name.split(";")
                if len(semi_colon_split) > 1:
                    for j in range(0, len(semi_colon_split)):
                        new_list.insert(i + j, semi_colon_split[j].strip())
                else:
                    new_list.insert(i, name.replace(";", ""))

    # Remove empty entries in the list
    for name in new_list:
        if len(name) == 0:
            new_list.remove(name)

    return new_list


if __name__ == "__main__":
    parser = StateInfoParser()
    parser.parse_state_info()
