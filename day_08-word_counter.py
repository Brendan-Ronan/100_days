# Word counter
print("Welcome to word counter! Enter any amount of text and the program will return the number of words.")

# user input
text = input("Enter text: ")

# count words
def word_counter(text):

    text = text.split()
    word_count = len(text)
    print(f"There are {word_count} words in this text.\n")
      

# count characters
def char_counter(text):

    count_char = len(text)
    print(f"There are {count_char} characters in this text.\n")

# count of unique words
def unique_words(text):
    unique = []
    text = text.split()

    for words in text:
        if words not in unique: 
            unique.append(words)
        else: continue

    unique_count = len(unique)
    print(f"There are {unique_count} unique words in this text.")


# call functions
word_counter(text)
char_counter(text)
unique_words(text)





