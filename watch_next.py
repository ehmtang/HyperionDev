import spacy

# Load medium model from spacy
nlp = spacy.load('en_core_web_md')

# Create list of movies from text file
with open("./movies.txt", 'r') as f:
    movie_list = f.read().splitlines()

# Planet Hulk description
planet_hulk_descr = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."

# Empty list to append similarity results
ranking = []

# Prompt user if they have seen 'Planet Hulk'
# if yes, execute similarity model for each movie contained in list.
# return the highest similarity movie to user.
# else do nothing
def watch_next():
    recommendation = input("Have you watched 'Planet Hulk', yes or no? ")

    if recommendation.lower() == 'yes':
        
        # Utilising nlp function on planet hulk description
        model_sentence = nlp(planet_hulk_descr)

        print("We recommend the following movie:\n")

        # Compare each movie in list to planet hulk        
        for movie in movie_list:
            similarity = nlp(movie).similarity(model_sentence)
            ranking.append(similarity)
        
        # Get index of max ranking similarity
        idx_max_ranking = ranking.index(max(ranking))

        return print(movie_list[idx_max_ranking])
        
    else:
        print('Never mind.')

watch_next()
