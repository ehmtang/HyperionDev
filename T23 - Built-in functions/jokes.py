import random

"""
More efficient to use dictionary for the lookup of elements. But task asks for a list
"""
# Storing dad jokes in a dictionary
# jokes = {
#     1 : "I'm afraid for the calendar. Its days are numbered.",
#     2 : "My wife said I should do lunges to stay in shape. That would be a big step forward.",
#     3 : "Why do fathers take an extra pair of socks when they go golfing?" "In case they get a hole in one!",
#     4 : "Singing in the shower is fun until you get soap in your mouth. Then it's a soap opera.",
#     5 : "What do a tick and the Eiffel Tower have in common?" "They're both Paris sites.",
#     6 : "What do you call a fish wearing a bowtie?" "Sofishticated.",
#     7 : "How do you follow Will Smith in the snow?" "You follow the fresh prints.",
#     8 : "If April showers bring May flowers, what do May flowers bring?" "Pilgrims.",
#     9 : "I thought the dryer was shrinking my clothes. Turns out it was the refrigerator all along.",
#     }

# Storing dad jokes in a list
jokes = [
    "I'm afraid for the calendar. Its days are numbered.",
    "My wife said I should do lunges to stay in shape. That would be a big step forward.",
    "Why do fathers take an extra pair of socks when they go golfing?" "In case they get a hole in one!",
    "Singing in the shower is fun until you get soap in your mouth. Then it's a soap opera.",
    "What do a tick and the Eiffel Tower have in common?" "They're both Paris sites.",
    "What do you call a fish wearing a bowtie?" "Sofishticated.",
    "How do you follow Will Smith in the snow?" "You follow the fresh prints.",
    "If April showers bring May flowers, what do May flowers bring?" "Pilgrims.",
    "I thought the dryer was shrinking my clothes. Turns out it was the refrigerator all along."
    ]

# Print dad joke at random from 1 to 9
print(jokes[random.randint(1, 9)])