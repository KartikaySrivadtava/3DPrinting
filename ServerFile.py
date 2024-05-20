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
        data = request.data
        print(data)
        # Upload user details
        with open('file.txt', 'w') as data_final:
            data_final.write(str(data))
        with open('file.txt', 'rb') as data_final:
            s3.upload_fileobj(data_final, bucket_name, 'user_data.txt')


app.run(debug=True)
