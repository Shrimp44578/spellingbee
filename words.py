import json
import string

with open('dictionary.json') as json_file:
    words_list = set(json.load(json_file).keys())  # Ensure words are a set for faster lookup

letters = list(string.ascii_lowercase)

def isPangram(word: str, game_letters: set) -> bool:
    word_letters = set(word)
    return word_letters == game_letters

def is_valid_word(word, game_letters, center_letter):
    """
    Check if the word is valid:
    - Contains only letters from game_letters
    - Uses the center letter at least once
    - Is at least 4 letters long
    - Is in the dictionary
    """
    if len(word) < 4:
        return False
    if center_letter not in word:
        return False
    for letter in word:
        if letter not in game_letters:
            return False
    if word not in words_list:
        return False
    return True

def getScore(word, game_letters, center_letter):
    """
    Calculate the score for a valid word.
    """
    score = len(word)  # Simple scoring: 1 point per letter
    pangram = set(game_letters) == set(word)
    if pangram:
        score += 7  # Bonus for pangram
    return score, pangram