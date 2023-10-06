from flask import Flask,request,render_template,jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:mypassword@localhost:3306/mydb"

# Silence deprecation warnings
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



db = SQLAlchemy(app)


class students1(db.Model):
    studentID = db.Column(db.String(20), primary_key=True)
    LastName = db.Column(db.String(80), nullable=False)
    FirstName = db.Column(db.String(80), nullable=False)
    Address = db.Column(db.String(200))
    City = db.Column(db.String(100))


@app.route("/",methods=["GET","POST"])
def index():
    if request.method=="POST":
        id = request.form['studentID']
        lname = request.form['LastName']
        fname = request.form['FirstName']
        address = request.form['Address']
        city = request.form['City']

      
        student = students1(studentID=id, LastName=lname, FirstName=fname, Address=address, City=city)
        db.session.add(student)
        db.session.commit()

        return "Successfully updated data in database"
    return render_template("index.html")

@app.route("/students")
def getusers():
    # Fetch data from the database and pass it to the template
    user_details = students1.query.all()
    return render_template("students.html", students=user_details)

if __name__=="__main__":
    app.run(debug=True)