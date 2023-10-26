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
    print(transition_probs,'\n')
    return transition_probs
