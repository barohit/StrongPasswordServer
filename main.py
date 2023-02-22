from flask import Flask, render_template, request
app = Flask(__name__)

def hashPassword(password):
    return hash(password)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/returnHash', methods=["POST"])
def returnHashedPassword():
    pword = request.form['passfield']
    return render_template('hashPassword.html', password=hashPassword(pword))


if __name__ == "__main__":
    app.run(debug=True)

