from math import log

def bin_find(bin_str:str, round_of_cycle:int) -> int:
    '''
    Function gets a binary string with lenght 2 ^ k and returns a position of some element 
    (what we choose by counting 1 and 0) mod 4.
    '''
    #list of bin results
    border_mean = []

    for _ in range(round(log(len(bin_str), 2))):
        left = bin_str[:len(bin_str)//2]
        right = bin_str[len(bin_str)//2:]

        left_ones = left.count('1')
        right_ones = right.count('1')

        if (left_ones > right_ones):
            bin_str = left
            border_mean.append('left')
        elif (right_ones > left_ones):
            bin_str = right
            border_mean.append('right')
        elif (int(round_of_cycle) % 2 == 0):
            bin_str = left
            border_mean.append('left')
        else:
            bin_str = right
            border_mean.append('right')
        
    index = 1
    for i in range(len(border_mean)):
        if border_mean[i] == 'right':
            index += 2 ** (len(border_mean) - i - 1)
    
    return (index  % 4)


def main():
    bin_str = input('The binary string: ')
    round_of_cycle = input('The round of cycle: ')

    print(bin_find(bin_str, round_of_cycle))


if __name__ == '__main__':
    main()
