import codecs
import json

import sys


def load_data(filepath):
    with codecs.open(filepath, 'r', encoding='utf-8', errors='ignore') as opened_file:
        return opened_file.read()


def pretty_print_json(opened_file):
    print(json.dumps(json.loads(opened_file), sort_keys=True, indent=4))


if __name__ == '__main__':
    path_to_file = sys.argv[1]
    pretty_print_json(load_data(path_to_file))
