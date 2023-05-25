#! /usr/bin/env python3

from sys import argv
import sys
import re

input_file = argv[1]
judge_answer = argv[2]
feedback_dir = argv[3]

try:
    submission_output = []
    while True:
        try:
            submission_output.append(input().strip())
        except EOFError:
            break

    judge_answers = []
    with open(judge_answer, 'r') as file:
        for line in file.readlines():
            line = line.strip()
            if line:
                judge_answers.append(line)


    if len(judge_answers) != len(submission_output):
        sys.exit(43)

    for judge, sub in zip(judge_answers, submission_output):
        if 'Impossible' in {judge, sub}:
            if judge != sub:
                sys.exit(43)
            else:
                continue
        if sub == '':
            sys.exit(43)
        if not re.match("([0-9]|\.)+", sub):
            sys.exit(43)
        if abs(float(judge) - float(sub)) > 0.1:
            sys.exit(43)
except:
    sys.exit(43)

sys.exit(42)