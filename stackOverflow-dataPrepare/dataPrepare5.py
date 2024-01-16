train = open('trainData.txt', 'w',encoding='utf-8')
import re
CLEANR = re.compile('<.*?>')
qna = 'Q&A.txt'
i=0
with open(qna, 'r', encoding='utf-8') as q:
    for line in q:
        q_line = line.split('\t')
        question = q_line[1]
        answer = q_line[2]
        cleanQuestion = re.sub(CLEANR, '', question)
        cleanAnswer = re.sub(CLEANR, '', answer)
        train.write('[Q] ' + cleanQuestion + '\n')
        train.write('[A] ' + cleanAnswer + '\n')
        i+=1
        if i % 10_000 == 0:
            print(i)
print(i)
train.close()

