from emoji import UNICODE_EMOJI
import re
import sys, os
from googletrans import Translator
from langdetect import detect
import math
from bisect import bisect_left

from .sentimoji import get_emoji_sentiment_rank

def load_docs(source, mode='train'):
    documents = {'data': [], 'target_names': [], 'ids': []}
    with open(source, 'r', encoding='utf-8') as inf:
        # skipping header row
        next(inf)
        for line in inf:
            if mode == 'predict':
                (recid, review) = re.split('\t', line.strip())
                documents['data'].append(review)
                documents['ids'].append(recid)
            else:
                # both train and test have this format
                (review, cat) = re.split('\t', line.strip())
                documents['data'].append(review)
                documents['target_names'].append(cat)
    return documents
    
def get_all_emojis():
    if not hasattr(get_all_emojis, "all_emojis"):
        get_all_emojis.all_emojis = {}
        for c in UNICODE_EMOJI:
            get_all_emojis.all_emojis['has-emoji({})'.format(c)] = (False)
    return get_all_emojis.all_emojis


# The emoji feature classifier
def document_emoji_feature(document_words, features):
    all_emojis = get_all_emojis()
    features.update(all_emojis)
    allchars = set(''.join(document_words))
    score = 0.0
    emojis = []
    for c in allchars:
        if c in UNICODE_EMOJI:
            emojis.append(c)
            features['has-emoji({})'.format(c)] = (True)
            sentiment = get_emoji_sentiment_rank(c)
            if sentiment is not False:
                score += sentiment['sentiment_score']
    features['emoji-positive'] = (False)
    features['emoji-negative'] = (False)
    features['emoji-neutral'] = (False)
    if len(emojis) > 0:
        score /= len(emojis)
    if score > 0.2:
        features['emoji-positive'] = (True)
    elif score < -0.2:
        features['emoji-negative'] = (True)
    else:
        features['emoji-neutral'] = (True)

def get_emojis_from_text(text):
    score = 0.0
    # Putting in a random emoji to avoid empty data
    emojis = ["🦻"]
    for c in text:
        if c in UNICODE_EMOJI:
            emojis.append(c)
            sentiment = get_emoji_sentiment_rank(c)
            if sentiment is not False:
                score += sentiment['sentiment_score']
    if len(emojis) > 0:
        score /= len(emojis)
    if score > 0.2:
        label = 'Positive'
    elif score < -0.2:
        label = 'Negative'
    else:
        label = 'Neutral'
    return ((emojis, label))


def get_doc_len_range(document_words):
    return (get_range(len(document_words)))


def get_range(doclen):
    ranges = ["1-10", "11-20", "21-30", "31-40", "41-50", "51-60", "61-70", "71-80", "81-90", "91-100", "101-110", "111-120", "121-130", "131-140",
              "141-150", "151-160", "161-170", "171-180", "181-190", "191-200", ">200"]
    breakpoints = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100,
                   110, 120, 130, 140, 150, 160, 170, 180, 190, math.inf]
    index = bisect_left(breakpoints, doclen)
    return ranges[index]
def get_language(text):
      #translator = Translator()
      try:
        return(detect(text))
      except:
        return("unknown")
      # if (language.confidence > 0.7): return language.lang
      # return "unknown"

def detect_lang_and_store(inputfile, outputfile):
  with open(inputfile) as inf, open(outputfile, "w") as f:
    for text in inf:
      # Intentional re-init of object - https://stackoverflow.com/questions/49497391/googletrans-api-error-expecting-value-line-1-column-1-char-0
      translator = Translator()
      try:
        text = text.strip()
        language = translator.detect(text)
        f.write(text + "\t" + language.lang + "\t" + str(language.confidence) + "\n")
      except Exception as e:
        print(str(e))
        continue
  f.close()

if __name__ == "__main__":
    # features = {}
    # document_words = 'ugh 🤢'
    # document_emoji_feature(document_words, features)
    # print(features)
    # document_words = 'கலக்கல் 🤩'
    # document_emoji_feature(document_words, features)
    # print(features)
    # detect_lang_and_store(["idhu enna maayam", "sundari kannaal oru sedhi", "malalayali aano", "கலக்கல்", "nandri hai"], "/tmp/languages_tmp.tsv")
    detect_lang_and_store(os.path.join(os.path.dirname(sys.path[0]),'../../resources/data/alltexts.txt'), os.path.join(os.path.dirname(sys.path[0]),'../../resources/data/alltextslang.txt'))