from matrix_data import rows, cols
from validations import validate_idx, validate_signs, validate_name_length


def init_game(first_player_name, second_player_name, m_size, players):
    sign = input(f"{first_player_name} would you like to play with 'X' or 'O'? \n").upper()
    valid_sign = validate_signs(sign, allowed_signs='XO')
    print('This is the numeration of the board:')
    print_matrix(create_numbered_matrix(m_size))
    print(f'{first_player_name} starts first.')
    players[first_player_name] = 'X' if valid_sign == 'X' else 'O'
    players[second_player_name] = 'O' if players[first_player_name] == 'X' else 'X'


def get_players_names():
    first_player_name = validate_name_length(input('First player name: '))
    second_player_name = validate_name_length(input('Second player name: '))
    while first_player_name == second_player_name:
        second_player_name = validate_name_length(input('Names cannot be the same. Please choose another one: '))
    return first_player_name, second_player_name


def get_r_c(num):
    row = [rows[n] for n in rows if num in n][0]
    col = [cols[n] for n in cols if num in n][0]
    return row, col


def print_matrix(mx):
    [print(*row) for row in mx]


def place_player_choice(mx, pl_choice, sign):
    row, col = get_r_c(pl_choice)
    mx[row][col] = f'| {sign} |'


def vertical_line(mx, m_size, row, col, sign):
    left_right_direct = [validate_idx(mx, m_size, row + i, col, sign) for i in range(m_size)].count(True)
    right_left_direct = [validate_idx(mx, m_size, row - i, col, sign) for i in range(1, m_size + 1)].count(True)
    return left_right_direct + right_left_direct == m_size


def horizontal_line(mx, m_size, row, col, sign):
    up = [validate_idx(mx, m_size, row, col + i, sign) for i in range(m_size)].count(True)
    down = [validate_idx(mx, m_size, row, col - i, sign) for i in range(1, m_size + 1)].count(True)
    return up + down == m_size


def primary_diagonal(mx, m_size, row, col, sign):
    left_up_right_down = [validate_idx(mx, m_size, row + i, col + i, sign) for i in range(m_size)].count(True)
    right_down_left_up = [validate_idx(mx, m_size, row - i, col - i, sign) for i in range(1, m_size + 1)].count(True)
    return left_up_right_down + right_down_left_up == m_size


def secondary_diagonal(mx, m_size, row, col, sign):
    right_up_left_down = [validate_idx(mx, m_size, row + i, col - i, sign) for i in range(m_size)].count(True)
    left_down_right_up = [validate_idx(mx, m_size, row - i, col + i, sign) for i in range(1, m_size + 1)].count(True)
    return right_up_left_down + left_down_right_up == m_size


def check_result(mx, m_size, row, col, sign):
    is_vertical = vertical_line(mx, m_size, row, col, sign)
    is_horizontal = horizontal_line(mx, m_size, row, col, sign)
    is_primary_diagonal = primary_diagonal(mx, m_size, row, col, sign)
    is_secondary_diagonal = secondary_diagonal(mx, m_size, row, col, sign)
    if any([is_vertical, is_horizontal, is_primary_diagonal, is_secondary_diagonal]):
        return True


def create_numbered_matrix(m_size):
    num_matrix = []
    count = 1
    for row in range(m_size):
        current_row = []
        for col in range(m_size):
            current_row.append(f'| {count} |')
            count += 1
        num_matrix.append(current_row)
    return num_matrix


def create_empty_matrix(m_size):
    mx = []
    for _ in range(m_size):
        mx.append([f'|   |' for n in range(1, m_size + 1)])
    return mx


def get_players_score(score_dict: {}):
    result = ['Current score: ']
    for player, score in score_dict.items():
        result.append(f'{player}: {score}')
    return '\n'.join(result)


def check_for_draw(mx, m_size):
    full_rows = []
    for row_idx in range(m_size):
        possible_squares = ['| X |', '| O |']
        row_count = [True for n in mx[row_idx] if n in possible_squares].count(True)
        full_rows.append(row_count == m_size)
    return full_rows.count(True) == m_size


def suggest_another_game():
    print('Would you care for another round? If so, type Y or N to exit: ')
    response = input().upper()
    valid_resp = validate_signs(response, allowed_signs='YN')
    while not valid_resp:
        print('Incorrect response. Please try again.')
    return response == 'Y'
