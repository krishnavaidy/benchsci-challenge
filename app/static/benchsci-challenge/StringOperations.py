import re
from collections import Counter
from bs4 import BeautifulSoup

# Function that takes as input a string and removes tags (approximately)
def clean_string(s):
    soup = BeautifulSoup(s)
    return soup.get_text().encode('utf-8')

# Tokenizes string to alphanumeric
def tokenize_string(s):
    return Counter(re.findall('\w+',s.lower()))

def find_cooccurrence(d1, d2):
    s1 = set(d1)
    s2 = set(d2)

    cooccurrence = {}

    for x in s1.intersection(s2):
        cooccurrence[x] = min(d1[x],d2[x]) 

    return cooccurrence
