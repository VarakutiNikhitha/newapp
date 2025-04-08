from flask import Flask, render_template, request, redirect, url_for
import pymysql
import bcrypt

app = Flask(__name__)

# MySQL DB connection
db = pymysql.connect(
    host='vamsi-databse.cxue66ieak7c.ap-south-1.rds.amazonaws.com',  # Replace with your RDS endpoint
    user='admin',
    password='Svamsi79955',
    database='userdb',
    cursorclass=pymysql.cursors.DictCursor
)

cursor = db.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    address = request.form['address']
    phonenumber = request.form['phonenumber']
    password = request.form['password'].encode('utf-8')
    hashed_password = bcrypt.hashpw(password, bcrypt.gensalt()).decode('utf-8')

    insert_query = "INSERT INTO user (name, email, address, phonenumber, password) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(insert_query, (name, email, address, phonenumber, hashed_password))
    db.commit()

    cursor.execute("SELECT * FROM user ORDER BY id DESC")
    data = cursor.fetchall()
    return render_template('submitteddata.html', data=data)

@app.route('/get-data', methods=['GET', 'POST'])
def get_data():
    if request.method == 'POST':
        input_id = request.form['input_id']
        cursor.execute("SELECT * FROM user WHERE id = %s", (input_id,))
        data = cursor.fetchall()
        return render_template('data.html', data=data, input_id=input_id)
    return render_template('get_data.html')

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete_data(id):
    if request.method == 'POST':
        cursor.execute("DELETE FROM user WHERE id = %s", (id,))
        db.commit()
        return redirect(url_for('get_data'))
    return render_template('delete.html', id=id)

if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')
