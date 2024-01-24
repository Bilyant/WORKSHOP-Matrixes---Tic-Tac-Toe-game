from game_functions import create_empty_matrix, print_matrix, place_player_choice, get_r_c, check_result, \
    get_players_score, check_for_draw, suggest_another_game, get_players_names, init_game
from validations import validate_player_choice

m_size = 3
matrix = create_empty_matrix(m_size)
game_won = False
turn = 1
first_player_name, second_player_name = get_players_names()

players = {
    first_player_name: 'sign',
    second_player_name: 'sign',
}
players_score = {
    first_player_name: 0,
    second_player_name: 0,
}

init_game(first_player_name, second_player_name, m_size, players)

while not game_won:
    is_draw = False
    player_turn = first_player_name if turn % 2 == 1 else second_player_name
    player_sign = players[player_turn]
    print_matrix(matrix)
    player_choice = input(f'{player_turn} choose a free position [1-9]: ')
    valid_choice = validate_player_choice(player_choice, m_size, matrix)
    place_player_choice(matrix, valid_choice, sign=player_sign)
    row, col = get_r_c(valid_choice)
    is_winner = check_result(mx=matrix, m_size=m_size, row=row, col=col, sign=player_sign)

    if is_winner or check_for_draw(matrix, m_size):
        print_matrix(matrix)
        game_won = True

        if is_winner:
            print(f'Congratulations! {player_turn} won!')
            players_score[player_turn] += 1
        else:
            print(f'It\'s a draw!')
            for player, score in players_score.items():
                players_score[player] += 1

        print(get_players_score(players_score))
        if suggest_another_game():
            game_won = False
            matrix = create_empty_matrix(m_size)
    turn += 1
