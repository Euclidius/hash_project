from math import floor, sin
from kollatc import kollatc


def choose_function(index:int):
    if index == 0:
        return first_function
    elif index == 1:
        return second_function
    elif index == 2:
        return third_function
    elif index == 3:
        return fourth_function
    else:
        raise ValueError('The value must be in range 0-3')


'''
length of all functions must be 8
'''

#(A -> (-B & -A))
def first_function(first_string:str, second_string:str) -> str:
    result = ''
    first_string = str(first_string)
    second_string = str(second_string)
    for i in range(len(str(first_string))):
        result += str(implement((int(first_string[i])), not_bitwise(int(first_string[i])) & not_bitwise(int(second_string[i]))))
    return result


#(-A xor B) -> B * A
def second_function(first_string:str, second_string:str) -> str:
    result = ''
    first_string = str(first_string)
    second_string = str(second_string)    
    for i in range(len(str(first_string))):
        result += str(implement((not_bitwise(int(first_string[i])) ^ int(second_string[i])), (int(second_string[i]) & int(first_string[i]))))
    return result

#-A xor B
def third_function(first_string:str, second_string:str) -> str:
    result = ''
    first_string = str(first_string)
    second_string = str(second_string)
    for i in range(len(str(first_string))):
        result += str(not_bitwise(int(first_string[i])) ^ int(second_string[i]))
    return result


#(A -> B) xor (-A + -B)
def fourth_function(first_string:str, second_string:str) -> str:
    result = ''
    first_string = str(first_string)
    second_string = str(second_string)
    for i in range(len(str(first_string))):
        result += str((implement(int(first_string[i]), int(second_string[i])) ^ not_bitwise(int(first_string[i])) | not_bitwise(int(second_string[i]))))
    return result


def implement(first_bit:int, second_bit:int) -> int:
    if not (isinstance(first_bit, int) and isinstance(second_bit, int)):
        raise ValueError("Arguments must be integer")
    if first_bit == 0:
        return 1
    elif first_bit == 1 and second_bit == 1:
        return 1
    else:
        return 0

def not_bitwise(bit:int) -> int:
    if bit == 1:
        return 0
    elif bit == 0:
        return 1
    else:
        raise ValueError("Argument must be 1 or 0")


def spin(phrase:str, number_of_cycle:int) -> str:
    
    if number_of_cycle % 3 == 0:
        deg = (kollatc(phrase) + number_of_cycle) % 37
    if number_of_cycle % 3 == 1:
        deg = (kollatc(phrase) - number_of_cycle) % 37
    if number_of_cycle % 3 == 2:
            deg = (kollatc(phrase) * number_of_cycle) % 37
        
    shift = floor(abs(sin(number_of_cycle) * 2 ** deg))
    shift = shift % len(phrase)
    return (phrase[shift:] + phrase[:shift]).strip()

    

def main():
    pass

if __name__ == '__main__':
    main()