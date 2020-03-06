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
        self.gsp_pattern = re.compile('')
        self.nickname_pattern = re.compile('')

    def parse_state_info(self):
        for file_name in self.files:
            self.parse_file(file_name)

    def parse_file(self, file_name):
        fobj = open(file_name)
        lines = fobj.readlines()
        for line in lines:
            title_match = self.title_pattern.search(line)
            if title_match is not None:
                print(title_match.group())


def get_wikipedia_files():
    files = os.listdir(os.path.curdir)
    for file_name in files:
        if ".txt" not in file_name:
            files.remove(file_name)

    return files


if __name__ == "__main__":
    parser = StateInfoParser()
    parser.parse_state_info()
