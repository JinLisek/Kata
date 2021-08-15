def remove_duplicate_words(text: str):
    result = ""

    found_words = set()

    for word in text.split(" "):
        if word not in found_words:
            result += word + " "

        found_words.add(word)

    return result[:-1]
