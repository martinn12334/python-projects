sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
sentence_list = sentence.split()
result = {word: len(word) for word in sentence_list}
print(result)