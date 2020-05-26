# Generate text8 Train/Validation/Test Datasets
def generate_text8(train_split=0.7, valid_split=0.1, test_split=0.2, save_data=True):
    assert train_split + valid_split + test_split == 1

    text8_raw = open("text8/text8", "r").read()

    # Print text8 Stats
    all_words = text8_raw.split()
    unique_characters = {x for word in set(all_words) for x in word}
    print("Total Tokens: {:,} tokens.".format(len(all_words)))
    print("Word Vocab Size (|V|): {:,} words.".format(len(set(all_words))))
    print("Character Vocab Size (|C|): {:,} characters.".format(len(unique_characters)))

    text8_length = len(text8_raw)
    train_end = int(text8_length*train_split)
    train_data = text8_raw[: train_end]
    if valid_split > 0:
        valid_end = train_end + int(text8_length*valid_split)
        valid_data = text8_raw[train_end : valid_end]
    else:
        valid_end = train_end
        valid_data = ''
    test_data = text8_raw[valid_end :]

    print("Train Size: {:,} characters.".format(len(train_data)))
    print("Validation Size: {:,} characters.".format(len(valid_data)))
    print("Test Size: {:,} characters.".format(len(test_data)))

    if save_data:
        f = open("text8/train.txt", "w")
        f.write(train_data)
        f.close()

        if valid_data != '':
            f = open("text8/valid.txt", "w")
            f.write(valid_data)
            f.close()

        f = open("text8/test.txt", "w")
        f.write(test_data)
        f.close()

    return train_data, valid_data, test_data

def main():
    train_data, valid_data, test_data = generate_text8()


if __name__ == '__main__':
    main()