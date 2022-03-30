from math import sqrt, sin, floor
import logic_funcs as lf

'''
This is a module for xor-square and "Polibius" square.
'''

def square(bin_str:str) -> list:
    #lenght of the bin_str must be 8 ^ 2 = 64
    square = [[] for _ in range(round(sqrt(len(bin_str))))]
    counter = 0
    
    for i in range(round(sqrt(len(bin_str)))):
        for j in range(round(sqrt(len(bin_str)))):
            square[i].append(bin_str[counter])
            counter += 1
    
    return square



def result_square(bin_str:list, function) -> str:
    str_square = square(bin_str)
    str_square = logic(str_square, function)
    str_square = polibius(str_square)
    str_square = xor_square(str_square)
    str_square = polibius(str_square)
    str_square = snail(str_square)
    str_square = map(str, str_square)

    return ''.join(str_square)


def logic(square:list, function) -> list:
    start_positions = [[0, 0]]
    while len(start_positions) != 0:
        pair = start_positions[0]
        if pair[0] < 7:
            square[pair[0] + 1][pair[1]] = function(square[pair[0] + 1][pair[1]], square[pair[0]][pair[1]])
            if [pair[0] + 1, pair[1]] not in start_positions:
                start_positions.append([pair[0] + 1, pair[1]])
               
        if pair[1] < 7:
            square[pair[0]][pair[1] + 1] = function(square[pair[0]][pair[1] + 1], square[pair[0]][pair[1]])
            if [pair[0], pair[1] + 1] not in start_positions:
                start_positions.append([pair[0], pair[1] + 1])
            
        start_positions.remove(start_positions[0])

    return square


def xor_square(square:list) -> list:
    for ring_number in range(round(sqrt(len(square)))):
        current_position = [ring_number, ring_number]
        start = [ring_number, ring_number]
        right_top = [ring_number, len(square) - ring_number - 1]
        right_bottom = [len(square) - ring_number - 1, len(square) - ring_number - 1]
        left_bottom = [len(square) - ring_number - 1, ring_number]
        while current_position != [start[0] + 1, start[1]]:
            if current_position[0] == ring_number and [current_position[0], current_position[1]] != right_top:
                square[current_position[0]][current_position[1] + 1] = str(int(square[current_position[0]][current_position[1] + 1]) ^ int(square[current_position[0]][current_position[1]]))
                current_position = [current_position[0], current_position[1] + 1]
                continue

            if current_position[1] == len(square) - ring_number - 1 and [current_position[0], current_position[1]] != right_bottom:
                square[current_position[0] + 1][current_position[1]] = str(int(square[current_position[0] + 1][current_position[1]]) ^ int(square[current_position[0]][current_position[1]]))
                current_position = [current_position[0] + 1, current_position[1]]
                continue

            if current_position[0] == len(square) - ring_number - 1 and [current_position[0], current_position[1]] != left_bottom:
                square[current_position[0]][current_position[1] - 1] = str(int(square[current_position[0]][current_position[1] - 1]) ^ int(square[current_position[0]][current_position[1]]))
                current_position = [current_position[0], current_position[1] - 1]
                continue

            if current_position[1] == ring_number and [current_position[0], current_position[1]] != start:
                square[current_position[0] - 1][current_position[1]] = str(int(square[current_position[0] - 1][current_position[1]]) ^ int(square[current_position[0]][current_position[1]]))
                current_position = [current_position[0] - 1, current_position[1]]
                continue
    return square


def polibius(square:list) -> list:
    for i in range(len(square)):
        if i % 3 == 0:
            deg = 32 + i
        if i % 3 == 1:
            deg = 32 - i
        if i % 3 == 2:
            deg = (32 * i) % 37
        
        if i % 4 == 0:
            shift = floor(abs(sin(square[i].count('11') + 1) * 2 ** deg))
        elif i % 4 == 1:
            shift = floor(abs(sin(square[i].count('00') + 1) * 2 ** deg))
        elif i % 4 == 2:
            shift = floor(abs(sin(square[i].count('10') + 1) * 2 ** deg))
        elif i % 4 == 3:
            shift = floor(abs(sin(square[i].count('01') + 1) * 2 ** deg))

        square[i] = square[i][(-shift % len(square[i])):] + square[i][:(-shift % len(square[i]))]
    return square


def snail(snail_map):
    
    result = []
    while len(snail_map) != 0:
        result += snail_map[0]
        snail_map.remove(snail_map[0])
        if len(snail_map) == 0:
            return result
        for i in range(len(snail_map)):
            result.append(snail_map[i][-1])
            snail_map[i][-1] = None
            snail_map[i].remove(None)
        if len(snail_map) == 0:
            return result
        result += snail_map[-1][::-1]
        snail_map.remove(snail_map[-1])
        if len(snail_map) == 0:
            return result
        for i in range(len(snail_map)):
            result.append(snail_map[len(snail_map) - i - 1][0])
            snail_map[len(snail_map) - i - 1][0] = None
            snail_map[len(snail_map) - i - 1].remove(None)
        
    return result


def main():
    bin_str = '0110101101101101011101110111010001101110101110110101010001101011' #len is 64
    
    for i in range(64):
        bin_str = '0' * 64
        bin_str = list(bin_str)
        bin_str[i] = 1
        print(result_square(bin_str, lf.first_function))

    print()

    for i in range(64):
        bin_str = '0' * 64
        bin_str = list(bin_str)
        bin_str[i] = 1
        print(result_square(bin_str, lf.second_function))

    print()

    for i in range(64):
        bin_str = '0' * 64
        bin_str = list(bin_str)
        bin_str[i] = 1
        print(result_square(bin_str, lf.third_function))

    print()

    for i in range(64):
        bin_str = '0' * 64
        bin_str = list(bin_str)
        bin_str[i] = 1
        print(result_square(bin_str, lf.fourth_function))


if __name__ == '__main__':
    main()