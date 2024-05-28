import boto3
from flask import Flask, request
from flask_cors import CORS

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png'}

bucket_name = ""
ACCESS_ID = ''
ACCESS_KEY = ''
s3 = boto3.client('s3', aws_access_key_id=ACCESS_ID, aws_secret_access_key=ACCESS_KEY)
app = Flask(__name__)
app.debug = True
CORS(app)


@app.route("/upload", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        print("Inside Post Method")
        firstname = request.form.get('firstname')
        print("First name is", firstname)
        lastname = request.form.get('lastname')
        print("Last name is", lastname)
        email = request.form.get('email')
        print("Email is", email)
        address = request.form.get('address')
        print("Address is", address)
        pin = request.form.get('pin')
        print("PIN is", pin)
        city = request.form.get('city')
        print("City is", city)
        file = request.files['pdf']
        print(file)
        # Upload user details
        with open('file.txt', 'w') as data_final:
            data_final.write(str(firstname)+','+str(lastname)+','+str(email)+','+str(address)+','+str(city)+','+str(pin))
        with open('file.txt', 'rb') as data_final:
            s3.upload_fileobj(data_final, bucket_name, 'user_data.txt')
        s3.upload_fileobj(file, bucket_name, 'Uploaded File.pdf')
        print("Files loaded successfully")
    return "successful"


app.run(debug=True)
