n = int(input())
trains = []

for i in range(n):
    inp = input()
    lis = inp.split()
    train_name = lis[0]
    destination = lis[4]
    departure_time = lis[6]
    
    hours, minutes = map(int, departure_time.split(':'))
    trains.append((train_name, (hours, minutes), inp))

for i in range(len(trains)):
    for j in range(len(trains) - i - 1):
        if trains[j][0] > trains[j + 1][0] or (
            trains[j][0] == trains[j + 1][0] and trains[j][1] < trains[j + 1][1]
        ):
            trains[j], trains[j + 1] = trains[j + 1], trains[j]

for train in trains:
    print(train[2])
