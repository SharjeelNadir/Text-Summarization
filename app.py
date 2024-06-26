from flask import Flask, render_template, request, redirect, session
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import re
import mysql.connector

app = Flask(__name__)

# MySQL database connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_database_password",
    database="name_of_database"
)

# Load the fine-tuned model and tokenizer
model_dir = './fine-tuned-model'
tokenizer = AutoTokenizer.from_pretrained(model_dir)
model = AutoModelForSeq2SeqLM.from_pretrained(model_dir)

# Function to preprocess text
def preprocess_text(text):
    # Remove extra whitespace and newline characters
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

# Function to summarize text
def summarize(text):
    inputs = tokenizer(
        "summarize: " + text,
        truncation=True,
        padding='longest',
        max_length=1024,  # Increase max length if needed
        return_tensors="pt"
    )
    
    summary_ids = model.generate(
        inputs['input_ids'],
        max_length=250,  # Increase the max length of the summary
        min_length=50,
        length_penalty=2.0,  # Adjust length penalty if needed
        num_beams=4,
        early_stopping=True
    )
    
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM logininfo WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()
        
        if user:
            session['username'] = username  # Store the username in session
            return redirect('/index')
        else:
            error = 'Incorrect username or password'
            return render_template('login.html', error=error)
    
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        cursor = connection.cursor()
        cursor.execute("INSERT INTO logininfo (username, password) VALUES (%s, %s)", (username, password))
        connection.commit()
        
        return redirect('/')
    
    return render_template('signup.html')

@app.route('/index', methods=['GET', 'POST'])
def index():
    if 'username' not in session:
        return redirect('/')
    
    summary = None
    text = None
    if request.method == 'POST':
        text = request.form['text']
        
        # Preprocess the text
        preprocessed_text = preprocess_text(text)
        
        # Summarize the preprocessed text
        summary = summarize(preprocessed_text)
        
        # Store summary in the database
        cursor = connection.cursor()
        cursor.execute("INSERT INTO summaries (username, summary) VALUES (%s, %s)", (session['username'], summary))
        connection.commit()
        
    # Retrieve previous summaries for the logged-in user
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT summary FROM summaries WHERE username = %s", (session['username'],))
    summaries = cursor.fetchall()
    
    return render_template('index.html', text=text, summary=summary, summaries=summaries)

if __name__ == '__main__':
    app.run(debug=True)
