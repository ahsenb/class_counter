import os

def count_words_in_text_files(directory, words):
    word_counts = {word: 0 for word in words}
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            with open(os.path.join(directory, filename), "r") as file:
                for line in file:
                    first_column = line.split(" ")[0]
                    for word in words:
                        if first_column == word:
                            word_counts[word] += 1
    return word_counts

directory = "/path/to/directory"
words = ["0", "1", "2", "3", "4"]
word_counts = count_words_in_text_files(directory, words)
for word, count in word_counts.items():
    print(f"{word}: {count}")