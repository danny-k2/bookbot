def word_count(book_text):
    words = book_text.split()
    count = len(words)
    return count

def character_count(book_text):
    character_dictionary = {}
    for char in book_text.lower():
        if char not in character_dictionary:
            character_dictionary[char] = 1
        else:
            character_dictionary[char] += 1
    return character_dictionary

def sort_on(items):
    return items["num"]

def character_sort(sorted_dictionary):
    sorted = []
    for char in sorted_dictionary:
        sorted.append({"character": char, "num": sorted_dictionary[char]})
    sorted.sort(reverse=True, key=sort_on)
    return sorted