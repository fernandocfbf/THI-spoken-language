class Tokenizer():

    def __init__(self, window_size):
        self.window_size = window_size

    def tokenize(self, dataset):
        word_to_index = dict()
        index = 0
        for sentence in dataset:
            for word in sentence.split():
                if word not in word_to_index:
                    word_to_index[word] = index
                    index += 1
        self.word_to_index = word_to_index

    def get_train_examples(self, dataset):
        train_examples = list()
        for sentence in dataset:
            for index, target_word in enumerate(sentence.split()):
                context_word_indices = list()
                for j in range(
                    max(0, index - self.window_size),
                    min(index + self.window_size + 1, len(sentence.split()))
                ):
                    if j != index:
                        context_word_indices.append(self.word_to_index[sentence.split()[j]])
                train_examples.append((self.word_to_index[target_word], context_word_indices))
        return train_examples
        