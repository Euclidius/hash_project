def first_s_block(base:int, phrase:str) -> str:
    s_clusters = []
    for i in range(0, len(phrase), 4):
        result_phrase = ''
        for j in range(4):
            result_phrase += phrase[i + j]
            
        s_clusters.append(result_phrase)
    
    match base:
        case 1:
            for i in range(len(s_clusters)):
                match s_clusters[i]:
                    case '0000':
                        s_clusters[i] = '0111'
                    case '0001':
                        s_clusters[i] = '1101'
                    case '0010':
                        s_clusters[i] = '1110'
                    case '0011':
                        s_clusters[i] = '0100'
                    case '0100':
                        s_clusters[i] = '0000'
                    case '0101':
                        s_clusters[i] = '0110'
                    case '0110':
                        s_clusters[i] = '1001'
                    case '0111':
                        s_clusters[i] = '1010'
                    case '1000':
                        s_clusters[i] = '0001'
                    case '1001':
                        s_clusters[i] = '0010'
                    case '1010':
                        s_clusters[i] = '1000'
                    case '1011':
                        s_clusters[i] = '0101'
                    case '1100':
                        s_clusters[i] = '1011'
                    case '1101':
                        s_clusters[i] = '1100'
                    case '1110':
                        s_clusters[i] = '0100'
                    case '1111':
                        s_clusters[i] = '1111'

        case 2:
            for i in range(len(s_clusters)):
                match s_clusters[i]:
                    case '0000':
                        s_clusters[i] = '1101'
                    case '0001':
                        s_clusters[i] = '1000'
                    case '0010':
                        s_clusters[i] = '1011'
                    case '0011':
                        s_clusters[i] = '0101'
                    case '0100':
                        s_clusters[i] = '0110'
                    case '0101':
                        s_clusters[i] = '1111'
                    case '0110':
                        s_clusters[i] = '0000'
                    case '0111':
                        s_clusters[i] = '0011'
                    case '1000':
                        s_clusters[i] = '0100'
                    case '1001':
                        s_clusters[i] = '0111'
                    case '1010':
                        s_clusters[i] = '0010'
                    case '1011':
                        s_clusters[i] = '1100'
                    case '1100':
                        s_clusters[i] = '0001'
                    case '1101':
                        s_clusters[i] = '1010'
                    case '1110':
                        s_clusters[i] = '1110'
                    case '1111':
                        s_clusters[i] = '1001'

        case 3:
            for i in range(len(s_clusters)):
                match s_clusters[i]:
                    case '0000':
                        s_clusters[i] = '1010'
                    case '0001':
                        s_clusters[i] = '0110'
                    case '0010':
                        s_clusters[i] = '1001'
                    case '0011':
                        s_clusters[i] = '0000'
                    case '0100':
                        s_clusters[i] = '1100'
                    case '0101':
                        s_clusters[i] = '1011'
                    case '0110':
                        s_clusters[i] = '0111'
                    case '0111':
                        s_clusters[i] = '1101'
                    case '1000':
                        s_clusters[i] = '1111'
                    case '1001':
                        s_clusters[i] = '0001'
                    case '1010':
                        s_clusters[i] = '0011'
                    case '1011':
                        s_clusters[i] = '1110'
                    case '1100':
                        s_clusters[i] = '0101'
                    case '1101':
                        s_clusters[i] = '0010'
                    case '1110':
                        s_clusters[i] = '1000'
                    case '1111':
                        s_clusters[i] = '0100'

        case 4:
            for i in range(len(s_clusters)):
                match s_clusters[i]:
                    case '0000':
                        s_clusters[i] = '0011'
                    case '0001':
                        s_clusters[i] = '1111'
                    case '0010':
                        s_clusters[i] = '0000'
                    case '0011':
                        s_clusters[i] = '0110'
                    case '0100':
                        s_clusters[i] = '1010'
                    case '0101':
                        s_clusters[i] = '0001'
                    case '0110':
                        s_clusters[i] = '1101'
                    case '0111':
                        s_clusters[i] = '1000'
                    case '1000':
                        s_clusters[i] = '1001'
                    case '1001':
                        s_clusters[i] = '0100'
                    case '1010':
                        s_clusters[i] = '0101'
                    case '1011':
                        s_clusters[i] = '1011'
                    case '1100':
                        s_clusters[i] = '1010'
                    case '1101':
                        s_clusters[i] = '0111'
                    case '1110':
                        s_clusters[i] = '0010'
                    case '1111':
                        s_clusters[i] = '1110'

    return ''.join(s_clusters)

def second_s_block(base:int, phrase:str) -> str:
    s_clusters = []
    for i in range(0, len(phrase), 4):
        result_phrase = ''
        for j in range(4):
            result_phrase += phrase[i + j]
            
        s_clusters.append(result_phrase)

    match base:
        case 1:
            for i in range(len(s_clusters)):
                match s_clusters[i]:
                    case '0000':
                        s_clusters[i] = '0100'
                    case '0001':
                        s_clusters[i] = '1011'
                    case '0010':
                        s_clusters[i] = '0010'
                    case '0011':
                        s_clusters[i] = '1110'
                    case '0100':
                        s_clusters[i] = '1111'
                    case '0101':
                        s_clusters[i] = '0000'
                    case '0110':
                        s_clusters[i] = '1000'
                    case '0111':
                        s_clusters[i] = '1101'
                    case '1000':
                        s_clusters[i] = '0011'
                    case '1001':
                        s_clusters[i] = '1100'
                    case '1010':
                        s_clusters[i] = '1001'
                    case '1011':
                        s_clusters[i] = '0111'
                    case '1100':
                        s_clusters[i] = '0101'
                    case '1101':
                        s_clusters[i] = '1010'
                    case '1110':
                        s_clusters[i] = '0110'
                    case '1111':
                        s_clusters[i] = '0001'

        case 2:
            for i in range(len(s_clusters)):
                match s_clusters[i]:
                    case '0000':
                        s_clusters[i] = '1101'
                    case '0001':
                        s_clusters[i] = '0000'
                    case '0010':
                        s_clusters[i] = '1011'
                    case '0011':
                        s_clusters[i] = '0111'
                    case '0100':
                        s_clusters[i] = '0100'
                    case '0101':
                        s_clusters[i] = '1001'
                    case '0110':
                        s_clusters[i] = '0001'
                    case '0111':
                        s_clusters[i] = '1010'
                    case '1000':
                        s_clusters[i] = '1110'
                    case '1001':
                        s_clusters[i] = '0011'
                    case '1010':
                        s_clusters[i] = '0101'
                    case '1011':
                        s_clusters[i] = '1100'
                    case '1100':
                        s_clusters[i] = '0010'
                    case '1101':
                        s_clusters[i] = '1111'
                    case '1110':
                        s_clusters[i] = '1000'
                    case '1111':
                        s_clusters[i] = '0110'

        case 3:
            for i in range(len(s_clusters)):
                match s_clusters[i]:
                    case '0000':
                        s_clusters[i] = '0001'
                    case '0001':
                        s_clusters[i] = '0100'
                    case '0010':
                        s_clusters[i] = '1011'
                    case '0011':
                        s_clusters[i] = '1101'
                    case '0100':
                        s_clusters[i] = '1100'
                    case '0101':
                        s_clusters[i] = '0011'
                    case '0110':
                        s_clusters[i] = '0111'
                    case '0111':
                        s_clusters[i] = '1110'
                    case '1000':
                        s_clusters[i] = '1010'
                    case '1001':
                        s_clusters[i] = '1111'
                    case '1010':
                        s_clusters[i] = '0110'
                    case '1011':
                        s_clusters[i] = '1000'
                    case '1100':
                        s_clusters[i] = '0000'
                    case '1101':
                        s_clusters[i] = '0101'
                    case '1110':
                        s_clusters[i] = '1001'
                    case '1111':
                        s_clusters[i] = '0010'
                    
        case 4:
            for i in range(len(s_clusters)):
                match s_clusters[i]:
                    case '0000':
                        s_clusters[i] = '0110'
                    case '0001':
                        s_clusters[i] = '1011'
                    case '0010':
                        s_clusters[i] = '1101'
                    case '0011':
                        s_clusters[i] = '1000'
                    case '0100':
                        s_clusters[i] = '0001'
                    case '0101':
                        s_clusters[i] = '0100'
                    case '0110':
                        s_clusters[i] = '1100'
                    case '0111':
                        s_clusters[i] = '0111'
                    case '1000':
                        s_clusters[i] = '1001'
                    case '1001':
                        s_clusters[i] = '0101'
                    case '1010':
                        s_clusters[i] = '0000'
                    case '1011':
                        s_clusters[i] = '1111'
                    case '1100':
                        s_clusters[i] = '1110'
                    case '1101':
                        s_clusters[i] = '0010'
                    case '1110':
                        s_clusters[i] = '0011'
                    case '1111':
                        s_clusters[i] = '1100'
    return ''.join(s_clusters)
def main():
    print(first_s_block(2, '1010110100100101011010001100011111111010010000100000101101110111'))
    print(second_s_block(2, '1010110100100101011010001100011111111010010000100000101101110111'))

if __name__ == '__main__':
    main()