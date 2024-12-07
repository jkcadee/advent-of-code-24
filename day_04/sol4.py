input_matrix = []

def read_txt() -> None:
    file = open("day_04/p4_input.txt", "r")
    num_list = file.readlines()
    for v in num_list:
        line = v.split()
        ln = []
        for l in line:
            for character in l:
                ln.append(character)
        input_matrix.append(ln)

    file.close()

def coord_valid(x, y, size_x, size_y):
    return 0 <= x < size_x and 0 <= y < size_y

def find_word_in_direction(grid, length, height, word, index, x, y, dir_X, dir_Y):
    if index == len(word):
        return True

    if coord_valid(x, y, length, height) and word[index] == grid[x][y]:
        return find_word_in_direction(grid, length, height, word, index + 1, x + dir_X, y + dir_Y, dir_X, dir_Y)
    
    return False

def solution_part1():
    found_word = 0
    word = "XMAS"
    length = len(input_matrix)
    height = len(input_matrix[0])

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    for i in range(length):
        for j in range(height):
            if input_matrix[i][j] == word[0]:
                for dir_X, dir_Y in directions:
                    if find_word_in_direction(input_matrix, length, height, word, 0, i, j, dir_X, dir_Y):
                        found_word += 1
    
    return found_word

def solution_part2():
    found_word = 0


def main():
    read_txt()
    print(solution_part1())
    #print(solution_part2(p_string))
    
if __name__ == "__main__":
    main()