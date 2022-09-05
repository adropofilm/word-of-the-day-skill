
# Word Of The Day Skill
A case study on the Mycroft AI powered word of the day skill I wrote in 2018.

### Description 
Welcome to my case study of the Word of the Day Skill! This skill was intended to leverage [Mycroft](https://github.com/MycroftAI/mycroft-core), the hackable open source voice assistant to provide you the "word of the day" and its definition. Current words and definitions come from 
[Dictionary.com.](Dictionary.com)

### Table of Contents
 - [What I would change today](#what-i-would-change-today)
 - [Usage](#usage)
 - [Credits](#credits)

###  What I would change today
Ok folks, it's 2022! It's been about 4 years since I've worked on this project. I don't intend on refactoring, primarily to use this as a learning opportunity, but here are some notes on what I would change today:
1. **Use an http client**:
    - **Why did I not use one?** Hard to believe, but in 2018, there was no readily available word of the day APIs that I could use (or afford on a college student's budget, or lack thereof) Instead I opted to use [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) to scrape the data I needed from the html. 
    - **How does this pose potential issues?** Relying on scraping HTML can cause broken functionality, especially since the UI is expected to change (and I'm sure it has). It's not as reliable as working with an API where you know you will get the exact data you need in the format you need it.
    - **Which client would I use now?** Most likely [requests](https://requests.readthedocs.io/en/latest/) or  [urllib3](https://urllib3.readthedocs.io/en/stable/) since both have all the functionality I'd need to make a basic GET request in addition to human-friendly documentation. :) 
2. **Write More Tests**:
   - **Why?** To make sure that the skill works, duh! The software test engineer in me today is shaking at the fact that I only wrote 1 test for this 4 years ago. Especially since there are at least 3 other *meaningful* tests I could have written for it.
3. **Write code that's more readable**:
    - I'd take a gander to say that you are probably a fan of code that is easy to read. I mean, who isn't?! There are several ways to employ this, but in this case, I would have changed the code below to be self-documenting, by extracting methods with names that tell exactly what they're doing:
    ``` python 
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
    ``` 
to look a little more something like
  

    def handle_word_of_the_day_intent(self, message):
        unextracted_word = get_word()
        extracted_word = extract_word()
        speak_word(extracted_word)
      

   - **Why does this help?** Because it gives cleaner, conciser code. It doesn't require comments because the methods are named in such a way that it is obvious what the code does, and it shows you only what you need to do in the `handle_word_of_the_day_intent` method.
   

###  Usage
This skill is no longer useable since Dictionary.com has updated their UI and the instability of my code was exposed LOL. BUT, if it did work, you'd run [Mycroft](https://github.com/MycroftAI/mycroft-core) and say:
* "tell me the word of the day"
* "word of the day"
* "word of day"

###  Credits 
* Fatima Mohamed
* Dictionary.com 
* Mycroft AI
