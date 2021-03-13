# Problem Set 4C
# Name: pialin
# Collaborators:
# Time Spent: x:xx

import string
import random                   
from ps4a import get_permutations

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
    
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words.copy()
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        # vowels = 'aeiou'
        lower_letters = string.ascii_lowercase #'abcdefghijklmnopqrstuvwxyz'
        upper_letters = string.ascii_uppercase #'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        dictionary = {}
         #random permutation of vowels 'aeiou'
        # one_permutation_vowels = random.choice(get_permutations(vowels_permutation))
        #lower_letter case
        for i in range(26):
            if lower_letters[i] in VOWELS_LOWER:
                vowel_index = VOWELS_LOWER.find(lower_letters[i])
                dictionary[lower_letters[i]] = vowels_permutation[vowel_index]
            else:
                dictionary[lower_letters[i]] = lower_letters[i]
        #upper_letter case
        for i in range(26):
            if upper_letters[i] in VOWELS_UPPER:
                vowel_index = VOWELS_UPPER.find(upper_letters[i])
                dictionary[upper_letters[i]] = vowels_permutation[vowel_index].upper()
            else:
                dictionary[upper_letters[i]] = upper_letters[i]
        
        return dictionary
            
    
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        word = ""
        for letter in self.get_message_text(): #self.message_text:
            if letter in string.ascii_letters:
                word = word + transpose_dict[letter]
            else:
                word = word + letter             
        return word

        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        SubMessage.__init__(self, text)

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        list_permutation_vowels = get_permutations(VOWELS_LOWER)
        max_number_of_real_words = 0
        
        for l in list_permutation_vowels:
            number_of_real_words = 0
            transpose_dict = self.build_transpose_dict(l)
            decoded_message = self.apply_transpose(transpose_dict)
            for word in decoded_message.split(' '):
                #add number of valid_word if is_world is True

                if is_word(self.get_valid_words(), word) == True:
                    number_of_real_words += 1
                else:
                    pass
            if number_of_real_words > max_number_of_real_words:
                max_number_of_real_words = number_of_real_words
                best_vowels_order = [l] 
                decrypted_message = [decoded_message]
            elif number_of_real_words == max_number_of_real_words: #in case 
                best_vowels_order.append(l)
                decrypted_message.append(decoded_message)
            else:             
                pass
        return (best_vowels_order, decrypted_message)
            
        
    

if __name__ == '__main__':

    # Example test case
    # message = SubMessage("Hello World!")
    # permutation = "eaiuo"
    # enc_dict = message.build_transpose_dict(permutation)
    # print("Original message:", message.get_message_text(), "Permutation:", permutation)
    # print("Expected encryption:", "Hallu Wurld!")
    # print("Actual encryption:", message.apply_transpose(enc_dict))
    # enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    # print("Decrypted message:", enc_message.decrypt_message())

    #TODO: WRITE YOUR TEST CASES HERE
    message = SubMessage("I hope tomorrow will be sunny!")
    permutation = "uiaeo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "A hepi temerrew wall bi sonny!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
    
    #test2
    # message = SubMessage("A cold breeze was stirring. There was light traffic to Oakland, heavier than in the closed world, surely far lighter than the traffic in a fully open world will be. The day was nearing the anniversary of Gov. Gavin Newsom's shelter in place order. My phone reminded me that this time a year ago, I'd made a huge shopping trip out of wild hope that somehow enough groceries would help us weather this thing out. I saluted the self who believed at that moment that she could buy enough frozen chicken to last a pandemic.")
    # permutation = "uieoa"
    # enc_dict = message.build_transpose_dict(permutation)
    # print("Original message:", message.get_message_text(), "Permutation:", permutation)
    # print("Expected encryption:", "U cold briizi wus sterreng. Thiri wus leght truffec to Ouklund, hiuveir thun en thi closid world, sarily fur leghtir thun thi truffec en u fally opin world well bi. Thi duy wus niureng thi unnevirsury of Gov. Guven Niwsom's shiltir en pluci ordir. My phoni rimendid mi thut thes temi u yiur ugo, E'd mudi u hagi shoppeng trep oat of weld hopi thut somihow inoagh grocireis woald hilp as wiuthir thes theng oat. E sulatid thi silf who bileivid ut thut momint thut shi coald bay inoagh frozin checkin to lust u pundimec.")
    # print("Actual encryption:", message.apply_transpose(enc_dict))
    # enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    # print("Decrypted message:", enc_message.decrypt_message())

