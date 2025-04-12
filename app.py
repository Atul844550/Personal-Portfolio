from flask import Flask, request, redirect, render_template
import mysql.connector

app = Flask(__name__)

# MySQL Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="8445501402",  
    database="personal_portfolio"
)
cursor = db.cursor()

# Home Route
@app.route('/home')
def home():
    return render_template('index.html')

# Contact Form Handler
from flask import Flask, request, redirect, render_template



@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    try:
       
        cursor = db.cursor()
        cursor.execute("INSERT INTO users (name, email, message) VALUES (%s, %s, %s)", (name, email, message))
        db.commit()
        cursor.close()

        
        return render_template("thankyou.html")
    
    except Exception as e:
        print("Database Error:", e)
        return "Something went wrong!"
    

@app.route('/thankyou')
def thank_you():
    return render_template("thankyou.html")




#  Run App
if __name__ == '__main__':
    app.run(debug=True)
