from flask import Flask, render_template
import urllib.request
import json

app = Flask(__name__)

users = list()

api_key = 'ALUI-UR40-40ZC-TFTW'
api_ref = '1d09skuj'
parameter_amount = '&results=25'


#Code below is taking random name, lastname and email from special created API at randomapi.com
#For now I turned off taking data from randomapi.com because my free account is limited and allows me to take only 500 requets per day.

#for iter in range(1):
#	random_api_link = 'https://randomapi.com/api/?key='+ api_key + '&ref=' + api_ref +'&fmt=json' + '&results=100'
#	response = urllib.request.urlopen(random_api_link) 
#	content = response.read() 

#	data = json.loads(content)

#	for user in data['results']:
#		users.append(user)

#So I use generated data in order to check if code works

users = [
{'name': 'Bridget', 'lastname': 'Bradtke', 'email': 'Antwan_Jacobson@hotmail.com'},
{'name': 'Ole', 'lastname': 'Klein', 'email': 'Deshaun9@gmail.com'},
{'name': 'Guido', 'lastname': 'Kassulke', 'email': 'Mariah.Turcotte@hotmail.com'},
{'name': 'Catharine', 'lastname': 'Wolf', 'email': 'Bailee.Skiles53@gmail.com'},
{'name': 'Michel', 'lastname': 'Breitenberg', 'email': 'Leanne.Larson32@yahoo.com'},
{'name': 'Rodrick', 'lastname': 'Nitzsche', 'email': 'Tommie_Schinner0@gmail.com'},
{'name': 'Bobby', 'lastname': 'Durgan', 'email': 'Tianna_Botsford@yahoo.com'},
{'name': 'Laisha', 'lastname': 'Heathcote', 'email': 'Joel.Abshire42@yahoo.com'},
{'name': 'Daron', 'lastname': 'Hamill', 'email': 'Albin2@yahoo.com'},
{'name': 'Keara', 'lastname': 'Tremblay', 'email': 'Delphia_Schowalter@yahoo.com'},
{'name': 'Osbaldo', 'lastname': 'Kessler', 'email': 'Angus.Johns@yahoo.com'},
{'name': 'Mae', 'lastname': 'Carter', 'email': 'Nicklaus_Raynor9@yahoo.com'},
{'name': 'Macey', 'lastname': 'Dietrich', 'email': 'Zion.Wuckert@gmail.com'},
{'name': 'Lorena', 'lastname': 'Bartoletti', 'email': 'Alverta_Bednar@gmail.com'},
{'name': 'Theron', 'lastname': 'Johns', 'email': 'Chase_Lemke@yahoo.com'},
{'name': 'Shaylee', 'lastname': 'Welch', 'email': 'Raven.Russel93@hotmail.com'},
{'name': 'Alexis', 'lastname': 'Pollich', 'email': 'Raoul.Stokes@yahoo.com'},
{'name': 'Maurine', 'lastname': 'Macejkovic', 'email': 'Rosamond_Gerhold@yahoo.com'},
{'name': 'Santina', 'lastname': 'Mayert', 'email': 'Cesar.Balistreri10@hotmail.com'},
{'name': 'Aiyana', 'lastname': 'Lind', 'email': 'Emilia_McLaughlin@gmail.com'},
{'name': 'Filomena', 'lastname': 'Lowe', 'email': 'Precious_Turcotte34@hotmail.com'},
{'name': 'Edwardo', 'lastname': 'White', 'email': 'Tatum.Kuvalis51@yahoo.com'},
{'name': 'Ethel', 'lastname': 'Blick', 'email': 'Mertie.Rodriguez15@gmail.com'},
{'name': 'Lexus', 'lastname': 'Ernser', 'email': 'Bennie.Daniel27@hotmail.com'}
]

email_sorted = sorted(users, key=lambda k: k['email'])
name_sorted = sorted(users, key=lambda k: k['name'])
lastname_sorted = sorted(users, key=lambda k: k['lastname'])

@app.route("/")
def home():
    return render_template('home.html', users = name_sorted)

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__':
	app.run(debug = True)