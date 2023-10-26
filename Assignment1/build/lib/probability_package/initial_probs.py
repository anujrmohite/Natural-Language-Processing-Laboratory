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
