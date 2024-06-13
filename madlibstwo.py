
adjective1 = input("Enter an adjective: ")
noun1 = input("Enter a noun: ")
verb_past = input("Enter a verb in past tense: ")
adverb = input("Enter an adverb: ")
adjective2 = input("Enter another adjective: ")
noun2 = input("Enter another noun: ")
noun3 = input("Enter one more noun: ")
verb = input("Enter a verb: ")
adjective3 = input("Enter one last adjective: ")

# Short story with placeholders for the user's words
story = f"""
Today I went to the zoo. I saw a(n) {adjective1} {noun1} jumping up and down in its tree.
 He {verb_past} {adverb} through the large tunnel that led to its {adjective2} {noun2}.
I got some peanuts and passed them through the cage to a gigantic gray {noun3} towering above my head.
Feeding that animal made me hungry. I went to get a {verb} and ate it {adjective3}.
"""

# Print the completed story
print("\nHere is your Mad Libs story:")
print(story)

