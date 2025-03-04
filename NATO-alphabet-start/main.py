import pandas

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")

# TODO 1. Create a dictionary in this format # {"A": "Alfa", "B": "Bravo"}:
nato_dict = {row.letter: row.code for index, row in nato_data.iterrows()}


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# Error handling 
def generate_phonetic():
    username = input("Enter your name: ").upper()
    try:
        list_letters = [nato_dict[letter] for letter in username]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(list_letters)


generate_phonetic()
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
