# coding=utf-8
import nltk

sentence = "Bhí an buachaill le cairde"
determiner = {'an', 'na'}
prepositions = {'ag', 'ar', 'as', 'chuig', 'chun', 'de', 'do', 'faoi', 'i', 'idir', 'le', 'ó', 'roimh', 'thar', 'trí',
                'um'}
output = []


def tokenize(word):
    tupled = [word]
    if word in prepositions:
        tupled.append("PREP")
    if word in determiner:
        tupled.append("DET")
    output.append(tupled)

split_sentence = sentence.split(" ")
for fragment in split_sentence:
    tokenize(fragment)

for item in output:
    print(item)