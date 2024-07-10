from flask import Flask, render_template

app = Flask(__name__, template_folder='../view') 

@app.route("/")
def home():
    return render_template("areaDeslogada.html")
    
if __name__ == "__main__":
    app.run(debug=True)