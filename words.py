#! /usr/bin/env python3


import sys
from urllib.request import urlopen
from urllib.request import * 


def fetch_words(url):
    
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('latin-1').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words

 
def print_items(items):
    for item in items:
        print(item)


def principal(url):
        words = fetch_words(url)
        print_items(words)


print(__name__)

def square(x):
    return x * x


print(square(3))


if __name__ == '__main__':
    principal(sys.argv[1])


