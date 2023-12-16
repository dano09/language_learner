import pandas as pd
from random import shuffle


def load_vocab_data():
    vocab = pd.read_excel("C:\\Users\\jdano\\Desktop\\bahasa.xlsx")
    categories = vocab['category'].unique()
    types = vocab['type'].unique()
    return {'vocab': vocab, 'categories': categories, 'types': types}


def play_flash_card_game(card_data, cards_for_match, flash_card_type):
    incorrect = []
    for i, c in enumerate(cards_for_match):
        user_guess = input(f'\n {i}/{len(cards_for_match)}: Type the translation for: {c}')
        answer = card_data[c][flash_card_type]
        correct = user_guess == answer
        if not correct:
            incorrect.append(c)
        correct_label = 'CORRECT!' if correct == True else 'INCORRECT!'
        print(f'\n{correct_label} You typed: {user_guess} \nand the answer is: {answer}')
    return incorrect



def run():
    data = load_vocab_data()
    vocab = data['vocab']
    categories = data['categories']
    print('Vocab CL')
    category = input(f'Pick a category from: {categories}')
    flash_card_type = input(f'Which Translation would you like to guess? (b) for Bahasa, (e) for English')

    cards = vocab[vocab['category'] == category]
    print(f'Your category is: {category}, Flash Card is: {flash_card_type}. Total Number of cards is: {len(cards)}')

    if flash_card_type == 'b':
        card_dict = cards.drop_duplicates(subset='english equivalent', keep='first').set_index('english equivalent').to_dict(orient='index')
    else:
        card_dict = cards.drop_duplicates(subset='bahasa', keep='first').set_index('bahasa').to_dict(orient='index')
    flash_card_type_map = {'b': 'bahasa', 'e': 'english equivalent'}

    unqiue_cards = list(card_dict.keys())
    shuffle(unqiue_cards)
    remaining_cards = unqiue_cards
    while len(remaining_cards) > 0:
        print(f"You have {len(remaining_cards)} to complete.")
        remaining_cards = play_flash_card_game(card_dict, remaining_cards, flash_card_type_map[flash_card_type])
    print("You Finished! Have a beer.")



run()
