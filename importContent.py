import fileinput
from pickle import Pickler, Unpickler
import os
import sys

from question import Question

def importContent():
    if "." + sys.argv[1] + ".mdq" in os.listdir() and os.stat("." + sys.argv[1] + ".mdq").st_size != 0:
        readFile = open("." + sys.argv[1] + ".mdq", 'rb')
        return Unpickler(readFile).load();
    questions = []
    given = ""
    answer = ""

    for line in fileinput.input():
        if line[0] == "#":
            if not answer.isspace() and not given.isspace() and answer != "":
                questions.append(Question(given=given.rstrip(), answer=answer.rstrip()))
                answer = ""
            given = line[2:]
        elif not line.isspace():
            answer += line
        else:
            pass
    questions.append(Question(given=given, answer=answer))
    writeFile = open("." + sys.argv[1] + ".mdq", 'wb+')
    Pickler(writeFile).dump(questions)
    return questions
