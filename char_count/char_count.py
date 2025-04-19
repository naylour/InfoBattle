from functools import reduce

def char_count(text: str):
    text = text.lower()

    chars_count = reduce(lambda acc, char: {**acc, char: acc.get(char, 0) + 1}, text, {})

    filtered_chars = {char: count for char, count in chars_count.items() if count > 1}

    necessary_matches = filtered_chars.keys()

    return len(necessary_matches)

print(char_count('aA11'))
