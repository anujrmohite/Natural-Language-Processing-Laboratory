import nltk
from collections import defaultdict

def load_ngram_models():
    ngram_models = {}  # Initialize a dictionary to store n-gram models
    n_values = [2, 3, 4, 5]  # Define the n-gram values to load

    for n in n_values:
        ngram_models[n] = defaultdict(int)  # Initialize a dictionary with default integer values for each n-gram
        with open(f"MIS-142103002_{n}-gram-output.txt", 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split()
                ngram = tuple(parts[:-1])  # Extract the n-gram as a tuple
                count = int(parts[-1])  # Extract the count of the n-gram
                ngram_models[n][ngram] += count  # Store the n-gram and its count in the model

    return ngram_models  # Return the loaded n-gram models

def predict_next_word(input_words, ngram_models, n):
    input_ngram = tuple(input_words[-(n - 1):])  # Extract the n-1 words from the input
    possible_next_words = []  # Initialize a list to store possible next words

    for ngram, count in ngram_models[n].items():
        if ngram[:-1] == input_ngram:  # Check if the n-1 words in the n-gram match the input
            possible_next_words.append((ngram[-1], count))  # Add the last word and its count

    if not possible_next_words:
        return "No prediction available."

    # Select the word with the highest count as the predicted next word
    predicted_word = max(possible_next_words, key=lambda x: x[1])[0]
    return predicted_word

def main():
    ngram_models = load_ngram_models()  # Load n-gram models from files

    while True:
        input_text = input("Enter a set of words (or type 'exit' to quit): ").strip().split()

        if input_text[0].lower() == 'exit':
            break

        n = int(input("Value of for N-gram model:"))  # Get the n value for the n-gram model
        if n not in ngram_models:
            print("Invalid 'n' value. Please choose from 2, 3, 4, or 5.")
            continue

        next_word = predict_next_word(input_text, ngram_models, n)  # Predict the next word

        with open("MIS-142103002_Part2-Output.txt", "a") as output_file:
            output_file.write(f"Input: {' '.join(input_text)}\n")
            output_file.write(f"Next Word: {next_word}\n\n")  # Write input and prediction to an output file

if __name__ == "__main__":
    main()  # Run the main function if this script is executed
