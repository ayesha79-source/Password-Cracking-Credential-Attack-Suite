
def generate_dictionary(seed_words):
    wordlist = set()

    for word in seed_words:
        word = word.strip()

        if not word:
            continue

        variations = [
            word,
            word.lower(),
            word.upper(),
            word.capitalize(),
            word + "123",
            word + "2026",
            word + "!",
            word.replace("a", "@"),
            word.replace("i", "1"),
            word.replace("o", "0")
        ]

        wordlist.update(variations)

    return sorted(wordlist)


def save_dictionary(wordlist, filename="generated_wordlist.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        for word in wordlist:
            file.write(word + "\n")

    return filename
