def get_num_words(text):
    text = text.split()
    num = len(text)
    return num

def char_count(text):
    freq = dict()
    for words in text:
        for letter in words:
            if (letter.lower()) in freq:
                freq[(letter.lower())] += 1
            else:
                freq[(letter.lower())] = 1
    freq = sorted(freq.items(), key=lambda item:item[1], reverse = True) 
    return freq
