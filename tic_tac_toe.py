
ls = [['-','-','-'],['-','-','-'],['-','-','-']]
print('lets play tictactoe')
circle_player = input('who is playing circles? ')
cross_player = input('who is playing crosses? ')
print('ok {} and {}, lets begin!'.format(circle_player, cross_player))
game_finished = 'n'
while True:
    for i in ls:
        print(i)
    circle_x = int(input('{}, where on x-axis? '.format(circle_player))) - 1
    circle_y = int(input('{}, where on Y-axis? '.format(circle_player))) - 1
    ls[circle_y][circle_x] = 'o'
    for i in ls:
        print(i)
    game_finished_circle = input('did you win? Y/N ')
    if game_finished_circle.upper() == 'Y':
        print('{} wins!'.format(circle_player))
        break
    cross_x = int(input('{}, where on x-axis? '.format(cross_player))) - 1
    cross_y = int(input('{}, where on Y-axis? '.format(cross_player))) - 1
    ls[cross_y][cross_x] = 'x'
    for i in ls:
        print(i)
    game_finished_cross = input('did you win? Y/N ')
    if game_finished_cross.upper() == 'Y':
        print('{} wins!'.format(cross_player))
        break





