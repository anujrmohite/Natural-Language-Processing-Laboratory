from collections import defaultdict

def build_ngram_models(input_file, output_file_prefix, n):
    ngram_models = defaultdict(int)

    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            words = line.strip().split()

            ngrams = [tuple(words[i:i + n]) for i in range(len(words) - n + 1)]

            for ngram in ngrams:
                ngram_models[ngram] += 1

    with open(f"{output_file_prefix}_{n}gram-output.txt", 'w', encoding='utf-8') as out_file:
        for ngram, count in ngram_models.items():
            out_file.write(f"{' '.join(ngram)} {count}\n")

input_file = "input_dataset.txt"
build_ngram_models(input_file, "142103002", 2)  # For bi-grams
build_ngram_models(input_file, "142103002", 3)  # For tri-grams
