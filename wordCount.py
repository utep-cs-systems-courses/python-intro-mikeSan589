#!/usr/bin/env python3

from collections import Counter
import re
import sys

def count_words(source_file, destination_file):
    with open(source_file, 'r') as infile:
        content = infile.read().lower()

    all_words = re.findall(r'\b\w+\b', content)
    word_frequency = Counter(all_words)
    sorted_words = sorted(word_frequency.items())

    # sorted word counts to file 
    with open(destination_file, 'w') as outfile:
        for word, frequency in sorted_words:
            outfile.write(f"{word} {frequency}\n")

if __name__ == "__main__":
    source_file = sys.argv[1]
    destination_file = sys.argv[2]

    count_words(source_file, destination_file)

