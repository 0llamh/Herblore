#       Herb.py
#       Herb class

import random

class Herb:

    def __init__(self):

        self.color = self.getColor()
        self.type = self.getType()
        self.name = self.getName(self.color, self.type)
        self.origin = self.getOrigin(self.name)
        self.rarity = self.getRarity()
        self.use = self.getUse()
        self.preparation = self.getPrep(self.type)
        self.expiration = self.getExpiration()
        self.delivery = self.getDelivery(self.preparation)

    def getColor(self):
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

    def getType(self):
        herbs = ["Bark", "Berry", "Blossom", "Bulb", "Flower", "Fruit", "Frond", "Grass", "Leaf", "Lily",
                 "Lotus", "Moss", "Mushroom", "Needle", "Nut", "Pollen", "Petal", "Root", "Rose", "Sap", "Seed",
                 "Stalk", "Stem", "Thorn", "Tulip", "Vine", "Weed"]
        herbs_rand = random.randint(0, 25)
        h_type = herbs[herbs_rand]
        return h_type

    def getName(self, c, t):
        h_name = ''
        r1 = random.randint(0, 2)
        add_noun_descriptor = random.randint(0, 1)

        # Generate Adjective
        adjectives = ['Arctic', 'Bright', 'Burning', 'Dark', 'Dancing', 'Dusty', 'Earth', 'Elder', 'Frozen', 'Great',
                      'Hard', 'Soft', 'Stinging']
        adj_rand = random.randint(0, 12)
        if r1 == 0:             # add color
            # todo: filter out generic color if taken in (e.g., Dark Greenish Blue == Blue)
            color_words = c.split()     # creates tuples of all words in string
            c = color_words[-1]         # saves last tuple value into c
            h_name += c + " "           # Randomly adds in color
        elif r1 == 1:           # add adjectives
            h_name += adjectives[adj_rand] + " "        # Appends adjective to full name string
        else:           # add color and adjectives
            color_words = c.split()                     # creates tuples of all words in string
            c = color_words[-1]                         # saves last tuple value into c
            h_name += c + " "                           # Randomly adds in color
            h_name += adjectives[adj_rand] + " "        # Appends adjective to full name string

        # Generate descriptive noun -- SEPARATE FROM HERB TYPE from getType()
        nouns = ['Cliff', 'Dawn', 'Dusk', 'Fire', 'Grave', 'Ice', 'Moon', 'Morning', 'Mountain', 'Muck', 'Mud',
                 'Night', 'Rain', 'Rock', 'Sand', 'Song', 'Shadow', 'Sun', 'Swamp', 'Water', 'Wind']
        if add_noun_descriptor == 1:
            while True:
                noun_rand = random.randint(0, 20)
                if nouns[noun_rand] != t:
                    break
            h_name += nouns[noun_rand] + t.lower()
        else:
            h_name += t

        return h_name

    def getOrigin(self, n):
        h_origin = ''
        origins = ['Ice and Snow', 'Forestation', 'Marshes and Swamps', 'Grass', 'Lakes and Rivers', 'Underground',
                   'Bushes and Shrubs', 'Desert', 'Mountains and Cliffs']
        # todo: filter out terrains based on type and adjectives
        # Run a loop to ensure name corroborates its origin
        while h_origin == '':
            roll_origin = random.randint(0, 8)
            if ('Arctic' in n) or ('Frozen' in n) or ('Ice' in n):
                h_origin = 'Ice and Snow'
            elif ('Bark' in n) or ('Sap' in n):
                h_origin = 'Forestation'
            elif ('Muck' in n) or ('Mud' in n) or ('Swamp' in n):
                h_origin = 'Marshes and Swamps'
            elif ('Mountain' in n) or ('Cliff' in n):
                h_origin = 'Mountains and Cliffs'
            elif ('Rain' in n) and (roll_origin == 5 or roll_origin == 7):
                continue        # rain doesn't occur underground or desert
            else:
                h_origin = origins[roll_origin]
        return h_origin

    def getRarity(self):
        rarity = 10     # base Dice check value on herbalism rolls
        dc = random.randint(0, 20)      # random additive to a max of 30 on a DC
        rarity += dc       # appends random value

        return rarity

    def getPrep(self, type):
        h_preparation = ''
        preps = ['Raw', 'Vigorously mixing', 'Boiling slowly', 'Boiling rapidly', 'Roasting', 'Smoking', 'Sun-drying',
                 'Soaking', 'Brining', 'Brewing', 'Steeping', 'Crushing', 'Crystallizing']
        r_preps = random.randint(0, 12)
        # todo how it alchemically prepared (should align with herb type and use)

        h_preparation += preps[r_preps]

        return h_preparation


    def getDelivery(self, prep):
        h_deliv = ''
        # todo delivery
        deliveries = ['Thick paste', 'Thin paste', 'Rough powder', 'Fine powder', 'Oily liquid',
                      'Gloopy liquid', 'Balm', 'Lotion', 'Course crystals']
        if prep == 'Raw':
            h_deliv = 'Raw'
            # todo: specific raw deliveries based on herb.type
        elif prep == 'Brewing':
            h_deliv = 'Fermented liquid'
        elif prep == 'Steeping':
            h_deliv = 'Tea'
        elif prep == 'Crystallizing':
            h_deliv = 'Course crystals'
        else:
            r_deliv = random.randint(0, 8)
            h_deliv = deliveries[r_deliv]

        return h_deliv

    def getExpiration(self):
        h_expiration = ""
        expirations = ['Immediately', 'Hours', 'Days', 'A year', 'No expiration']
        rand_expire = random.randint(0, 4)
        if rand_expire == 4:
            h_expiration = 'No expiration'
        else:
            h_expiration += expirations[rand_expire]
        return h_expiration

    def getUse(self):
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
            h_use += " commonly used as a " + drugs[r_drug]
        return h_use
