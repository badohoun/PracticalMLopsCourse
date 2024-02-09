from flask import Flask, render_template,request

# init app

app = Flask(__name__)

# Route
@app.route('/')
def index():
    return 'Hello Practical Mlops Hack course'

# Adding HTML 
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
    return render_template('home.html',firstname=firstname.upper(),lastname=lastname.upper())


# Templating
@app.route('/about')
def about():
    mission = "Optimizing Data and ML Models with Python"
    return render_template('about.html' , mission_front_end=mission)

if __name__== '__main__':
    app.run(debug=True)