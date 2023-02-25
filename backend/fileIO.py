import json

#user will be user{username: "", pass: ""}
def create_file(user: json):
    userDict = json.loads(user)
    file = open(userDict['username'] + '.json', 'w')
    file.write(user)
    file.close()       
#end of write_file

def read_file(user: json) -> json:
    userDict = json.loads(user)
    try:
        file = open(userDict['username'] + '.json', 'r')
        usersFile = file.read()
        file.close()
        return usersFile
    except FileNotFoundError:
        return -1
#end of read_file

john = {"username": "John", "pass": "ILikePasswords"}

create_file(json.dumps(john))
print(read_file(json.dumps(john)))