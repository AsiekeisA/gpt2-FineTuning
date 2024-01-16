import ast
qwa = 'questionsWithAnswers.txt'
qacc = 'questionsWithAccept.txt'
qna = open('Q&A.txt', 'w', encoding='utf-8')
i=0
na = 0
wa = 0
acc = 0
with open(qwa, 'r', encoding='utf-8') as q, open(qacc, 'r', encoding='utf-8') as a:
    a_line = a.readline().split('\t')
    a_id = a_line[0]
    last_accept = 0
    prev_id = 0
    prev_score = 0
    prev_q = ''
    prev_a = ''
    for line in q:
        q_line = line.split('\t')
        q_id = int(q_line[0])
        score = int(q_line[1])
        question = q_line[2]
        answer = q_line[3]
        if prev_id != q_id and prev_id != 0:
            qna.write(str(prev_id) + '\t' + prev_q + '\t' + prev_a)
            i+=1
        if last_accept != q_id:
            if q_id == a_id:
                last_accept = a_id
                prev_id = a_id
                prev_q = a_line[1]
                prev_a = a_line[2]
                a_line = a.readline().split('\t')
                if len(a_line) == 3:
                    a_id = a_line[0]
                else:
                    a_id = 0
            else:
                if prev_id == q_id:
                    if prev_score < score :
                        prev_score = score
                        prev_q = question
                        prev_a = answer
                else:
                    prev_id = q_id
                    prev_score = score
                    prev_q = question
                    prev_a = answer
        if i % 10_000 == 0:
            print(i)
    qna.write(str(prev_id) + '\t' + prev_q + '\t' + prev_a)
    i+=1
print(i)
qna.close()

