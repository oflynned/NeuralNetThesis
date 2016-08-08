# coding=utf-8
import nltk

sentence =   [("Chonaic", "V"), ("an", "Det"), ("madra", "N"), ("an", "Det"), ("fear", "N"), ("i", "P"),("bpáirc", "N")]
#[("Chuaigh", "VBD"), ("Sean", "NNP"), ("chuig", "IN"),
#("an", "DT"), ("gcarr", "NN"), ("sean", "JJ"), ("mór", "JJ")]

grammar = r"""
    NP: {<Det>?<N><JJ>*}
    PP: {<P><NP>}
    """
	
"""
cp = nltk.RegexpParser(grammar)
result = cp.parse(sentence)
print(result)
result.draw()

"""
raw_sentence = "Chuamar chuig an stáisiúin. Cheap mise go raibh sé go maith. Chonaic mé thú. Feicfidh tusa an rud sin. Tá an méid sin ite agam."
determiner = {'an', 'na', 'uile'}
prepositions = {'ag', 'ar', 'as', 'chuig', 'chun', 'de', 'do', 'faoi', 'i', 'idir', 'le', 'ó', 'roimh', 'thar', 'trí',
                'um'}
patterns = [
    #persons non-emphatic
    (r'(^(mé)$)', 'PRP'),
    (r'(^(tú)$)', 'PRP'),
    (r'(^(thú)$)', 'PRP'),
    (r'(^(sé)$)', 'PRP'),
    (r'(^(sí)$)', 'PRP'),
    (r'(^(sinn)$)', 'PRP'),
    (r'(^(muid)$)', 'PRP'),
    (r'(^(sibh)$)', 'PRP'),
    (r'(^(siad)$)', 'PRP'),

    # person emphatic
    (r'(^(mise)$)', 'PRPE'),
    (r'(^(tusa)$)', 'PRPE'),
    (r'(^(seisean)$)', 'PRPE'),
    (r'(^(sise)$)', 'PRPE'),
    (r'(^(sinne)$)', 'PRPE'),
    (r'(^(muidne)$)', 'PRPE'),
    (r'(^(sibhse)$)', 'PRPE'),
    (r'(^(siadsan)$)', 'PRPE'),

    # person conjoined
    (r'(?=^(.[h]))(?=.*((as)|(eas))$)', 'PRP Past 1st Conj'),
    (r'(?=^(.[h]))(?=.*((ais)|(eais))$)', 'PRP Past 2nd Conj'),
    (r'(?=^(.[h]))(?=.*((amar)|(eamar))$)', 'PRP Past 1st Plural Conj'),
    (r'(?=^(.[h]))(?=.*((amh)|(eamh))$)', 'PRP Past 2nd Plural Conj'),
    (r'(?=^(.[h]))(?=.*((adar)|(eadar))$)', 'PRP Past 3rd Plural Conj'),
    (r'(?=^(.[h]))(?=.*((adh)|(eadh))$)', 'PRP Past Relative Conj'),

    (r'(.*((aim)|(im))$)', 'PRP Past 1st Conj'),
    (r'(.*((aimid)|(imid))$)', 'PRP Past 1st Conj'),
    (r'(.*((tar)|(tear))$)', 'PRP Past 1st Conj'),

    # verb general forms
    (r'(?=^(.[h]))(?!.*(((aigh)|(igh)))$)', 'PAST 1ST CONJ'),
    (r'(?=^(.[h]))(?=.*(((aigh)|(igh)))$)', 'PAST 2ND CONJ'),
    (r'(.*(((ann)|(eann)))$)', 'PRESENT 1ST CONJ'),
    (r'(.*(((aíonn)|(íonn)))$)', 'PRESENT 2ND CONJ'),
    (r'(.*(((faidh)|(fidh)))$)', 'FUTURE 1ST CONJ'),
    (r'(.*(((oidh)|(eoidh)))$)', 'FUTURE 2ND CONJ'),

    (r'^((an)|(na))$', 'DT'),  # determiner
    (r'.*((adh)|(eadh))$', 'VBG'),  # gerund
    (r'.*((ann)|(eann))$', 'VBZ'),  # gerund
    (r'.*((ta)|(te)|(the)|(tha))$', 'VBN'),  # past participle
    (r'^-?[0-9]+(.[0-9]+)?ú$', 'CD'),  # cardinal numbers
    (r'.*', 'NN')  # default to noun
]

output = []

split_sentence = nltk.word_tokenize(raw_sentence)
def_tagger = nltk.RegexpTagger(patterns)
tagged = def_tagger.tag(split_sentence)

for item in tagged:
    print(item)