import nltk
from nltk.corpus import brown
nltk.download('brown')
tagged_sentences = brown.tagged_sents()

def calculate_transition_probs(tagged_sentences):
    transition_probs = {}
    for sentence in tagged_sentences:
        for i in range(len(sentence) - 1):
            prev_tag, tag = sentence[i][1], sentence[i + 1][1]
            if prev_tag in transition_probs:
                if tag in transition_probs[prev_tag]:
                    transition_probs[prev_tag][tag] += 1
                else:
                    transition_probs[prev_tag][tag] = 1
            else:
                transition_probs[prev_tag] = {tag: 1}

    # Normalize transition probabilities
    for prev_tag in transition_probs:
        total_transitions = sum(transition_probs[prev_tag].values())
        for tag in transition_probs[prev_tag]:
            transition_probs[prev_tag][tag] /= total_transitions

    return transition_probs

transition_probs = calculate_transition_probs(tagged_sentences)

def calculate_emission_probs(tagged_sentences):
    emission_probs = {}
    for sentence in tagged_sentences:
        for word, tag in sentence:
            if tag in emission_probs:
                if word in emission_probs[tag]:
                    emission_probs[tag][word] += 1
                else:
                    emission_probs[tag][word] = 1
            else:
                emission_probs[tag] = {word: 1}

    # Normalize emission probabilities
    for tag in emission_probs:
        total_emissions = sum(emission_probs[tag].values())
        for word in emission_probs[tag]:
            emission_probs[tag][word] /= total_emissions

    return emission_probs

emission_probs = calculate_emission_probs(tagged_sentences)

def calculate_initial_probs(tagged_sentences):
    initial_probs = {}
    total_sentences = len(tagged_sentences)
    for sentence in tagged_sentences:
        initial_tag = sentence[0][1]
        if initial_tag in initial_probs:
            initial_probs[initial_tag] += 1
        else:
            initial_probs[initial_tag] = 1

    # Normalize initial probabilities
    for tag in initial_probs:
        initial_probs[tag] /= total_sentences

    return initial_probs

initial_probs = calculate_initial_probs(tagged_sentences)

def viterbi_algorithm(sentence, transition_probs, emission_probs, initial_probs):
    words = nltk.word_tokenize(sentence)
    n = len(words)

    # Initialize the Viterbi matrix and backpointer matrix
    viterbi = [[0.0] * n for _ in range(len(transition_probs))]
    backpointer = [[-1] * n for _ in range(len(transition_probs))]

    # Initialize the first column of the Viterbi matrix
    for i, tag in enumerate(transition_probs):
        viterbi[i][0] = initial_probs.get(tag, 0.0001) * emission_probs[tag].get(words[0], 0.0001)

    # Forward pass
    for t in range(1, n):
        for i, tag in enumerate(transition_probs):
            max_score, max_backpointer = 0.0, -1
            for j, prev_tag in enumerate(transition_probs):
                # Calculate the score for transitioning from prev_tag to tag
                score = viterbi[j][t-1] * transition_probs[prev_tag].get(tag, 0.0001) * emission_probs[tag].get(words[t], 0.0001)
                if score > max_score:
                    max_score = score
                    max_backpointer = j
            viterbi[i][t] = max_score
            backpointer[i][t] = max_backpointer

    # Backtracking
    best_path = [-1] * n
    max_final_score, max_final_tag = 0.0, -1
    for i, tag in enumerate(transition_probs):
        if viterbi[i][n-1] > max_final_score:
            max_final_score = viterbi[i][n-1]
            max_final_tag = i

    best_path[n-1] = max_final_tag
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
