user_prompt = "enter a new member: \n"
new_member = input(user_prompt).strip()

file = open("files/members.txt", "r")
content = file.readlines()
file.close()

content.append(new_member+"\n")
file = open("files/members.txt", "w")
file.writelines(content)
file.close()

filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for filename in filenames:
    file = open(f"files/{filename}", "w")
    file.writelines("Hello")
    file.close()

filenames = ['a.txt', 'b.txt', 'c.txt']

for filename in filenames:
    file = open(f"files/{filename}", "r")
    content = file.read()
    print(content)
    file.close()
