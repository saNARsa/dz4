def single_root_words(root_word , *other_words):
    same_words = []
    x = []
    for i in other_words:

        if root_word.lower() in i.lower():
            same_words.append(i)
        elif i.lower() in root_word.lower():
            same_words.append(i)
    print(same_words)


single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')