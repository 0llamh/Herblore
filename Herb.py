#       Herb.py
#       Herb class

import random

class Herb:

    def __init__(self):

        self.color = self.getColor()
        self.name = self.getName(self.color)
        self.origin = self.getOrigin(self.name)
        self.rarity = self.getRarity()
        self.texture = self.getTexture(self.name)
        self.use = self.getUse()
        self.expiration = self.getExpiration()
        self.delivery = self.getDelivery()

    def getName(self, c):
        fname = ""
        r1 = random.randint(1, 2)
        r2 = random.randint(1, 2)

        # Generate Adjective
        adjectives = "Arctic", "Burning", "Dawn", "Dusk", "Earth", "Elder", "Frozen", "Great", "Grave", "Ice", "Moon", "Morning", "Mountain", "Muck", "Night", "Rain", "Shadow", "Sun", "Swamp", "Water", "Wind"
        adj_rand = random.randint(0, 20)       # 21
        if r1 == 2:
            # todo: filter out generic color if taken in (e.g., Dark Greenish Blue == Blue)
            color_words = c.split()     # creates tuples of all words in string
            c = color_words[-1]     # saves last tuple value into c
            fname += c + " "      # Randomly adds in color
        fname += adjectives[adj_rand] + " "       # Appends adjective to full name string

        # Generate Noun
        nouns = "Bark", "Berry", "Blossom", "Bulb", "Flower", "Fruit", "Leaf", "Lily", "Moss", "Needle", "Nut", "Pollen", "Petal", "Root", "Rose", "Sap", "Seed", "Stalk", "Stem", "Thorn", "Vine", "Weed"
        noun_rand = random.randint(0, 21)   # 22
        # todo: separate strict base herb types ( Bark, berry, nut ) to be usable only as suffixes or solo. Possibly create new function to generate/save.
        if r2 == 2:
            while True:
                noun_rand2 = random.randint(0, 20)   # 21
                if noun_rand != noun_rand2:
                    break
            fname += nouns[noun_rand] + nouns[noun_rand2].lower()
        else:
            fname += nouns[noun_rand]

        return fname

    def getColor(self):
        fColor = ""
        colors = "Black", "Blue", "Brown", "Copper", "Gold", "Green", "Grey", "Pink", "Purple", "Orange", "Red", "Silver", "White", "Yellow"
        color_primary = random.randint(0, 13)   # 14
        color_descriptor = random.randint(1, 3)

        if color_descriptor == 1:
            # Light
            pale_or_light = random.randint(1, 2)
            if pale_or_light == 1:
                fColor = "Pale " + colors[color_primary]
            else:
                fColor = "Light " + colors[color_primary]
        elif color_descriptor == 2:
            # Dark
            fColor = "Dark " + colors[color_primary]
        else:
            fColor = colors[color_primary]
            # todo: more descriptive primaries based on individual rolls: turquoise, magenta, garnet, teal, etc.
        return fColor

    def getOrigin(self, n):
        fOrigin = ""
        origins = "Tundra", "Desert", "Jungle or Swamp", "Forestation", "Mountains", "Grasslands", "Underground", "Fresh Water", "Salt Water"

        # todo: polish up fresh water and salt water filtering
        # Run a loop to ensure name corroborates its origin
        if ("Arctic" in n) or ("Ice" in n) or ("Frozen" in n):
            fOrigin = "Tundra"
        elif ("Swamp" in n) or ("Muck" in n):
            fOrigin = "Jungle or Swamp"
        elif "Mountain" in n:
            fOrigin = "Mountains"
        elif ("Bark" in n) or ("Sap" in n) or ("Moss" in n) or ("Vine" in n):
            while True:
                origin_rand = random.randint(0, 8)
                fOrigin = origins[origin_rand]
                if fOrigin == "Forestation" or fOrigin == "Jungle/Swamp":
                    break
        else:
            while True:
                origin_rand = random.randint(0, 8)
                fOrigin = origins[origin_rand]
                if ("Water" in fOrigin) and (("Bark" in n) or ("Sap" in n) or ("Pollen" in n)):
                    continue
                else:
                    break

        return fOrigin

    def getRarity(self):
        rarity = 10     # base Dice check value on herbalism rolls
        dc = random.randint(0, 20)      # random additive to a max of 30 on a DC
        rarity += dc       # appends random value

        return rarity

    def getTexture(self, n):
        hTexture = ""
        # todo texture

        return hTexture

    def getUse(self):
        hUse = ""
        # todo use

        return hUse

    def getExpiration(self):
        hExpire = ""
        # todo expiration

        return hExpire

    def getDelivery(self):
        hDeliv = ""
        # todo delivery

        return hDeliv