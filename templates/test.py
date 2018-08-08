import urllib.request
import json

users = list()

api_key = 'ALUI-UR40-40ZC-TFTW'
api_ref = '1d09skuj'
parameter_amount = '&results=25'


for iter in range(1):
#	random_api_link = 'https://randomapi.com/api/?key='+ api_key + '&ref=' + api_ref +'&fmt=json' + '&results=100'
	randomuser_link = 'https://randomuser.me/api/?inc=name,email&results=100'
	response = urllib.request.urlopen(randomuser_link) 
	content = response.read() 

	data = json.loads(content)

	for user in data['results']:
		#users.append(user)
		print(user['email'])

#users = [
#{'name': 'Bridget', 'lastname': 'Bradtke', 'email': 'Antwan_Jacobson@hotmail.com'},
#{'name': 'Ole', 'lastname': 'Klein', 'email': 'Deshaun9@gmail.com'},
#{'name': 'Guido', 'lastname': 'Kassulke', 'email': 'Mariah.Turcotte@hotmail.com'},
#{'name': 'Catharine', 'lastname': 'Wolf', 'email': 'Bailee.Skiles53@gmail.com'},
#{'name': 'Michel', 'lastname': 'Breitenberg', 'email': 'Leanne.Larson32@yahoo.com'},
#{'name': 'Rodrick', 'lastname': 'Nitzsche', 'email': 'Tommie_Schinner0@gmail.com'},
#{'name': 'Bobby', 'lastname': 'Durgan', 'email': 'Tianna_Botsford@yahoo.com'},
#{'name': 'Laisha', 'lastname': 'Heathcote', 'email': 'Joel.Abshire42@yahoo.com'},
#{'name': 'Daron', 'lastname': 'Hamill', 'email': 'Albin2@yahoo.com'},
#{'name': 'Keara', 'lastname': 'Tremblay', 'email': 'Delphia_Schowalter@yahoo.com'},
#{'name': 'Osbaldo', 'lastname': 'Kessler', 'email': 'Angus.Johns@yahoo.com'},
#{'name': 'Mae', 'lastname': 'Carter', 'email': 'Nicklaus_Raynor9@yahoo.com'},
#{'name': 'Macey', 'lastname': 'Dietrich', 'email': 'Zion.Wuckert@gmail.com'},
#{'name': 'Lorena', 'lastname': 'Bartoletti', 'email': 'Alverta_Bednar@gmail.com'},
#{'name': 'Theron', 'lastname': 'Johns', 'email': 'Chase_Lemke@yahoo.com'},
#{'name': 'Shaylee', 'lastname': 'Welch', 'email': 'Raven.Russel93@hotmail.com'},
#{'name': 'Alexis', 'lastname': 'Pollich', 'email': 'Raoul.Stokes@yahoo.com'},
#{'name': 'Maurine', 'lastname': 'Macejkovic', 'email': 'Rosamond_Gerhold@yahoo.com'},
#{'name': 'Santina', 'lastname': 'Mayert', 'email': 'Cesar.Balistreri10@hotmail.com'},
#{'name': 'Aiyana', 'lastname': 'Lind', 'email': 'Emilia_McLaughlin@gmail.com'},
#{'name': 'Filomena', 'lastname': 'Lowe', 'email': 'Precious_Turcotte34@hotmail.com'},
#{'name': 'Edwardo', 'lastname': 'White', 'email': 'Tatum.Kuvalis51@yahoo.com'},
#{'name': 'Ethel', 'lastname': 'Blick', 'email': 'Mertie.Rodriguez15@gmail.com'},
#{'name': 'Lexus', 'lastname': 'Ernser', 'email': 'Bennie.Daniel27@hotmail.com'}
#]


email_sorted = sorted(users, key=lambda k: k['email'])
name_sorted = sorted(users, key=lambda k: k['name':'first'])
lastname_sorted = sorted(users, key=lambda k: k['name':'last'])



print('='*20)
print('Email sorted users\n')

for user in email_sorted:
	#print(user['email'] + " : " + user['name']['first'] + " " + user['name']['last'])
	print(user)

'''

print('='*20)
print('name sorted users\n')

for user in name_sorted:
	print(user['name']['first'] + " " + user['name']['last'] + " : " + user['email'])

print('='*20)
print('lastname sorted users\n')

for user in lastname_sorted:
	print(user['name']['last'] + " " + user['name']['first'] + " : " + user['email'])


#print(users['results'])


#data = json.loads(content.decode("utf8")) 
#print(data) 
#print(data['type'])
'''