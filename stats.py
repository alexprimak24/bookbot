def open_file(path_to_file):
    with open(path_to_file) as f:
        return f.read()
    
def get_num_words(text):
    return len(text.split())

def unique_characters_count(text):
    text_lowercase = text.lower()
    characters_count = {}
    for char in text_lowercase:
        if char not in characters_count:
            characters_count[char] = 1
        else:
            characters_count[char] += 1
    
    return characters_count

def handle_sort_dictionary(dictionary):

    def sort_on(dict):
        return dict["num"]
        
    entries_list = []

    for entry in dictionary:
        new_entry = {"char": entry, "num":dictionary[entry]}
        entries_list.append(new_entry)

    entries_list.sort(reverse=True,key=sort_on)

    return entries_list
    
            