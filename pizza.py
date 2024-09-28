import sqlite3
from flask import Flask, render_template, url_for, request, redirect,jsonify
from joblib import load
from flask_bcrypt import Bcrypt
import pickle

app = Flask(__name__)
app.secret_key = "__privatekey__"
bcrypt = Bcrypt(app)


conn = sqlite3.connect('sqlite.db')
c = conn.cursor()
c.execute("""
    CREATE TABLE IF NOT EXISTS user (
        user_name VARCHAR(10) PRIMARY KEY,
        password TEXT,
        Email Email
    )
""")
conn.commit()
conn.close()

@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('sqlite.db')
        c = conn.cursor()
        c.execute("SELECT * FROM user WHERE user_name = ? AND password = ?", (username, password))
        if not c.fetchone():
            conn.close()
            return render_template('login.html', error="Incorrect Username or Password")
        else:
            conn.close()
            return render_template('index.html', name=username)
    if request.method=='GET':
        pass 
    return render_template('login.html')

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username and password:
            conn = sqlite3.connect('sqlite.db')
            c = conn.cursor()
            c.execute("SELECT * FROM user WHERE user_name = (?)", (username,))
            if c.fetchone():
                conn.close()
                return render_template('error.html', error="User already exists")
            else:
                c.execute("INSERT INTO user (user_name, password) VALUES (?, ?)", (username, password))
                conn.commit()
                conn.close()
                return redirect(url_for('login'))
    return render_template('signup.html')


@app.route('/predict', methods=['POST'])
def predict(): 
    l1 = load('Model\pizza_category_joblib')
    l2 = load('Model\pizza_size_joblib')
    l3 = load('Model\pizza_name_joblib')
    l4 = load('Model\pizza_ingredients_joblib')
        
    if request.method == 'POST':
        data = request.form
        sample = list(data.values())
        # sample = [1,'M','Classic','Mozzarella Cheese, Provolone Cheese, Smoked Gouda Cheese, Romano Cheese, Blue Cheese, Garlic','The Five Cheese Pizza']
        sample[1] = l1.transform([sample[1]])[0]
        sample[2] = l2.transform([sample[2]])[0]
        sample[3] = l3.transform([sample[3]])[0]
        sample[4] = l4.transform([sample[4]])[0]
        
        # sample[2] = l1.transform([sample[2]])[0]
        # sample[3] = l3.transform([sample[3]])[0]
        # sample[4] = l2.transform([sample[4]])[0]
        sample = list(map(float, sample))
        
        with open('Model\Model (1).pkl','rb') as f:
            lreg = pickle.load(f)
            
        final = lreg.predict([sample])[0]
        return render_template('result_prediction.html', result = final)
        
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
