import nltk

def read_grammar(grammar_file):
    with open(grammar_file, "r") as file:
        grammar_content = file.read()
    return nltk.PCFG.fromstring(grammar_content)

def cyk_parse(sentence, pcfg_grammar):
    words = sentence.split()
    chart = nltk.ChartParser(pcfg_grammar)
    parses = list(chart.parse(words))

    return parses

def save_output_to_file(output_file_path, parses):
    with open(output_file_path, "w") as output_file:
        for parse in parses:
            output_file.write("Most Probable Parse:\n")
            output_file.write(str(parse) + "\n")

def main():
    grammar_file = "grammar.txt"
    pcfg_grammar = read_grammar(grammar_file)

    input_sentence = "the dog chased the cat"
    parses = cyk_parse(input_sentence, pcfg_grammar)

    output_file_path = "142103002_Assign4_Output.txt"
    save_output_to_file(output_file_path, parses)


if __name__ == "__main__":
    main()
