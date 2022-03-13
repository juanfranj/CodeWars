
class Dictionary:
    def __init__(self,words):
        self.words=words
    def find_most_similar(self,term):
        counts = []
        for word in self.words:
            count = 0
            if term == word:
                return word
            else:
                for i in range(min(len(term), len(word))):
                    count += abs(ord(term[i]) - ord(word[i])) + max(0, len(word)-len(term))
            counts.append(count)
        min_count = min(counts)
        return self.words[counts.index(min_count)]
            


if __name__ == '__main__':
    words=['cherry', 'peach', 'pineapple', 'melon', 'strawberry', 'raspberry', 'apple', 'coconut', 'banana']
    test_dict=Dictionary(words)
    print(test_dict.find_most_similar('berry'))

