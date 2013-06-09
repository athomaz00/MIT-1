# 6.00 Problem Set 5
# RSS Feed Filter

# Problem Set 5
# Name: Joshua Cole
# Time: 3:00

import feedparser
import string
import time
from project_util import translate_html
from news_gui import Popup

#-----------------------------------------------------------------------
#
# Problem Set 5

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        summary = translate_html(entry.summary)
        try:
            subject = translate_html(entry.tags[0]['term'])
        except AttributeError:
            subject = ""
        newsStory = NewsStory(guid, title, subject, summary, link)
        ret.append(newsStory)
    return ret

#======================
# Part 1
# Data structure design
#======================

# Problem 1

class NewsStory:
    guid = ""
    title = ""
    subject = ""
    summary = ""
    link = ""

    def __init__(self, guid, title, subject, summary, link):
        self.guid = guid
        self.title = title
        self.subject = subject
        self.summary = summary
        self.link = link

    def get_guid(self):
        return self.guid

    def get_title(self):
        return self.title

    def get_subject(self):
        return self.subject

    def get_summary(self):
        return self.summary

    def get_link(self):
        return self.link
    

#======================
# Part 2
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError


# Whole Word Triggers
# Problems 2-5

class WordTrigger(Trigger):
    word = ""

    def __init__(self, word):
        self.word = word.lower()
    
    def is_word_in(self, text):
        """
        Returns True if the whole word 'word' is present
        in text, or False otherwise.
        """
        text = text.lower()
        for letter in string.punctuation:
            text = text.replace(letter, " ")
        return self.word in text.split(" ")


class TitleTrigger(WordTrigger):
    def evaluate(self, story):
        return self.is_word_in(story.get_title())

class SubjectTrigger(WordTrigger):
    def evaluate(self, story):
        return self.is_word_in(story.get_subject())

class SummaryTrigger(WordTrigger):
    def evaluate(self, story):
        return self.is_word_in(story.get_summary())


# Composite Triggers
# Problems 6-8
class NotTrigger(Trigger):
    trigger = None

    def __init__(self, trigger):
        self.trigger = trigger

    def evaluate(self, story):
        return not self.trigger.evaluate(story)

class NotTrigger(Trigger):
    trigger = None

    def __init__(self, trigger):
        self.trigger = trigger

    def evaluate(self, story):
        return not self.trigger.evaluate(story)

class AndTrigger(Trigger):
    trigger_one = None
    trigger_two = None
    
    def __init__(self, trigger_one, trigger_two):
        self.trigger_one = trigger_one
        self.trigger_two = trigger_two

    def evaluate(self, story):
        return self.trigger_one.evaluate(story) and self.trigger_two.evaluate(story)

class OrTrigger(Trigger):
    trigger_one = None
    trigger_two = None
    
    def __init__(self, trigger_one, trigger_two):
        self.trigger_one = trigger_one
        self.trigger_two = trigger_two

    def evaluate(self, story):
        return self.trigger_one.evaluate(story) or self.trigger_two.evaluate(story)


# Phrase Trigger
# Question 9

class PhraseTrigger(Trigger):
    phrase = ""

    def __init__(self, phrase):
        self.phrase = phrase

    def evaluate(self, story):
        return self.phrase in story.get_title() or self.phrase in story.get_subject() or self.phrase in story.get_summary()


#======================
# Part 3
# Filtering
#======================

def filter_stories(stories, triggerlist):
    def filter_function(story):
        for trigger in triggerlist:
            if trigger.evaluate(story):
                return True
        return False
    return filter(filter_function, stories)

#======================
# Part 4
# User-Specified Triggers
#======================

def readTriggerConfig(filename):
    """
    Returns a list of trigger objects
    that correspond to the rules set
    in the file filename
    """
    # Here's some code that we give you
    # to read in the file and eliminate
    # blank lines and comments
    triggerfile = open(filename, "r")
    all = [ line.rstrip() for line in triggerfile.readlines() ]
    lines = []
    for line in all:
        if len(line) == 0 or line[0] == '#':
            continue
        lines.append(line)

    added_triggers = []
    triggers = {}
    for line in lines:
        parts = line.split(" ")
        if parts[0] == "ADD":
            for name in parts[1:]:
                added_triggers.append(triggers[name])
        if parts[1] == "TITLE":
            triggers[parts[0]] = TitleTrigger(parts[2])
        elif parts[1] == "SUBJECT":
            triggers[parts[0]] = SubjectTrigger(parts[2])
        elif parts[1] == "SUMMARY":
            triggers[parts[0]] = SummaryTrigger(parts[2])
        elif parts[1] == "PHRASE":
            triggers[parts[0]] = PhraseTrigger(" ".join(parts[2:]))
        elif parts[1] == "AND":
            triggers[parts[0]] = AndTrigger(triggers[parts[2]], triggers[parts[3]])
        elif parts[1] == "NOT":
            triggers[parts[0]] = NotTrigger(triggers[parts[2]])
        elif parts[1] == "OR":
            triggers[parts[0]] = OrTrigger(triggers[parts[2]], triggers[parts[3]])
    return added_triggers
        
import thread

def main_thread(p):
    # A sample trigger list - you'll replace
    # this with something more configurable in Problem 11
    t1 = SubjectTrigger("Obama")
    t2 = SummaryTrigger("MIT")
    t3 = PhraseTrigger("Supreme Court")
    t4 = OrTrigger(t2, t3)
    triggerlist = [t1, t4]
    
    # TODO: Problem 11
    # After implementing readTriggerConfig, uncomment this line 
    triggerlist = readTriggerConfig("triggers.txt")

    guidShown = []
    
    while True:
        print "Polling..."

        # Get stories from Google's Top Stories RSS news feed
        stories = process("http://news.google.com/?output=rss")
        # Get stories from Yahoo's Top Stories RSS news feed
        stories.extend(process("http://rss.news.yahoo.com/rss/topstories"))

        # Only select stories we're interested in
        stories = filter_stories(stories, triggerlist)
    
        # Don't print a story if we have already printed it before
        newstories = []
        for story in stories:
            if story.get_guid() not in guidShown:
                newstories.append(story)
        
        for story in newstories:
            guidShown.append(story.get_guid())
            p.newWindow(story)

        print "Sleeping..."
        time.sleep(SLEEPTIME)

SLEEPTIME = 60 #seconds -- how often we poll
if __name__ == '__main__':
    p = Popup()
    thread.start_new_thread(main_thread, (p,))
    p.start()

