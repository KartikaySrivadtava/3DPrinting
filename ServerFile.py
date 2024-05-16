import io
import json
import boto3
import pandas as pd
from flask import Flask, request, render_template

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png'}

bucket_name = ""
ACCESS_ID = ''
ACCESS_KEY = ''
s3 = boto3.client('s3', aws_access_key_id=ACCESS_ID, aws_secret_access_key=ACCESS_KEY)
app = Flask(__name__)
app.debug = True


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        first_name = request.form.get("fname")
        last_name = request.form.get("lname")
        address = request.form.get("address")
        email = request.form.get("email")
        uploaded_file = request.files["file-to-save"]

        new_filename = first_name + '_' + last_name + '.' + uploaded_file.filename.rsplit('.', 1)[1].lower()
        print(uploaded_file)

        user_info = {
            "first_name": first_name,
            "last_name": last_name,
            "address": address,
            "email": email,
        }

        # Upload user details
        with open('file.txt', 'w') as data:
            data.write(str(user_info))
        with open('file.txt', 'rb') as data:
            s3.upload_fileobj(data, bucket_name, 'user_data.txt')
        # Upload file
        s3.upload_fileobj(uploaded_file, bucket_name, new_filename)
    return render_template('index.html')


app.run(debug=True)
