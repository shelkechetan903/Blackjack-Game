import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    score = sum(cards)
    ace_count = cards.count(11)
    
    while score > 21 and ace_count > 0:
        score -= 10
        ace_count -= 1
        
    return score

def compare(u_score, c_score):
    if u_score == c_score:
        return "\nDraw !"
    elif u_score == 0:
        return "\nWin with Blackjack !"
    elif c_score == 0:
        return "\nLose, opponent has Blackjack !"
    elif u_score > 21:
        return "\nYou went over. You lose !"
    elif c_score > 21:
        return "\nOpponent went over. You win !"
    elif u_score > c_score:
        return "\nYou win !"
    else: 
        return "\nYou lose !"

def play_game():
    user_card = []
    comp_card = []
    is_game_over = False

    for i in range(2):
        user_card.append(deal_card())
        comp_card.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_card)
        comp_score = calculate_score(comp_card)
        print(f"\nYour cards: {user_card}, current score: {user_score}")
        print(f"Computer's first card: {comp_card[0]}")

        if user_score == 0 or comp_score == 0 or user_score > 21:
            is_game_over = True
        else:
            add_card = input("Type 'y' to get another card, 'n' to pass: ").lower()
            if add_card == 'y':
                user_card.append(deal_card())
            else:
                is_game_over = True

    while comp_score != 0 and comp_score < 17:
        comp_card.append(deal_card())
        comp_score = calculate_score(comp_card)    

    print(f"\nYour final hand: {user_card}, final score: {user_score}")
    print(f"Computer's final hand: {comp_card}, final score: {comp_score}")
    print(compare(u_score=user_score, c_score=comp_score))

while input("\nDo you want to play a game of Blackjack? Type 'y' for yes or 'n' for no: ").lower() == 'y':
    play_game()