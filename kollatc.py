def kollatc(bin_str: str) -> int:
    int_input = int(bin_str, base = 2)
    counter = 0
    
    if int_input == 0:
        return 0

    if int_input == 1:
        return 1
        
    while int_input != 1:
        if int_input % 2 == 0:
            counter += 1
            int_input = int_input // 2
        else:
            counter += 1
            int_input = int_input * 3 + 1

    return counter

def main():
    input_str = '0111000001101111011101000110100001100001001001110110010001100110'
    print(kollatc(input_str))

if __name__ == '__main__':
    main()