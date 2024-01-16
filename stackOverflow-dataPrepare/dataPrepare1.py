import xml.etree.ElementTree as ET

POST_FILE = 'E:/stackoverflow-Posts/Posts.xml'

posts = open('post1.txt', 'w',encoding='utf-8')
postsids = open('postids.txt', 'w',encoding='utf-8')
comms = open('post2.txt', 'w',encoding='utf-8')

with open(POST_FILE, 'r', encoding='utf-8') as file:
    i=0
    p=0
    c=0
    for line in file:
        try:
            row = ET.fromstring(line.strip())
            if row.attrib['PostTypeId'] == '1':
                tags = row.attrib['Tags']
                if '<java>' in tags:
                    id = row.attrib['Id']
                    posts.write(str(row.attrib))
                    posts.write('\n')
                    postsids.write(str(id)+'\n')
                    p+=1
            elif row.attrib['PostTypeId'] == '2':
                comms.write(str(row.attrib))
                comms.write('\n')
                c+=1
            i+=1
            if i %100_000==0:
                print (i,'{ posts: ',p,", comms: ",c," }")
        except ET.ParseError:
            continue
posts.close()
postsids.close()
comms.close()
