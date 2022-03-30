from bin_find import bin_find
from logic_funcs import choose_function, spin
from square import result_square
from s_blocks import first_s_block, second_s_block

counter = 0

"""
ONLY USING UTF-8
"""

for _ in range(64):
    
    input_str = ['0'] * 64
    input_str[counter] = '1'
    input_str = ''.join(input_str)
    '''
    input_str = str(bin(counter)[2:]).zfill(64)
    '''
    with open('input.txt', 'w', encoding = 'utf-8') as f:
        f.write(input_str)
    
    print(counter)
    
    #size of block in bytes
    block_size_r = 8

    #opens and writes all blocks
    with open('input.txt', encoding = 'utf-8') as f:
        raw_list = f.readlines()

    raw_list = [i.rstrip('\n') for i in raw_list]
    raw_string = ''.join(raw_list)

    #plain text but blocks
    raw_blocks = []
    for i in range(0, len(raw_string), block_size_r):
        raw_blocks.append(raw_string[i:i + block_size_r])

    #the paddock
    if len(raw_blocks[-1]) != block_size_r:
        raw_blocks[-1] += ('1' + '0' * (block_size_r-len(raw_blocks[-1]) - 1))
    raw_blocks.append(str(len(raw_string)))
    raw_blocks[-1] += ('1' + '0' * (block_size_r - len(raw_blocks[-1]) - 1))

    raw_bin_blocks = []

    for i in range(len(raw_blocks)):
        res = ''
        for j in range(len(raw_blocks[i])):
            res += bin(ord(raw_blocks[i][j]))[2:].zfill(8)
        raw_bin_blocks.append(res)

    #!THIS WAS A CLEAR PART OF A CODE

    condition_string = list('0' * 64)
    for cycle_num in range(len(raw_bin_blocks)):
        if cycle_num % 3 == 0:
            condition_string = condition_string[::-1]
        
        condition_string = ''.join(condition_string)
        condition_string = spin(condition_string, cycle_num)
        reference_index = bin_find(raw_bin_blocks[cycle_num], cycle_num)
        logic_function = choose_function(reference_index)

        condition_string = first_s_block(reference_index, condition_string)
        condition_string = result_square(condition_string, logic_function)
        condition_string = second_s_block(reference_index, condition_string)

        condition_string = list(condition_string)
        for position in range(len(raw_bin_blocks[cycle_num])):
            condition_string[position] = str(int(condition_string[position]) ^ int(raw_bin_blocks[cycle_num][position]))

    with open('output.txt', 'a') as f:
        f.write(''.join(condition_string))
        f.write('\n')
        

    counter += 1


    #print(''.join(condition_string))