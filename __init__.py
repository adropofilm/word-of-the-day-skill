# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.

from adapt.intent import IntentBuilder

from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

import urllib as urllib2
from bs4 import BeautifulSoup

__author__ = 'fmohamed'

LOGGER = getLogger(__name__)


class WordOfTheDaySkill(MycroftSkill):
    def __init__(self):
        super(WordOfTheDaySkill, self).__init__(name="WordOfTheDaySkill")

    def initialize(self):
        word_of_the_day_intent = IntentBuilder("WordOfTheDayIntent"). \
            require("WordOfTheDayKeyword").build()
        self.register_intent(word_of_the_day_intent, self.handle_word_of_the_day_intent)

    def replace_all(text, dictionary):
        for i, j in dictionary.iteritems():
            text = text.replace(i,j)
        return text

    def handle_word_of_the_day_intent(self, message):
        self.speak_dialog("word.of.day")

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

	self.speak("The word of the day is {}. The definition is as follows. {}".format(word_of_day, def_str)

        # print "Word of the day: ", word_of_day
        # print "Definition: ", def_str

    def stop(self):
        pass


def create_skill():
    return WordOfTheDaySkill()



