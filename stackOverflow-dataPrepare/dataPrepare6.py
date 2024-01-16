data_path = 'trainData.txt'
every = 0
file = 0
with open(data_path, 'r', encoding='utf-8') as data:
    line = data.readline()
    while line:
        file += 1
        train_path='./files/train'+str(file)+'.txt'
        train = open(train_path, 'w', encoding='utf-8')
        for i in range(2000):
            if line:
                every += 1
                train.write(line)
                line = data.readline()
            else:
                break
        print(every)
        train.close()
