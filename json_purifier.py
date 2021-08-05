import json

def get_user_id(length, user, from_key):
    for i in range(1, length):
        if from_key in jsondict['messages'][i]:
            if jsondict['messages'][i]['from'].lower() == user:
                user_id = jsondict['messages'][i]['from_id']
                return user_id
                break
            else:
                continue

user = input("Enter telegram Username: ").lower()

with open("result.json", 'r') as tgm_json:
    jsondict = json.load(tgm_json)
    tgm_json.close()

length = len(jsondict['messages'])

from_key = 'from'

user_id = get_user_id(length, user, from_key)

messages = []
key = 'from_id'

for i in range(1, length):
        if key in jsondict['messages'][i]:         
            from_id = jsondict['messages'][i]['from_id'] 
            if from_id == user_id:
                message_text = jsondict['messages'][i]['text']
                if type(message_text) == list:
                    continue
                else:
                    messages.append(message_text)
if len(messages) != 0:
    print("User messages found.")
    with open("messages.txt", "w") as f:
        for message in messages:
            if message == "":
                continue
            else:
                f.write(str(message) + "\n")
else:
    print("That's not a real user, stop it.")
    exit()

