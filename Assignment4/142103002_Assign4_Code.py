import nltk

# Function to read a Probabilistic Context-Free Grammar (PCFG) from a file
def read_grammar(grammar_file):
    # Open and read the content of the grammar file
    with open(grammar_file, "r") as file:
        grammar_content = file.read()
    # Convert the grammar content to an nltk.PCFG object
    return nltk.PCFG.fromstring(grammar_content)


# Function to perform Cocke–Younger–Kasami (CYK) parsing on a sentence using a PCFG
def cyk_parse(sentence, pcfg_grammar):
    # Split the input sentence into words
    words = sentence.split()
    # Create a ChartParser object with the given PCFG grammar
    chart = nltk.ChartParser(pcfg_grammar)
    # Perform CYK parsing and obtain a list of parses
    parses = list(chart.parse(words))
    return parses


# Function to save the CYK parsing output to a file
def save_output_to_file(output_file_path, parses):
    # Open the output file in write mode
    with open(output_file_path, "w") as output_file:
        # Iterate through the list of parses
        for parse in parses:
            # Write the header indicating the most probable parse
            output_file.write("Most Probable Parse:\n")
            # Write the parse tree to the file as a string
            output_file.write(str(parse) + "\n")


# Main function
def main():
    # File path for the grammar file
    grammar_file = "grammar.txt"
    # Read the PCFG grammar from the file
    pcfg_grammar = read_grammar(grammar_file)

    # Input sentence to be parsed
    input_sentence = "the dog chased the cat"
    # Perform CYK parsing on the input sentence using the PCFG grammar
    parses = cyk_parse(input_sentence, pcfg_grammar)

    # File path for the output file
    output_file_path = "142103002_Assign4_Output.txt"
    # Save the CYK parsing output to the specified file
    save_output_to_file(output_file_path, parses)

# Entry point of the script
if __name__ == "__main__":
    main()
