import nltk
import sklearn_crfsuite
from sklearn_crfsuite import metrics
import pycrfsuite

nltk.download('treebank')

def word_features(sentence, i):
    word = sentence[i][0]
    features = {
        'word': word,
        'is_first': i == 0,
        'is_last': i == len(sentence) - 1,
        'is_capitalized': word[0].upper() == word[0],
        'is_all_caps': word.upper() == word,
        'is_all_lower': word.lower() == word,
        'prefix-1': word[0],
        'prefix-2': word[:2],
        'prefix-3': word[:3],
        'suffix-1': word[-1],
        'suffix-2': word[-2:],
        'suffix-3': word[-3:],
        'prev_word': '' if i == 0 else sentence[i - 1][0],
        'next_word': '' if i == len(sentence) - 1 else sentence[i + 1][0],
        'has_hyphen': '-' in word,
        'is_numeric': word.isdigit(),
        'capitals_inside': word[1:].lower() != word[1:]
    }
    return features

# Function to perform POS tagging on input data
def pos_tagging(input_file, output_file):
    # Load the Penn Treebank corpus or use your own dataset
    corpus = nltk.corpus.treebank.tagged_sents()

    # Extract features and split the data
    X = []
    y = []
    for sentence in corpus:
        X_sentence = []
        y_sentence = []
        for i in range(len(sentence)):
            X_sentence.append(word_features(sentence, i))
            y_sentence.append(sentence[i][1])
        X.append(X_sentence)
        y.append(y_sentence)

    # Split the data into training and testing sets
    split = int(0.8 * len(X))
    X_train = X[:split]
    y_train = y[:split]
    X_test = X[split:]
    y_test = y[split:]

    # Train a CRF model using sklearn-crfsuite
    crf = sklearn_crfsuite.CRF(
        algorithm='lbfgs',
        c1=0.1,
        c2=0.1,
        max_iterations=100,
        all_possible_transitions=True
    )
    crf.fit(X_train, y_train)

    # Alternatively, you can use pycrfsuite for training and tagging
    trainer = pycrfsuite.Trainer(verbose=False)
    for x, y in zip(X_train, y_train):
        trainer.append(x, y)
    trainer.set_params({
        'c1': 1.0,
        'c2': 1e-3,
        'max_iterations': 50,
        'feature.possible_transitions': True
    })
    trainer.train('pos.crfsuite')

    tagger = pycrfsuite.Tagger()
    tagger.open('pos.crfsuite')

    # Read input data from the input file
    with open(input_file, 'r') as infile:
        input_data = [line.strip() for line in infile.readlines()]

    # Perform POS tagging on the input data
    tagged_data = []
    for sentence in input_data:
        features = [word_features(list(zip(sentence.split(), [''] * len(sentence.split()))), i) for i in range(len(sentence.split()))]
        tags = tagger.tag(features)
        tagged_data.append(list(zip(sentence.split(), tags)))

    # Write the tagged data to the output file
    with open(output_file, 'w') as outfile:
        for tagged_sentence in tagged_data:
            outfile.write(' '.join([f'{token} {tag}' for token, tag in tagged_sentence]) + '\n')

if __name__ == "__main__":
    input_file = 'input.txt'  # Specify your input file
    output_file = 'output.txt'  # Specify your output file

    pos_tagging(input_file, output_file)
