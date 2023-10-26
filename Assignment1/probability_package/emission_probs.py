def calculate_emission_probs(tagged_sentences):
    emission_probs = {}  # empty dictionary to store emission probabilities

    # Iterate through each sentence in the tagged_sentences
    for sentence in tagged_sentences:
        for word, tag in sentence:
            if tag in emission_probs:
                # If the tag is already in emission_probs
                if word in emission_probs[tag]:
                    # If the word is already associated with the tag, increment the count
                    emission_probs[tag][word] += 1
                else:
                    # If the word is not associated with the tag, initialize its count to 1
                    emission_probs[tag][word] = 1
            else:
                # If the tag is not in emission_probs, create a new entry for it with the word and a count of 1
                emission_probs[tag] = {word: 1}

    # Normalize emission probabilities
    for tag in emission_probs:
        total_emissions = sum(emission_probs[tag].values())  # Calculate the total emissions for the tag
        for word in emission_probs[tag]:
            # Normalize each word's count by dividing it by the total emissions
            emission_probs[tag][word] /= total_emissions

    return emission_probs  # Return the normalized emission probabilities
