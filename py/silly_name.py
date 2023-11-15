"""
Randomly Combines the Firstname and the Lastname to generate a nutty name
"""

import random

# name = "Radiance Babajide"

class SillyName:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.last_generated = ""

    def generate(self):
        all_chars = []
        # No of characters from the firstname and lastname
        no_of_chars_firstname = random.randint(1,4)
        no_of_chars_lastname = random.randint(1,4)

        all_chars += random.choices(self.firstname, k=no_of_chars_firstname)
        all_chars += random.choices(self.lastname, k=no_of_chars_lastname)

        # random.shuffle(all_chars)
        self.last_generated = "".join(all_chars)
        return self.last_generated
    

s = SillyName("Radiance", "Babajide")
print(s.generate())