import ast
quest = 'posts.txt'
ans = 'sort_answers.txt'
qwa = open('questionsWithAnswers.txt', 'w', encoding='utf-8')
qacc = open('questionsWithAccept.txt', 'w', encoding='utf-8')
qna = open('questionsNoAnswer.txt', 'w', encoding='utf-8')
i=0
na = 0
wa = 0
acc = 0
with open(quest, 'r', encoding='utf-8') as q, open(ans, 'r', encoding='utf-8') as a:
    q_line = q.readline().split('\t')
    a_line = a.readline().split('\t')
    prev_a_id=0
    while True:
        if not q_line or len(q_line)!=5:
            print('Koniec odpowiedzi')
            break
        q_id = int(q_line[0])
        accept_answer = int(q_line[1])
        answer_count = int(q_line[2])
        question = q_line[4].replace('\n','')
        i+=1
        if answer_count == 0:
            na+=1
            qna.write(str(q_id)+'\t'+question)
            q_line = q.readline().split('\t')
        else:
            tempScore=0
            tempAnswer=''
            while True:
                if not a_line or len(a_line)!=5:
                    print('Koniec odpowiedzi')
                    break
                aParent_id = int(a_line[0])
                a_id = int(a_line[1])
                if q_id == aParent_id:
                    score = int(a_line[2])
                    answer = a_line[4]
                    wa+=1
                    qwa.write(str(q_id) + '\t' + str(score) + '\t' + question + '\t' + answer)
                    if accept_answer == a_id:
                        acc+=1
                        qacc.write(str(q_id) + '\t' + question + '\t' + answer)
                    a_line = a.readline().split('\t')
                elif q_id > aParent_id:
                    a_line = a.readline().split('\t')
                else:
                    q_line = q.readline().split('\t')
                    break
            if not a_line or len(a_line)!=5:
                print('Koniec odpowiedzi')
                break
        if i % 10_000 == 0:
            print(i,'- z odpowiedzia:',wa,'w tym accepted(',acc,'), bez odpowiedzi:',na)
qna.close()
qwa.close()
qacc.close()

