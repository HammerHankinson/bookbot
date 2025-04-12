def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_counts = {}

    for char in text.lower():
      if char in char_counts:
        char_counts[char] += 1
      else: char_counts[char] = 1
    return char_counts

def sort_character_counts(char_counts):
    sorted_list = [{'char': char, "count": count} for char, count in char_counts.items()]
    sorted_list.sort(key=lambda x: x['count'], reverse=True)
    return sorted_list