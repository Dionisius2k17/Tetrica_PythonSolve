#!/usr/bin/env python3
#Код проверялся на системах Linux (Ubuntu, MacOS)
from itertools import groupby
import wikipediaapi

def get_categorymembers(categorymembers):
    for c in categorymembers.values():
        yield c.title

wiki_wiki = wikipediaapi.Wikipedia('ru')
page_animal = wiki_wiki.page("Категория:Животные_по_алфавиту")

categories = get_categorymembers(page_animal.categorymembers)
next(categories)
categories = [c for c in categories if ' ' in c]
categories = sorted(categories)

groups = groupby(categories, lambda k: k[0])

for k, v in groups:
    if k >= 'Ё':
        print(k, ":", len(list(v)))


