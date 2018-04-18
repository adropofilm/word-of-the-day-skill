import urllib as urllib2
from bs4 import BeautifulSoup


def replace_all(text, dictionary):
    for i, j in dictionary.iteritems():
        text = text.replace(i,j)
    return text

url = "http://www.dictionary.com/wordoftheday/"

website = urllib2.urlopen(url)

soup = BeautifulSoup(website, 'html.parser')

# Extract word of day:
word = soup.title.string
replace_dict = { 'Get the Word of the Day - ': '', ' | Dictionary.com': '' }
word_of_day = replace_all(word, replace_dict)

# Extract definition:
defin = soup.ol.li.span
def_str = str(defin)
replace_dict = { '<span>': '', '<em>': '', '</em>': '', '</span>': ''}
def_str = replace_all(def_str, replace_dict)


# print "Word of the day: ", word_of_day
# print "Definition: ", def_str



