class Dictionary:
    def __init__(self):
        self.words = {}
    def get_word(self, word):
        return self.words.get(word, "Rijec nije pronadjena u rjecniku.")

class EnglishDictionary(Dictionary):
    def __init__(self):
        
        self.words = {
            "hello": "zdravo",
            "goodbye": "dovidjenja",
            "house": "kuca",
        }

class GermanDictionary(Dictionary):
    def __init__(self):
        
        self.words = {
            "halo": "zdravo",
            "chus": "dovidjenja",
            "haus": "kuca",
        }

englishdict = EnglishDictionary()
a = input("Molimo unesite rijec na Engleskom: ")
germandict = GermanDictionary()
b = input("Molimo unesite rijec na Njemackom: ")
print(englishdict.get_word(a))
print(germandict.get_word(b))


