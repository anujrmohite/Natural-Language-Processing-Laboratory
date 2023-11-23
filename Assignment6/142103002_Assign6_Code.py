import nltk
from nltk.corpus import wordnet
from nltk.wsd import lesk
from nltk import word_tokenize

nltk.download("wordnet")


def disambiguate_word(context, ambiguous_word):
    # Tokenizing the context into a list of words
    context_tokens = word_tokenize(context)
    # Lesk algorithm to disambiguate the meaning of the ambiguous word
    sense = lesk(context_tokens, ambiguous_word)

    if sense:
        definition = sense.definition()
        return f"The appropriate sense of ->'{ambiguous_word}' in the context is: -> {definition}"
    else:
        return (
            f"No appropriate sense found for ->'{ambiguous_word}' in the given context."
        )


context = "I went to the bank to deposit some money."
ambiguous_word = "bank"

# passing for provided context and ambiguous word
result = disambiguate_word(context, ambiguous_word)

output_file = "142103002_Assign6_Output.txt"
with open(output_file, "w") as file:
    print(result, file=file)
print(f"Result saved to {output_file}")
