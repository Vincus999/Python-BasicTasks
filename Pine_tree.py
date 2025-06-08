
# Pine tree

def pine_tree(base_stars):
    rows = (base_stars + 1) // 2

    for i in range(1, rows + 1):
        print(' ' * (rows - i), end='')

        print('*' * (2 * i - 1))


base_stars = 13
pine_tree(base_stars)
