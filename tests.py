with open('output.txt') as f:
    data = f.readlines()


counter = 0

for i in range(1, len(data)):
    for j in range(len(data[i])):
        if data[0][j] != data[i][j]:
            counter += 1

power = counter / 64

print(round(power / 64, 4))