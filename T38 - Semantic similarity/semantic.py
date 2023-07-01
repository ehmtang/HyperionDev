import spacy
nlp = spacy.load('en_core_web_md')

tokens = nlp('cat monkey banana book')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, '%.4f' % token1.similarity(token2))


"""
cat cat 1.0000
cat monkey 0.3945
cat banana 0.2334
cat book 0.0693
monkey cat 0.3945
monkey monkey 1.0000
monkey banana 0.3741
monkey book 0.0745
banana cat 0.2334
banana monkey 0.3741
banana banana 1.0000
banana book 0.0347
book cat 0.0693
book monkey 0.0745
book banana 0.0347
book book 1.0000

Constructed a comparison of the 4 words.
- Items have 1.000 ranking with itself
- Items that have low ranking have little in common. example apple cat. both objects but share no other common feature
- Ranking increases with items that have more in common. example banana apple, both objects are fruit. monkey cat are both animals.
- note symmetry, output is similar to a correlation matrix
"""

sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
             "Hello, there is my car",
             "I\'ve lost my car in my car",
             "I\'d like my boat ",
             "I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

"""
where did my dog go -  0.8375595303084714
Hello, there is my car -  0.8612759137404267
I've lost my car in my car -  0.8797555739317211
I'd like my boat  -  0.7397250711402195
I will name my dog Diana -  0.7840655785769225

Cosine similarity scores highly when words used are contained in the sentence_to_compare.
"""

"""
Differences between 'en_core_web_sm' and 'en_core_web_md'
Reduced accuracy values from 'sm' model vs 'md' model.

Documentation notes the 'md' and 'lg' models include pre-trained vectors (features).
the 'sm' model does not include trained word vectors. 

In the example, the language used for complaints and baking have closely aligned word vectors in their respective groups.
Therefore accuracy/similarity scores higher using the 'md' model.
"""