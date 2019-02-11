import json
import pprint
import os

def search_users(search_eq, file):
    count = 0
    user_info = [{}]
    funct = search_eq.split('=')
    attr = str(funct[0])
    if attr == 'new':
        attr_val = bool(funct[1])
    else:
        attr_val = str(funct[1])

    for i in range(json_file_len):
        data = file[i]
        if data[attr] == attr_val:
            count += 1
            user_info.append(data)
    
    pprint.pprint(user_info)
    if count > 1:
        print('Total number of entries found: ', count)
    
def create_user(input_dict):
    user = {'id':json_file_len + 1,'first_name':'','last_name':'','email':'','gender':'','ip_address':'','new':''}

    for k,v in input_dict.items():
        user[k] = v
    
    #pprint.pprint(user)
    json_data.append(user)
    open('/home/nick/Desktop/users/MOCK_DATA.json', mode='w').write(json.dumps(json_data, indent=0))

def delete_user(input_dict):
    for k,v in input_dict.items():
        for i in range(json_file_len):
            if json_data[i][k] == v:
                json_data.pop(i)
                break
        open('/home/nick/Desktop/users/MOCK_DATA.json', mode='w').write(json.dumps(json_data, indent=0, separators=(',',':')))

with open('/home/nick/Desktop/users/MOCK_DATA.json', mode='r') as json_file:
    json_str = json_file.read()
    json_data = json.loads(json_str)
    json_file_len = len(json_data)


#Example of function calls.

#search_users('first_name=Moss', json_data)

#new_dict = {
#"id": 1000,
#"first_name": "Flora",
#"last_name": "Kenworthey",
#"email": "fkenwortheyrr@techcrunch.com",
#"gender": "Female",
#"ip_address": "195.21.254.191",
#"new": False
#}

#create_user(new_dict)
#search_users('first_name=Nick', json_data)
#delete_user(new_dict)
