import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.models import load_model
import numpy as np 
tokenizer = Tokenizer()
data = open("./data/nlp/poem_generation.txt").read()
corpus = data.lower().split("\n")
tokenizer.fit_on_texts(corpus)

total_words = len(tokenizer.word_index)+1

# print(tokenizer.word_index)
print("Total Words: ",total_words)
max_sequence_len = 16

model = load_model("./models/poem_generation.h5")

def generate_poem(seed_text):
    
    next_words = 50

    for _ in range(next_words):
        token_list = tokenizer.texts_to_sequences([seed_text])[0]
        token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
        predicted = np.argmax(model.predict(token_list), axis=-1)
        output_word = ""
        for word, index in tokenizer.word_index.items():
            if index == predicted:
                output_word = word
                break
        seed_text += " " + output_word

    last = seed_text.split(" ")
    N =6
    group_list = [last[n:n+N] for n in range(0, len(last), N)]
    poem = []
    for i in group_list:
        verses = " ".join(i)
        poem.append(verses)

    print(poem)

    return poem

