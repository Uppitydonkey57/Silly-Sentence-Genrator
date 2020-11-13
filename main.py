import random


def RandomList(selected_list):
    return selected_list[random.randint(0, len(selected_list) - 1)]


nouns = ["pizza", "tin can", "shark", "headphone", "light", "video game", "cousin", "waffle", "monster", "ukulele",
         "salami", "pig ear", "ear wig", "skeleton", "mustache", "criminal", "meatball", "finger nail", "nose hair",
         "banjo", "rodent", "gama ray", "suit case", "jacket", "decapitated head", "flugal horn", "painting",
         "tea biscuit", "toilet bowl", "jelly fish", "flower", "banana", "ant farm", "lightning", "tv remote",
         "knee", "yarn", "vacuum"]

verbs = ["run", "eat", "sleep", "fight", "jump", "race", "cook", "sing", "dance", "cry", "surrender", "challenge",
         "cavort", "kick", "pace", "drive", "triangulate", "launch", "croak", "scratch", "pick", "think", "draw",
         "build", "dream", "read", "scream", "swim"]

noun_places = ["the USA", "France", "Canada", "Florida", "Texas", "Italy", "Germany", "Alaska", "Sweden",
               "the good old days", f"a place where {RandomList(nouns)}s could {RandomList(verbs)}", "Mars",
               "Colonial Williamsburg", "Dubai", "Hell", "the Crack of Doom", "Mount Saint Helens", "Mordor", "the Moon",
               "Illinois"]

noun_people = ["Sherlock", "George Lucas", "Steven Spielberg", "Mario", "Waluigi", "Luigi", "George Washington",
               f"the person in charge of {RandomList(noun_places)}", "Jason", "Papa John", "Chuck e Cheese",
               "Vlad the Impaler", "Dracula", "Harry Houdini", "Baby Jesus", "Genghis Kahn", "Buddha", "Moses",
               "the Pharaoh", "Ivan the Terrible", "Blackbeard", "Gordon Ramsay", "Brian Malarkey", "Guy Fieri",
               "Julius Caesar", "Achilles", "Zeus", "Bob Ross", "the Devil", "Neil deGrasse Tyson"]

adjectives = ["bored", "thinking", "smelly", "tired", "lazy", "happy", "excited", "ungrateful", "stupid", "hairy",
              "cheesy", "itchy", "flavorful", "childish", "balding", "bold", "daring", "evil", "malicious",
              "questionable", "furry", "insane", "quizzical", "fascinating", "tasteless", "fantastic", "bashful",
              "unexcited"]

sentence_beginnings = ["Once upon a time", "in the beginning",
                       f"I remember when",
                       f"{random.randint(1, 1000000)} years ago", "when I was your age",
                       f"Before {RandomList(nouns)} was invented",
                       f"Before {RandomList(adjectives)} {RandomList(nouns)}s could {RandomList(verbs)}",
                       f"Back in {RandomList(noun_places)}",
                       f"Before I could {RandomList(verbs)}",
                       f"After I met {RandomList(noun_people)}",
                       f"This morning",
                       f"After I left {RandomList(noun_places)}",
                       f"If you really want to {RandomList(verbs)}",
                       f"Despite what {RandomList(noun_people)} said"]

sentence_ends = [f"a {RandomList(adjectives)} {RandomList(nouns)} was {RandomList(verbs)}ing.",
                 f"I {RandomList(verbs)} all the time, almost constantly!",
                 f"my {RandomList(adjectives)} {RandomList(nouns)}s favorite thing to do was {RandomList(verbs)}ing.",
                 f"a {RandomList(adjectives)} {RandomList(nouns)} was {RandomList(adjectives)}.",
                 f"I met {RandomList(noun_people)}.",
                 f"everyone in {RandomList(noun_places)} was {RandomList(verbs)}ing.",
                 f"{RandomList(noun_people)} was {RandomList(adjectives)}.",
                 f"{RandomList(noun_people)} was the talk of {RandomList(noun_places)}.",
                 f"my favorite place is {RandomList(noun_places)}.",
                 f"I could {RandomList(verbs)} in {RandomList(noun_places)}.",
                 f"I {RandomList(verbs)} with {RandomList(noun_people)}.",
                 f"{RandomList(verbs)}ing reminded me of {RandomList(nouns)}.",
                 f"{RandomList(nouns)}s reminded me of {RandomList(noun_people)}."]

print(RandomList(sentence_beginnings),
      RandomList(sentence_ends))
