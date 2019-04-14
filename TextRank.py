import bs4 as bs
##import urllib.request
import re
import os
import nltk
nltk.download('punkt')
nltk.download('stopwords')

"""
Gathering data from raw text selection. No cleaning should be needed because selection text 
from browsers does not include html tags.
"""
def ezRank(selection_text):
    sentence_list = nltk.sent_tokenize(selection_text)

    stopwords = nltk.corpus.stopwords.words('english')

    """
    Gathing setence scores and ranking them
    """
    word_frequencies = {}
    for word in nltk.word_tokenize(selection_text):
        if word not in stopwords:
            if word not in word_frequencies.keys():
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1

    maximum_frequncy = max(word_frequencies.values())

    for word in word_frequencies.keys():
        word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)

    sentence_scores = {}
    for sent in sentence_list:
        for word in nltk.word_tokenize(sent.lower()):
            if word in word_frequencies.keys():
                if len(sent.split(' ')) < 30:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word]
                    else:
                        sentence_scores[sent] += word_frequencies[word]

    import heapq
    summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)

    summary = ' '.join(summary_sentences)
    return(summary)

