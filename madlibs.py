# Mad Libs Game with Numbers: A Day at the Zoo

# Step 1: Prompt the User for Words and Numbers
# Ask the player for different types of words and numbers to fill in the story.

adjective1 = input("Please enter an adjective: ")

noun1 = input("Please enter a noun: ")

verb_past_tense1 = input("Please enter a verb in past tense: ")

adverb1 = input("Please enter an adverb: ")

adjective2 = input("Please enter another adjective: ")

noun2 = input("Please enter another noun: ")

noun3 = input("Please enter one more noun: ")

number_of_animals = input("Please enter a number: ")  # New numeric input

age_of_animal = input("Please a number: ")  # New numeric input

adjective3 = input("Please enter a third adjective: ")

number_of_scoops = input("Please enter a number: ")  # New numeric input

verb1 = input("Please enter a verb: ")

adverb2 = input("Please enter another adverb: ")

verb_past_tense2 = input("Please enter another verb in past tense: ")

adjective4 = input("Please enter a fourth adjective: ")

# Step 2 & 3: Create a Story Template and Insert the Words and Numbers
# Combine the inputs with the story template to create a unique story
# story variable bvdfhjajh 

story = f"""
Today I went to the zoo. I saw a {adjective1} {noun1} jumping up and down in its tree.
He {verb_past_tense1} {adverb1} through the large tunnel that led to its {adjective2} {noun2}.
I got some peanuts and passed them through the cage to a gigantic gray {noun3} towering above my head.
According to the zookeeper, there were {number_of_animals} animals like this one, and the oldest was {age_of_animal} years old.
Feeding that animal made me hungry. I went to get a {adjective3} scoop of ice cream. Actually, make that {number_of_scoops} scoops! It filled my stomach.
Afterwards, I had to {verb1} {adverb2} to catch our bus. When I got home, I {verb_past_tense2} my mom for a {adjective4} day at the zoo.
"""

# Step 4: Display the Story
# Show the completed story to the player, filled with their words.
print(story) #print story
