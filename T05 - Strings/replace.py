sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog!."
print(sentence)

# Replace ! with whitespace
sentence_replace = sentence.replace("!", " ")

# Remove last whitespace before punctuation
idx = sentence_replace.rfind(" ")
sentence_replace = sentence_replace[0:idx] + sentence_replace[idx+1:]
print(sentence_replace)

"""
Alternatively I can use regular expressions to remove whitespaces before punctuations.

Reference
https://stackoverflow.com/questions/18878936/how-to-strip-whitespace-from-before-but-not-after-punctuation-in-python
"""

# Capitalise the string
sentence_upper = sentence_replace.upper()
print(sentence_upper)

# Reverse the string
sentence_reverse = sentence_replace[::-1]
print(sentence_reverse)