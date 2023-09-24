import re


class Document:
    def __init__(self, path, preprocessing_fn):
        # Reading raw data
        with open(path, 'r') as f:
            self.raw_data = f.read()

        # Setting preprocessing_fn as an attribute
        self.preprocessing_fn = preprocessing_fn

        # preprocessing data
        self.preprocessed_data = preprocessing_fn(self.raw_data)

        # building the vocabulary
        tokens = self.preprocessed_data.split(' ')

        # Unique tokens
        self.vocabulary = set(tokens)

        # Frequencies
        self.frequencies = {
            w: self.preprocessed_data.count(w) for w in self.vocabulary}

    def __len__(self):
        return len(self.frequencies)

    def __getitem__(self, idx):
        if type(idx) is str:
            if idx in self.frequencies:
                return (idx, self.frequencies[idx])
            else:
                raise IndexError(f"Word '{idx}' does not"
                                 " exist in the vocabulary.")
        elif type(idx) is int:
            items_list = list(self.frequencies.items())
            return items_list[idx]
        else:
            raise TypeError("Document indices must be a str or an int,"
                            f" not {type(idx)}")


def my_preprocessing(text):
    _text = text.lower()
    _text = _text.replace('\n', ' ')
    _text = re.sub(r'\d+', '', _text)
    _text = re.sub(r'[^\w\s]', '', _text)
    _text = _text.strip()

    return _text


doc = Document(path='./data/shakespeare.txt',
               preprocessing_fn=my_preprocessing)
