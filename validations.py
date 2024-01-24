def validate_name_length(name: str):
    while len(name.strip()) == 0:
        name = input('Name should be at least one character long. Please enter another one: ')
        continue
    return name


def validate_player_choice(pl_choice, m_size, mx):
    current_choice = pl_choice
    while True:
        if not current_choice.isdigit():
            current_choice = input('That wasn\'t a number. Please give it another try: ')
            continue

        n = int(current_choice)
        if n <= 0 or n > m_size ** 2:
            current_choice = input('The number is out of boundaries. Please give it another try: ')
            continue

        from game_functions import get_r_c
        row, col = get_r_c(n)
        if mx[row][col] in ['| X |', '| O |']:
            current_choice = input('That position is already taken. Please choose again')
            continue

        return int(current_choice)


def validate_signs(sign: str, allowed_signs: str):
    while sign not in allowed_signs:
        new_sign = input("Please choose between 'X' and 'O': ")
        sign = validate_signs(new_sign, allowed_signs='XO')
    return sign


def validate_idx(mx, m_size, row, col, sign):
    if row < 0 or col < 0 or row >= m_size or col >= m_size:
        return False
    if mx[row][col] == f'| {sign} |':
        return True
