import random as r
import msvcrt as m
import os

# To start press w or a or s or d
# Exit --> another button
# monkey is from France

# map size
map_x = r.randint(15, 20)
map_y = r.randint(20, 30)
# monkey cords
x = r.randint(1, map_x)
y = r.randint(1, map_y)
# croissant cords
banana_x = r.randint(1, map_x - 1)
banana_y = r.randint(1, map_y - 1)
# score flag
count = 0
# crocodile cords
x_cro = r.randint(1, map_x)
y_cro = r.randint(1, map_y)
# crocodile logic by Rova
def cro_step(x_cro,y_cro):
    choice = 'xy'
    step_choice = r.choice(choice)
    if step_choice == 'x':
        if x >= x_cro and x_cro != map_x :
            x_cro += 1
            return x_cro,y_cro
        elif x < x_cro and x_cro != 0:
            x_cro -= 1
            return x_cro,y_cro
        else:
            return x_cro,y_cro
    elif step_choice == 'y':
        if y >= y_cro and y_cro != map_y:
            y_cro += 1
            return x_cro,y_cro
        elif y < y_cro and y_cro != 0:
            y_cro -= 1
            return x_cro,y_cro
        else:
            return x_cro, y_cro
# first loop
while True:
    # crocodile final cords
    x_cro = cro_step(x_cro, y_cro)[0]
    y_cro = cro_step(x_cro, y_cro)[1]
    # imported tool to skip Enter button  
    move = m.getch().decode('utf-8')
    # w a s d logic os is calling terminal commands
    if move == 'w':
        os.system('cls')
        x -= 1
    elif move == 'a':
        os.system('cls')
        y -= 1
    elif move == 's':
        os.system('cls')
        x += 1
    elif move == 'd':
        os.system('cls')
        y += 1
    else:
        break
    # second loop
    for i in range(1, map_x + 1):
        for j in range(1, map_y + 1):
                # crocodile position
                if i == x_cro and j == y_cro:
                    print('🐊', end='')
                    continue
                # exiting if
                if x == x_cro and y == y_cro:
                    print('☠️  ☠️  ☠️  ☠️  ☠️  ☠️  ☠️  ☠️  ☠️  ☠️  ☠️  ☠️  ☠️  ☠️  ☠️  ☠️  ☠️  ☠️  ☠️  ☠️')
                    print('☠️  ☠️  ☠️  ☠️  ☠️  ☠️  ☠️    W A S T E D  ☠️  ☠️  ☠️  ☠️  ☠️  ☠️  ☠️  ☠️')
                    print('☠️  ☠️  ☠️  ☠️  ☠️  ☠️  ☠️  ☠️  ☠️  ☠️  ☠️  ☠️  ☠️  ☠️  ☠️  ☠️  ☠️  ☠️  ☠️  ☠️ ')
                    exit()
                # monkey moving logic
                if x == map_x + 1:
                    x = 1
                if y == map_y + 1:
                    y = 1
                if x == 0:
                    x = map_x
                if y == 0:
                    y = map_y
                if i == x and j == y:
                    print('🐒', end='')
                    continue
                # croissant position logic
                if banana_y == y and banana_x == x:
                    banana_x = r.randint(1, map_x - 1)
                    banana_y = r.randint(1, map_y - 1 )
                    count += 1
                # croissant position
                if i == banana_x and j == banana_y:
                    print('🥐', end='')
                # palma generator
                else:
                    print(f'🌴', end='')
        print()
    # score indicator
    print(f'🥐 Croissant_points  {count}')