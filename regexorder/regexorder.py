#!/usr/bin/env python3

import os
import json
from functools import lru_cache
import regex as re

class RegexOrderNode(object):
    def __init__(self, order, name, parents, regex):
        self.order = order
        self.name = name
        self.parents = parents
        self.regex = regex

        self.__regex = re.compile(regex, re.U)


    def match(self, s):
        return self.__regex.fullmatch(s)


    def __str__(self):
        return self.name


class RegexOrder(object):
    __idAny = "any"
    __idNone = "none"

    def __init__(self, filename=None):
        if filename is None:
            filename = os.path.join(os.path.split(__file__)[0], "templates.json")

        with open(filename) as f:
            self.templates = {}

            for i, t in enumerate(json.load(f)):
                name = t["name"]
                self.templates[name] = RegexOrderNode(
                    -i,
                    name,
                    [self.templates[p] for p in t["parents"]],
                    t["regex"]
                )


    @lru_cache()
    def match(self, s, prev=None):
        if prev is None:
            prev = self.templates[RegexOrder.__idNone]

        if s == "":
            return prev

        res = None

        candidates = {prev}
        tried = set()
        while len(candidates):
            newcandidates = set()

            for t in candidates:
                if t in tried or res and res.order < t.order:
                    continue
                tried.add(t)

                if t.match(s):
                    res = t

                for p in t.parents:
                    if p not in tried and p not in candidates:
                        newcandidates.add(p)

            candidates = newcandidates

        return res


    def matchall(self, strs, prev=None):
        template = prev

        for s in strs:
            template = self.match(s, template)

        return template
