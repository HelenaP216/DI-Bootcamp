# Daily Challenge: Text Analysis
# 
# Key Python Topics:
#     OOP (Classes, Class Methods, Inheritance)
#     File handling (open())
#     String manipulation (split(), join(), translate(), regular expressions)
#     Dictionaries
#     Sets
#     Lists
#     string module
#     re module (regular expressions)

# Instructions:
# Create a Text class to analyze text data, either 
# from a string or a file. Then, create a 
# TextModification class to perform text cleaning.

# Part I: Analyzing a Simple String
# Step 1: Create the Text Class
#     Create a class called Text.
#     The __init__ method should take a string as an 
#       argument and store it in an attribute 
#       (e.g: self.text).

import re
import string

class Text:
    def __init__(self, text: str):
        self.text = text

    def _tokens(self):
        """
        Returns a list of lowercase words, with no punctuation.
        """
        return re.findall(r"[A-Za-z']+", self.text.lower())

# Step 2: Implement word_frequency Method
#     Create a method called word_frequency(word).
#     Split the text attribute into a list of words.
#     Count the occurrences of the given word in the 
#       list.
#     Return the count.
#     If the word is not found, return None or a 
#       meaningful message.

    def word_frequency(self, word: str):
        words = self._tokens()
        target = word.lower()
        count = words.count(target)
        return count if count > 0 else None
    
# Step 3: Implement most_common_word Method
#     Create a method called most_common_word().
#     Split the text into a list of words.
#     Use a dictionary to store word frequencies.
#     Find the word with the highest frequency.
#     Return the most common word.

    def most_common_word(self):
        words = self._tokens()
        if not words:
            return None

        freq = {}
        for w in words:
            freq[w] = freq.get(w, 0) + 1

        # Return the word with the highest count
        return max(freq, key=freq.get)

# Step 4: Implement unique_words Method
#     Create a method called unique_words().
#     Split the text into a list of words.
#     Use a set to store unique words.
#     Return the unique words as a list.

    def unique_words(self):
        return list(set(self._tokens()))
    
# Part II: Analyzing Text from a File
# Step 5: Implement from_file Class Method
#     Create a class method called 
#       from_file(file_path).
#     Open the file at file_path in read mode.
#     Read the file content.
#     Create and return a Text instance with the file 
#       content as the text.

    @classmethod
    def from_file(cls, file_path: str):
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        return cls(content)
    
# Bonus: Text Modification
# Step 6: Create the TextModification Class
#     Create a class called TextModification that 
#       inherits from Text.

# Step 7: Implement remove_punctuation Method
#     Create a method called remove_punctuation().
#     Use the string module to get a string of 
#       punctuation characters.
#     Use a string method or regular expressions to 
#       remove punctuation from the text attribute.
#     Return the modified text.

class TextModification(Text):
    def remove_punctuation(self):
        # Removing punctuation characters
        translator = str.maketrans("", "", string.punctuation)
        self.text = self.text.translate(translator)
        return self.text
    
# Step 8: Implement remove_stop_words Method
#     Create a method called remove_stop_words().
#     Search online for a list of English stop words 
#       (common words like “a”, “the”, “is”).
#     Split the text into a list of words.
#     Filter out stop words from the list.
#     Join the remaining words back into a string.
#     Return the modified text.

    def remove_stop_words(self):
        # Base list derived from common English stop-word list.
        stop_words = {
            "a","an","the","and","or","but","if","because","as","until","while",
            "of","at","by","for","with","about","against","between","into","through",
            "during","before","after","above","below","to","from","up","down","in",
            "out","on","off","over","under","again","further","then","once","here",
            "there","when","where","why","how","all","any","both","each","few","more",
            "most","other","some","such","no","nor","not","only","own","same","so",
            "than","too","very","can","will","just","don","should","now",
            "i","me","my","we","our","you","your","he","him","his","she","her","it",
            "its","they","them","their","is","are","was","were","be","been","being",
            "have","has","had","do","does","did"
        }

        tokens = re.findall(r"[A-Za-z']+", self.text.lower())
        filtered = [w for w in tokens if w not in stop_words]
        self.text = " ".join(filtered)
        return self.text

# Step 9: Implement remove_special_characters Method
#     Create a method called
#       remove_special_characters().
#     Use regular expressions to remove special 
#       characters from the text attribute.
#     Return the modified text.

    def remove_special_characters(self):
        # Replacing everything else than letters, numbers and whitespace with space.
        self.text = re.sub(r"[^A-Za-z0-9\s]", " ", self.text)
        # Collapse multiple spaces
        self.text = re.sub(r"\s+", " ", self.text).strip()
        return self.text

# Testing:
t = Text("Hello, hello, shalom! This is a test. This test is simple, but it is effective.")
print(t.word_frequency("test"))      # 2
print(t.most_common_word())          # 'this' or 'test' or 'hello' (depends on counts)
print(sorted(t.unique_words()))      # list of unique words

tm = TextModification("Wow!!! This... is indeed a *very* messy room !!! Room #1   !!")
print(tm.remove_punctuation())
print(tm.remove_special_characters())
print(tm.remove_stop_words())
