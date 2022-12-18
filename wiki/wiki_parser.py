import re
import lxml
import pandas as pd
import requests

from wiki.data import wikitem


def get_wiki_items():
    s = requests.Session()
    r = s.get('https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites')

    tables = pd.read_html(r.text, header=0)
    test_table = tables[0]
    parse_items = []
    for x in test_table.values:
        site = _format_text(x[0])
        front_end_lang = _format_text(x[2])
        back_end_lang = _format_text(x[3])
        popularity = _format_popularity(x[1])
        parse_items.append(wikitem.ParseItem(site, front_end_lang, back_end_lang, int(popularity)))

    return parse_items


def _format_text(text):
    x = re.sub("(\[[0-9]+])*", "", text)
    x = re.sub("\(([^\)]+)\)", "", x)
    x = re.sub("( ,+)", ",", x)
    return x


def _format_popularity(text):
    x = _format_text(text)
    x = re.sub("(,+)", "", x)
    return x
