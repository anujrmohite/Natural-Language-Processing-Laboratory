import nltk
from nltk.corpus import brown
from collections import defaultdict, Counter
import random

# Load the Brown Corpus and tokenize it into sentences
nltk.download('brown')
sentences = brown.sents()

# Define a function to generate N-grams from a list of words
def generate_ngrams(sentence, n):
    ngrams = []
    for i in range(len(sentence) - n + 1):
        ngram = tuple(sentence[i:i + n])
        ngrams.append(ngram)
    return ngrams

# Create dictionaries to store the counts of N-grams for different N values
ngram_counts = {}

# Prompt the user for the value of "n"
n = int(input("Enter the value of 'n' for N-grams (e.g., 2 for bigram, 3 for trigram): "))

if n < 2:
    print("Invalid value of 'n'. Please choose a value of 2 or greater.")
    exit()

ngram_counts[n] = defaultdict(int)

# Iterate through the sentences, tokenize them into words, and update the N-gram counts
for sentence in sentences:
    ngrams = generate_ngrams(sentence, n)
    for ngram in ngrams:
        ngram_counts[n][ngram] += 1

# Write the N-gram models to output files as specified in the problem statement
with open(f'MIS-142103002_{n}-gram-output.txt', 'w') as output_file:
    for ngram, count in ngram_counts[n].items():
        ngram_str = ' '.join(ngram)
        output_file.write(f"{ngram_str} {count}\n")

# Part 2: Predicting the Next Word

# Load the N-gram model
def load_ngram_model(n):
    ngram_model = defaultdict(Counter)
    with open(f'MIS-142103002_{n}-gram-output.txt', 'r') as input_file:
        for line in input_file:
            parts = line.strip().split()
            if len(parts) >= 2:
                ngram = tuple(parts[:-1])
                count = int(parts[-1])
                ngram_model[ngram[:-1]][ngram[-1]] += count
    return ngram_model

# Define a function to predict the next word using the N-gram model
def predict_next_word(ngram_model, input_words):
    context = tuple(input_words[-(n - 1):])

    if context not in ngram_model:
        return "No prediction available"

    next_word_counts = ngram_model[context]
    total_count = sum(next_word_counts.values())

    # Choose the next word based on probabilities
    rand_val = random.uniform(0, total_count)
    cumulative_prob = 0.0

    for word, count in next_word_counts.items():
        word_prob = count / total_count
        cumulative_prob += word_prob
        if cumulative_prob >= rand_val:
            return word

# Example usage:
input_words = ["This", "is", "a"]
ngram_model = load_ngram_model(n)
next_word = predict_next_word(ngram_model, input_words)
print(f"Predicted next word: {next_word}")
