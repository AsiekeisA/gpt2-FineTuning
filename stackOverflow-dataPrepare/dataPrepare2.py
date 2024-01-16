import ast
posts = 'post1.txt'
comms = 'post2.txt'
p = open('posts.txt', 'w', encoding='utf-8')
a = open('answers.txt', 'w', encoding='utf-8')

with open(posts, 'r', encoding='utf-8') as file:
    i=0
    for line in file:
        line_object = ast.literal_eval(line)
        if i % 100_000 == 0:
            print('posts: ',i)
        i+=1
        id = line_object.get('Id')
        accept_answer = line_object.get('AcceptedAnswerId')
        if accept_answer == None:
            accept_answer='0'
        body = line_object.get('Body').replace('\n', '').replace('\t', '')
        answ = line_object.get('AnswerCount')
        comm = line_object.get('CommentCount')
        p.write(id+'\t'+accept_answer+'\t'+answ+'\t'+comm+'\t'+body+'\n')
with open(comms, 'r', encoding='utf-8') as file:
    i=0
    for line in file:
        line_object = ast.literal_eval(line)
        type = int(line_object['PostTypeId'])
        if type == 2:
            id = line_object.get('Id')
            parentId = line_object.get('ParentId')
            score = line_object.get('Score')
            body = line_object.get('Body').replace('\n', '')
            comm = line_object.get('CommentCount')
            a.write(parentId+'\t'+id+'\t'+score+'\t'+comm+'\t'+body+'\n')
            i += 1
            if i % 100_000 == 0:
                print('answers: ', i)
p.close()
a.close()

