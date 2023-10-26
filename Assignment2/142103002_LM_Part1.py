import nltk
from nltk.corpus import brown
from collections import defaultdict

nltk.download('brown')  # Download the Brown corpus

words = brown.words()  # Get a list of words from the Brown corpus

def generate_ngrams(words, n):
    ngrams = []
    for i in range(len(words) - n + 1):
        ngram = tuple(words[i:i + n])  # Generate n-grams by grouping words in tuples
        ngrams.append(ngram)
    return ngrams

ngram_counts = {}  # Initialize a dictionary to store n-gram counts
n_values = [2, 3, 4, 5]  # Define the n-gram values to compute

for n in n_values:
    ngram_counts[n] = defaultdict(int)  # Initialize a dictionary with default integer values for each n-gram

for n in n_values:
    ngrams = generate_ngrams(words, n)  # Generate n-grams for each n value
    for ngram in ngrams:
        ngram_counts[n][ngram] += 1  # Count the occurrences of each n-gram

for n in n_values:
    with open(f'MIS-142103002_{n}-gram-output.txt', 'w') as output_file:
        for ngram, count in ngram_counts[n].items():
            ngram_str = ' '.join(ngram)  # Convert the n-gram tuple to a string
            output_file.write(f"{ngram_str} {count}\n")  # Write the n-gram and its count to an output file

print("Done")  # Print "Done" to indicate the completion of the code
