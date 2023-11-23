import nltk
from nltk.corpus import wordnet
from nltk.wsd import lesk
from nltk import word_tokenize

# Download WordNet - a lexical database of the English language
nltk.download("wordnet")


def disambiguate_word(context, ambiguous_word):
    # Tokenizing the context into a list of words
    context_tokens = word_tokenize(context)

    # Lesk algorithm to disambiguate the meaning of the ambiguous word
    sense = lesk(context_tokens, ambiguous_word)

    # Check if a sense was determined
    if sense:
        # Get the definition of the determined sense
        definition = sense.definition()
        return f"The appropriate sense of '{ambiguous_word}' in the context is: {definition}"
    else:
        # If no sense is found, indicate that no appropriate sense was found
        return (
            f"No appropriate sense found for '{ambiguous_word}' in the given context."
        )


# Example context and ambiguous word
context = "I went to the bank to deposit some money."
ambiguous_word = "bank"

# Apply the disambiguation function to the provided context and ambiguous word
result = disambiguate_word(context, ambiguous_word)

# Specify the output file
output_file = "output.txt"

# Write the result to the output file
with open(output_file, "w") as file:
    print(result, file=file)

# Print a message indicating where the output is saved
print(f"Result saved to {output_file}")
