import nltk
from nltk.corpus import brown
nltk.download('brown')
tagged_sentences = brown.tagged_sents()
from probability_package import calculate_transition_probs, calculate_emission_probs, calculate_initial_probs

transition_probs = calculate_transition_probs(tagged_sentences)
emission_probs = calculate_emission_probs(tagged_sentences)
initial_probs = calculate_initial_probs(tagged_sentences)

def viterbi_algorithm(sentence, transition_probs, emission_probs, initial_probs):
    # Tokenized the input sentence into words
    words = nltk.word_tokenize(sentence)
    n = len(words)  # Get the number of words in the sentence

    # Initialized the Viterbi matrix and backpointer matrix
    viterbi = [[0.0] * n for _ in range(len(transition_probs))]
    backpointer = [[-1] * n for _ in range(len(transition_probs))]

    # Initialize the first column of the Viterbi matrix
    for i, tag in enumerate(transition_probs):
        # Calculate the initial score for each tag based on initial and emission probabilities
        viterbi[i][0] = initial_probs.get(tag, 0.0001) * emission_probs[tag].get(words[0], 0.0001)

    # Forward pass
    for t in range(1, n):
        for i, tag in enumerate(transition_probs):
            max_score, max_backpointer = 0.0, -1
            for j, prev_tag in enumerate(transition_probs):
                # Calculate the score for transitioning from prev_tag to tag
                score = viterbi[j][t-1] * transition_probs[prev_tag].get(tag, 0.0001) * emission_probs[tag].get(words[t], 0.0001)

                # Update max_score and max_backpointer if a higher score is found
                if score > max_score:
                    max_score = score
                    max_backpointer = j

            # Update the Viterbi matrix and backpointer matrix with the best score and backpointer
            viterbi[i][t] = max_score
            backpointer[i][t] = max_backpointer

    # Backtracking
    best_path = [-1] * n
    max_final_score, max_final_tag = 0.0, -1

    # Find the tag with the highest score in the last column of the Viterbi matrix
    for i, tag in enumerate(transition_probs):
        if viterbi[i][n-1] > max_final_score:
            max_final_score = viterbi[i][n-1]
            max_final_tag = i

    # Set the last tag in the best path
    best_path[n-1] = max_final_tag

    # Backtrack to find the best sequence of tags
    for t in range(n-1, 0, -1):
        best_path[t-1] = backpointer[best_path[t]][t]

    # Create a tagged sentence based on the best path
    tagged_sentence = [(words[i], list(transition_probs.keys())[best_path[i]]) for i in range(n)]

    return tagged_sentence

def process_input_file(input_filename, output_filename, transition_probs, emission_probs, initial_probs):
    with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
        for line in input_file:
            sentence = line.strip()
            result = viterbi_algorithm(sentence, transition_probs, emission_probs, initial_probs)
            # tagged sentence to the output file
            output_file.write(" ".join([f"{word}_{tag}" for word, tag in result]) + '\n')

input_filename = "142103002_Assign1_Input.txt"
output_filename = "142103002_Assign1_Output.txt"

process_input_file(input_filename, output_filename, transition_probs, emission_probs, initial_probs)
