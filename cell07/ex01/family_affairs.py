#!/usr/bin/env python3

def find_the_redheads(family):
    redheads = filter(lambda item: item[1] == "red", family.items())
    return [name for name, color in redheads]


dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))