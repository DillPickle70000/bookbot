def get_num_words(text):
    return len(text.split())

def get_num_unique_characters(text):
    lower_text = text.lower()
    counts = {}
    for char in lower_text:
        if char.isalpha():
            counts[char] = counts.get(char, 0) + 1
    unique_characters = len(counts)
    return unique_characters, counts


def _num_key(item):
    """Helper: return the 'num' value for a char-count dict (used as sort key)."""
    return item["num"]


def sort_character_counts(counts_dict):
    """Convert a counts dict (char -> int) into a list of dicts
    like {"char": <char>, "num": <count>} and sort it from
    greatest to least by the count using .sort() and a helper key.
    """
    items = [{"char": k, "num": v} for k, v in counts_dict.items()]
    items.sort(key=_num_key, reverse=True)
    return items