#       Herb.py
#       Herb class

import random

class Herb:

    def __init__(self):

        self.color = self.getColor()
        self.name = self.getName(self.color)
        self.origin = self.getOrigin(self.name)
        self.rarity = self.getRarity()
        self.use = self.getUse()
        self.preparation = self.getPrep(self.name, self.use)
        self.expiration = self.getExpiration()
        self.delivery = self.getDelivery()

    def getName(self, c):
        h_name = ""
        r1 = random.randint(1, 2)
        r2 = random.randint(1, 2)

        # Generate Adjective
        adjectives = "Arctic", "Burning", "Dawn", "Dusk", "Earth", "Elder", "Frozen", "Great", "Grave", "Ice", "Moon", "Morning", "Mountain", "Muck", "Night", "Rain", "Shadow", "Sun", "Swamp", "Water", "Wind"
        adj_rand = random.randint(0, 20)       # 21
        if r1 == 2:
            # todo: filter out generic color if taken in (e.g., Dark Greenish Blue == Blue)
            color_words = c.split()     # creates tuples of all words in string
            c = color_words[-1]     # saves last tuple value into c
            h_name += c + " "      # Randomly adds in color
        h_name += adjectives[adj_rand] + " "       # Appends adjective to full name string

        # Generate Noun
        nouns = "Bark", "Berry", "Blossom", "Bulb", "Flower", "Fruit", "Leaf", "Lily", "Moss", "Needle", "Nut", "Pollen", "Petal", "Root", "Rose", "Sap", "Seed", "Stalk", "Stem", "Thorn", "Vine", "Weed"
        noun_rand = random.randint(0, 21)   # 22
        # todo: separate strict base herb types ( Bark, berry, nut ) to be usable only as suffixes or solo. Possibly create new function to generate/save.
        if r2 == 2:
            while True:
                noun_rand2 = random.randint(0, 20)   # 21
                if noun_rand != noun_rand2:
                    break
            h_name += nouns[noun_rand] + nouns[noun_rand2].lower()
        else:
            h_name += nouns[noun_rand]

        return h_name

    def getColor(self):
        h_color = ""
        colors = "Black", "Blue", "Brown", "Copper", "Gold", "Green", "Grey", "Pink", "Purple", "Orange", "Red", "Silver", "White", "Yellow"
        color_primary = random.randint(0, 13)   # 14
        color_descriptor = random.randint(1, 3)

        if color_descriptor == 1:
            # Light
            pale_or_light = random.randint(1, 2)
            if pale_or_light == 1:
                h_color = "Pale " + colors[color_primary]
            else:
                h_color = "Light " + colors[color_primary]
        elif color_descriptor == 2:
            # Dark
            h_color = "Dark " + colors[color_primary]
        else:
            h_color = colors[color_primary]
            # todo: more descriptive primaries based on individual rolls: turquoise, magenta, garnet, teal, etc.
        return h_color

    def getOrigin(self, n):
        h_origin = ""
        origins = "Tundra", "Desert", "Jungle or Swamp", "Forestation", "Mountains", "Grasslands", "Underground", "Fresh Water", "Salt Water"

        # todo: polish up fresh water and salt water filtering
        # Run a loop to ensure name corroborates its origin
        if ("Arctic" in n) or ("Ice" in n) or ("Frozen" in n):
            h_origin = "Tundra"
        elif ("Swamp" in n) or ("Muck" in n):
            h_origin = "Jungle or Swamp"
        elif "Mountain" in n:
            h_origin = "Mountains"
        elif ("Bark" in n) or ("Sap" in n) or ("Moss" in n) or ("Vine" in n):
            while True:
                origin_rand = random.randint(0, 8)
                h_origin = origins[origin_rand]
                if h_origin == "Forestation" or h_origin == "Jungle/Swamp":
                    break
        else:
            while True:
                origin_rand = random.randint(0, 8)
                h_origin = origins[origin_rand]
                if ("Water" in h_origin) and (("Bark" in n) or ("Sap" in n) or ("Pollen" in n)):
                    continue
                else:
                    break

        return h_origin

    def getRarity(self):
        rarity = 10     # base Dice check value on herbalism rolls
        dc = random.randint(0, 20)      # random additive to a max of 30 on a DC
        rarity += dc       # appends random value

        return rarity

    def getPrep(self, name, use):
        h_preparation = "in some way"
        # todo how it alchemically prepared (should align with herb type and use)
        preps = ['a thick paste', 'a thin paste', 'a rough powder', 'a fine powder', 'an oily liquid',
                 'a thick, gloopy liquid', '']
        return h_preparation

    def getUse(self):
        h_use = "use and effect"
        # todo more uses and effects
        r_use = random.randint(0, 2)    # get use
        use = ['an ailment', 'a poison', 'a drug']
        h_use = use[r_use]
        if h_use == 'an ailment':
            r_potion = random.randint(0, 9)
            potions = ['to stop bleeding', 'to relieve pain', 'to sterilize a wound or object', 'to lower a fever',
                       'as a respiratory adrenal agent', 'to soothe rashes and hives', 'as a decongestant',
                       'as a burn agent', 'as an antivenom', 'as a anti-paralytic']
            h_use += " " + potions[r_potion]
        elif h_use == 'a poison':
            r_poison = random.randint(0, 17)
            poisons = ['blood thinning', 'headaches', 'body aches', 'an infection', 'fevers and chills',
                       'respiratory inflammation', 'blurry vision or blindness', 'painful rashes and hives',
                       'impaired motor function or paralyzing agent', 'amnesia', 'drowsiness', 'paranoia', 'insomnia',
                       'impotence', 'infertility', 'laxadation', 'vomiting', 'muscle death']
            h_use += " that causes " + poisons[r_poison]
        elif h_use == 'a drug':
            r_drug = random.randint(0, 3)
            drugs   = ['euphoriant', 'sensory stimulant', 'steroid', 'hallucinogen']
            h_use += " commonly as a " + drugs[r_drug]
        return h_use

    def getExpiration(self):
        h_expiration = "best if used "
        expirations = ['immediately', 'within hours', 'within days', 'within a year', 'no expiration']
        rand_expire = random.randint(0, 4)
        if rand_expire == 4:
            h_expiration = 'with no expiration'
        else:
            h_expiration += expirations[rand_expire]
        return h_expiration

    def getDelivery(self):
        h_deliv = ""
        # todo delivery

        return h_deliv