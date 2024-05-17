def word_counter(sentence):
    words = sentence.split()
    word_counts = {}

    for word in words:
        word = word.lower().strip(",.!?")  # Normalize words
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts

sentence = input("Enter a sentence: ")
word_counts = word_counter(sentence)
for word, count in word_counts.items():
    print(f"{word}: {count}")
