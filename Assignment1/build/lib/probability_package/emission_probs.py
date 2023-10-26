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
