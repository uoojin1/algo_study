'''
3
jim likes mary
kate likes tom
tom does not like jim
2
jim tom
likes
Sample Output 0

2
0 1
'''

def textQueries(sentences, queries):
    ret = []
    for querie in quries:
        word_count = {}
        for word in querie:
            if word in word_count:
                world_count[word] += 1
            else:
                world_count[word] = 1
        # initialized
        in_sentence = []
        for sentence in sentences:
            words = sentence.split(' ')
            counter = 0
            for word in words:
                if word in word_count:
                    in_sentence.append(word)
        ret.append(in_sentence)
