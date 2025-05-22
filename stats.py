def count_words(text):
	"""Counts the number of words book text string, prints the count"""
	num_words = len(text.split())
	print(f"{num_words} words found in the document")
	return num_words

def char_frequency(text):
    """
    Counts the frequency of each character in the text (case-insensitive).
    
    Args:
        text (str): The input text string
        
    Returns:
        dict: A dictionary with characters as keys and their frequencies as values
    """
    # Initialize an empty dictionary to store character counts
    freq_dict = {}
    
    # Convert text to lowercase
    text = text.lower()
    
    # Iterate through each character in the text
    for char in text:
        # Add or update the character count in the dictionary
        freq_dict[char] = freq_dict.get(char, 0) + 1
    return freq_dict

def sorted_list(freq_dict):
    # Create a list of dictionaries with the required structure
    chars_list = []
    for char, count in freq_dict.items():
        chars_list.append({"char": char, "num": count})
    
    # Define a helper function for sorting
    def sort_on(dict):
        return dict["num"]
    
    # Sort the list from greatest to least
    chars_list.sort(reverse=True, key=sort_on)
    
    return chars_list

