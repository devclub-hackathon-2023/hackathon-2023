import json

#user will be user{username: "", pass: ""}
def create_file(user: json):
    userDict = json.loads(user)
    file = open(userDict['username'] + '.json', 'x')
    file.write(user)
    file.close()       
#end of write_file

def read_file(user: json):
    userDict = json.loads(user)
    try:
        file = open(userDict)
    except FileNotFoundError:
        pass
#end of read_file

thing = {"username": "John", "pass": "ThisIsMyPassword"}
thing = json.dumps(thing)
create_file(thing)