import nltk
from collections import defaultdict

# Define a function to load N-gram models from a file
def load_ngram_models():
    ngram_models = {}
    n_values = [2, 3, 4, 5]

    for n in n_values:
        ngram_models[n] = defaultdict(int)
        with open(f"MIS-142103002_{n}-gram-output.txt", 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split()
                ngram = tuple(parts[:-1])
                count = int(parts[-1])
                ngram_models[n][ngram] += count

    return ngram_models

# Define a function to predict the next word using N-gram models
def predict_next_word(input_words, ngram_models, n):
    input_ngram = tuple(input_words[-(n - 1):])
    possible_next_words = []

    for ngram, count in ngram_models[n].items():
        if ngram[:-1] == input_ngram:
            possible_next_words.append((ngram[-1], count))

    if not possible_next_words:
        return "No prediction available."

    predicted_word = max(possible_next_words, key=lambda x: x[1])[0]
    return predicted_word

def main():
    ngram_models = load_ngram_models()

    while True:
        input_text = input("Enter a set of words (or type 'exit' to quit): ").strip().split()

        if input_text[0].lower() == 'exit':
            break

        n = int(input("Enter the value of 'n' for N-gram model (e.g., 2 for bigram, 3 for trigram): "))
        if n not in ngram_models:
            print("Invalid 'n' value. Please choose from 2, 3, 4, or 5.")
            continue

        next_word = predict_next_word(input_text, ngram_models, n)

        print("Predicted Next Word:", next_word)

if __name__ == "__main__":
    main()
