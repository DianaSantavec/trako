import requests 
import json





respone = response.get(url, parameters)


yourKey = "fcf13eab00317ac32b50020c2ff8ef81"
yourToken = "" #secret

URL = "https://api.trello.com/1/members/me/boards"
#PARAMS = {key={fcf13eab00317ac32b50020c2ff8ef81}}
keys = {'key':'fcf13eab00317ac32b50020c2ff8ef81', 'token' : 'j'}

URL = "https://api.trello.com/1/members/me/boards?key={fcf13eab00317ac32b50020c2ff8ef81}&token={j}"

response = requests.get('https://api.trello.com/1/members/me/boards', params=keys)


#response['list'] = [json.loads(s) for s in response['list']]
#with open('file.json', 'w') as output:
#    json.dump(response, output)

responseJson = response.json()

for data in responseJson:
    print(data['id'])
    url = 'https://api.trello.com/1/boards/' + data['id']
    boardResponse = requests.get(url, params=keys)
    boardResponseJson = boardResponse.json()
    print(boardResponseJson['name'])



#
#with open ('data.json', 'w') as outfile:
#    json.dump(responseJson, outfile)

#print(responseJson)