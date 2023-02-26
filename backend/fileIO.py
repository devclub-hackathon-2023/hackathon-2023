import json
import uuid
USER_DIRECTORY = './users/'

#user will be user{username: "", pass: ""}
def create_file(user: json) -> json:
    userDict = json.loads(user)
    userDict["userID"] = str(uuid.uuid4())
    user = json.dumps(userDict)
    file = open(USER_DIRECTORY + userDict['username'] + '.json', 'w')
    file.write(user)
    file.close()
    return user       
#end of write_file

def read_file(user: json) -> json:
    userDict = json.loads(user)
    try:
        file = open(USER_DIRECTORY + userDict['username'] + '.json', 'r')
        usersFile = file.read()
        file.close()
        return usersFile
    except FileNotFoundError:
        return -1
#end of read_file
