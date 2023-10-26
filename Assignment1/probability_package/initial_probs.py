def calculate_initial_probs(tagged_sentences):
    initial_probs = {}  # Initialize an empty dictionary to store initial probabilities

    total_sentences = len(tagged_sentences)  # Get the total number of sentences in the corpus

    # Iterate through each sentence in the tagged_sentences
    for sentence in tagged_sentences:
        initial_tag = sentence[0][1]  # Get the part-of-speech tag of the first word in the sentence
        if initial_tag in initial_probs:
            # If the tag is already in initial_probs, increment its count
            initial_probs[initial_tag] += 1
        else:
            # If the tag is not in initial_probs, create a new entry with a count of 1
            initial_probs[initial_tag] = 1

    # Normalize initial probabilities
    for tag in initial_probs:
        initial_probs[tag] /= total_sentences  # Calculate the probability by dividing the count by the total number of sentences

    return initial_probs  # Return the normalized initial probabilities
