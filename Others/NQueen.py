
global N
N = 4

table = [[0, 1, 1, 0], 
         [1, 0, 0, 1],
         [0, 0, 0, 0], 
         [0, 0, 0, 0]]


def print_table(table):
    for i in range(N):
        for j in range(N):
            print(table[i][j], end='')


def horizontal_collision(table, lin, col):
    if (table[lin][col] == 0):
        return 0
    
    collision_count = table[lin].count(1) - 1

    return max(0, collision_count)


def vertical_collision(table, lin, col):
    if (table[lin][col] == 0):
        return 0

    column = [table[x][col] for x in range(N)]
    collision_count = column.count(1) - 1
    return max(0, collision_count)


def diagonal_collision(table, lin, col):
    if (table[lin][col] == 0):
        return 0

    micl = min(lin, col)

    diag1 = [table[lin + min(N - lin - 1, col) - x][col - min(N-lin-1, col) + x]
             for x in range(N - abs((N - lin - 1) - col))]

    collisions_1 = max(0, diag1.count(1) - 1)


    diag2 = [table[lin - micl + x][col - micl + x]
             for x in range(N - abs(lin - col))]
    
    collisions_2 = max(0, diag2.count(1) - 1)

    #print(str(diag1) + "  " + str(diag2))
    return collisions_1 + collisions_2


def collision_count(table):
    total = 0
    for i in range(N):
        for j in range(N):
            total = total + \
                    max(0, vertical_collision(table, i, j)) + \
                    max(0, horizontal_collision(table, i, j)) +\
                    max(0, diagonal_collision(table, i, j))
    return total / 2


print(collision_count(table))
