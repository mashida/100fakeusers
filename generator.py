from flask import Flask, render_template
import urllib.request
import json

app = Flask(__name__)

users = list()


#Code below is taking random name, lastname and email from special created API at randomapi.com
#For now I turned off taking data from randomapi.com because my free account is limited and allows me to take only 500 requets per day.

randomuser_link = 'https://randomuser.me/api/?inc=name,email&results=100'
response = urllib.request.urlopen(randomuser_link) 
content = response.read() 

data = json.loads(content)

for user in data['results']:
	users.append({'name':user['name']['first'], 'lastname':user['name']['last'], 'email':user['email']})

@app.route("/")
def home():
    return render_template('home.html', users = users)

if __name__ == '__main__':
	app.run(debug = True)