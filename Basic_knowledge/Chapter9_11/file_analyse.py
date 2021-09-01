# -*- coding: utf-8 -*-
"""
文本分析

Created on Wed Sep  1 16:56:04 2021

@author: Meng Qiangfan
"""

def words_count(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file '{filename}' has about {num_words} words.")
        return num_words


def special_words_count(filename, word):
    """Count the approximate number of the appointed word in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")
    else:
        num_words = contents.lower().count(word)
        print(f"The file '{filename}' has about {num_words} '{word}'.")
        return num_words
