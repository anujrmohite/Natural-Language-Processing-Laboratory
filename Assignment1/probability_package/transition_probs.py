def calculate_transition_probs(tagged_sentences):
    transition_probs = {}  # empty dictionary to store transition probabilities

    # Iterate through each sentence in the tagged_sentences
    for sentence in tagged_sentences:
        for i in range(len(sentence) - 1):
            # Get the part-of-speech tags for the current word and the next word
            prev_tag, tag = sentence[i][1], sentence[i + 1][1]
            if prev_tag in transition_probs:
                # If the previous tag is already in transition_probs
                if tag in transition_probs[prev_tag]:
                    # If the current tag is already associated with the previous tag, increment its count
                    transition_probs[prev_tag][tag] += 1
                else:
                    # If the current tag is not associated with the previous tag, create a new entry with a count of 1
                    transition_probs[prev_tag][tag] = 1
            else:
                # If the previous tag is not in transition_probs, create a new entry with the current tag and a count of 1
                transition_probs[prev_tag] = {tag: 1}

    # Normalize transition probabilities
    for prev_tag in transition_probs:
        total_transitions = sum(transition_probs[prev_tag].values())  # Calculate the total number of transitions from the previous tag
        for tag in transition_probs[prev_tag]:
            # Normalize each transition probability by dividing its count by the total transitions
            transition_probs[prev_tag][tag] /= total_transitions

    print(transition_probs, '\n')  # Print the transition probabilities (for debugging)

    return transition_probs  # Return the normalized transition probabilities
