#! /bin/sh

./templates.py | dot -Tsvg -Gsize=10,10\! -o templates.svg
