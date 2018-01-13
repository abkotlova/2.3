import json
from pprint import pprint

with open ("newsafr.json") as f:
    data = json.load(data_file)
    pprint (data)


def count_length (text):
    text_list = text.split(" ")
    text_set = set()
    for i in text_list:
        if len(i) > 6:
            text_set.add(i)
    word_value = {}
    for i in text_set:
        count = 0
        for j in text_list:
            if i == j:
                count += 1
        word_value[i] = count
    return word_value
