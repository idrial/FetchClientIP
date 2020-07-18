# a tool to find the public facing IP address of a particular endpoint as an interviewing project

from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__) 

@app.route('/', methods=['GET'])
def get_splash():

	# this is a public endpoint AWS gives you to use to check IPs of client request comes from

	ip_verify_flask_server = requests.get('https://checkip.amazonaws.com').text.strip()

	# will return public IP of client regardless if its behind a proxy using env 
	
	if request.environ.get('HTTP_X_FORWARDED_FOR') is None: client_ip_address = request.environ['REMOTE_ADDR']
	else: client_ip_address = request.environ['HTTP_X_FORWARDED_FOR']

# return with the client IP in different forms so we can display it in the html template show how it's calculated 
	return render_template("homepage.html", ip=client_ip_address, ip2=ip_verify_flask_server)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
