#1
sentence = input("Enter a sentence: ")
print("Total number of characters:", len(sentence))


#2
words = sentence.split()
print("Total number of words:", len(words))

print("First word:", words[0])
print("Last word:" , words[-1])


#3
print("First three characters:", sentence[:3])

print("Last three characters:", sentence[-3:])

print("Sentence in reverse:", sentence[::-1])


#4
print("Uppercase:", sentence.upper())

print("Lowercase:", sentence.lower())

print("With hyphens:", sentence.replace(" ", "-"))
