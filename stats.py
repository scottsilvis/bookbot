

def count_words(text: str) -> int:
    return len(text.split())

def char_count(text: str) -> dict:

    text_lower = text.lower()

    tally = {}
    for i in text_lower:
        if i not in tally:
            tally[i] = 1
        else: tally[i] += 1
    return tally


def sort_on(dictionary):
    return dictionary["num"]

def sort_out(dictionary: dict):
    result_list = []
    for character in dictionary:
        new_dict = {"char": character, "num": dictionary[character]}
        result_list.append(new_dict)
    result_list.sort(reverse=True, key=sort_on)
    return result_list