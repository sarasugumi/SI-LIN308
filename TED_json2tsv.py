#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
# Tiny script to convert JSON into TXT
# Copyright: 2017-2021 Nara Institute of Science and Technology
#

import sys
import json
from argparse import ArgumentParser

def normalize (line):
    return line.replace("　", " ").replace('\n', ' ').replace("  ", " ")

def extract (jsonfp):
    jsonobj = json.load (jsonfp)
    if "paragraphs" not in jsonobj:
        raise RuntimeError ("Invalid JSON data")
    for paragraph in jsonobj["paragraphs"]:
        for cue in paragraph["cues"]:
            yield (int(cue["time"]), normalize(cue["text"]))

def main ():
    argparser = ArgumentParser ()
    argparser.add_argument ("json", help="JSON file.")
    args = argparser.parse_args()

    with open (args.json, 'rt') as jsonfp:
        prev = None
        for time, text in extract (jsonfp):
            if prev != None:
                print ("%d\t%d\t%s" % (prev[0], time, prev[1]))
            prev = (time, text)
        print ("%d\t%d\t%s" % (prev[0], prev[0], prev[1]))

if __name__ == "__main__":
    try:
        main ()
    except Exception as e:
        raise e
