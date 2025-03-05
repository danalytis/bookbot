def get_num_words(string):
    return f"Found {len(string.rsplit())} total words"


def times_each_char(text):
    results = {}
    for char in text.lower():
        results[char] = results.get(char, 0) + 1
    return results


def sort_results(text):
    del text[" "]
    return sorted(text.items(), key=lambda item: item[1], reverse=True)
