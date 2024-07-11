#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""


def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', 'Aaron 57', 'Abagail 895', ' ...]
    """
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()

    # Extract the year
    year_match = re.search(r'Popularity\sin\s(\d\d\d\d)', text)
    if not year_match:
        raise ValueError("Could not find the year in the file")
    year = year_match.group(1)

    # Extract the names and rank numbers
    name_rank_tuples = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', text)

    # Store in a dictionary
    name_rank_dict = {}
    for rank, boy_name, girl_name in name_rank_tuples:
        if boy_name not in name_rank_dict or int(rank) < int(name_rank_dict[boy_name]):
            name_rank_dict[boy_name] = rank
        if girl_name not in name_rank_dict or int(rank) < int(name_rank_dict[girl_name]):
            name_rank_dict[girl_name] = rank

    # Convert dictionary to a sorted list
    name_rank_list = [year] + [f"{name} {rank}" for name, rank in sorted(name_rank_dict.items())]

    return name_rank_list


def main():
    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]

    if not args:
        print('usage: [--summaryfile] file [file ...]')
        sys.exit(1)

    # Notice the summary flag and remove it from args if it is present.
    summary = False
    if args[0] == '--summaryfile':
        summary = True
        del args[0]

    # For each filename, get the names, then either print the text output
    # or write it to a summary file
    for filename in args:
        name_rank_list = extract_names(filename)
        text = '\n'.join(name_rank_list) + '\n'

        if summary:
            with open(filename + '.summary', 'w') as summary_file:
                summary_file.write(text)
        else:
            print(text)


if __name__ == '__main__':
    main()
