#! /usr/bin/env python3

import json

with open("regexorder/templates.json") as f:
    print("digraph {")

    for t in json.load(f):
        name = t["name"]

        print("\t{} [shape=box fontsize=20 style=filled];".format(t["name"]))

        if t["parents"]:
            print("\t{} -> {{{}}};".format(name, "; ".join(t["parents"])))

    print("}")
