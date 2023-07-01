class Cow(object):

    _noise = 'moo!'
    
    def __init__(self, colour):
        self.colour = colour

    def make_noise(self):
        print(self._noise)

    def set_colour(self, new_colour):
        self.colour = new_colour

    def get_colour(self):
        return self.colour

    def __eq__(self, other):
        if self.colour == other.colour:
            return True
        else:
            return False

    def __str__(self):
        return self.colour + ' ' + self._noise

# Create objects
cow_1 = Cow('blue')
cow_2 = Cow('red')

# Call the make noise method
cow_1.make_noise()

# Compare cows
print("Cows are the same:", cow_1 == cow_2)

# Change the colour of a cow
cow_1.set_colour('red')

# Compare the two cows again
print("Cows are the same:", cow_1 == cow_2)