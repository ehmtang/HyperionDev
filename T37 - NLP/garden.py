import spacy

# Load English tokenizer, tagger, parser and NER
nlp = spacy.load('en_core_web_sm')

gardenpathSentences = [
    "The old man the boat",
    "The horse raced past the barn fell",
    "The florist sent the flowers was pleased",
    "The sour drink from the ocean",
    "The man who hunts ducks out on weekends",
    "Helen is expecting tomorrow to be a bad day",
    "Do you prefer Microsoft or Macs?",
    "A British man, Irishman and Scotsman walk into a bar...",
    "One cat, a couple of cats, third place"
    ]

# Tokenise garden path sentences using nlp spacy
# append to processed sentences to nlp_gardenpathSentences list
# append tokenised sentence to tokenised_sentences list
tokenised_sentences = []
nlp_gardenpathSentences = []
for idx, sentence in enumerate(gardenpathSentences):

    nlp_sentence = nlp(sentence)
    nlp_gardenpathSentences.append(nlp_sentence)

    token = nlp_sentence.text.split()
    tokenised_sentences.append(token)


# Analyse sentence and find entities 
for idx, nlp_sentence in enumerate(nlp_gardenpathSentences):

    # Analyse syntax
    print("Noun phrases: ", [chunk.text for chunk in nlp_sentence.noun_chunks])
    print("Verbs: ", [token.lemma_ for token in nlp_sentence if token.pos_ == "VERB"])

    # Find named entities, phrases and concepts
    for entity in nlp_sentence.ents:
        print(entity.text, entity.label_, entity.label)
    
    print()

# Get an explanation of an entity and print it
"""
All entities listed from spacy:

['ORG', 'CARDINAL', 'DATE', 'GPE', 'PERSON', 
'MONEY', 'PRODUCT', 'TIME', 'PERCENT', 'WORK_OF_ART', 
'QUANTITY', 'NORP', 'LOC', 'EVENT', 'ORDINAL', 
'FAC', 'LAW', 'LANGUAGE']
"""

entity_org = spacy.explain("ORG")
entity_cardinal = spacy.explain("CARDINAL")
entity_norp = spacy.explain("NORP")
print(f"ORG: {entity_org}")
print(f"CARDINAL: {entity_cardinal}")
print(f"NORP: {entity_norp}")

"""
output:
ORG: Companies, agencies, institutions, etc.
CARDINAL: Numerals that do not fall under another type
NORP: Nationalities or religious or political groups

Sentences used may require reclassification of entities.

Eg the old man the boat failed to classify man as a verb
British was correctly classified as NORP however Irishman and Scotsman that are more ambiguous were classified as ORG and PERSON entities.
"""