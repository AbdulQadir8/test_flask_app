from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

data = []

@app.route("/", methods=['POST','GET'])
def home():
    if request.method == "POST":
        name = request.json['name']
        email = request.json['email']
        roll = request.json['roll']
        course = request.json['course']
        record1 = {"name":name,
                "email":email,
                "roll":roll,
                "course":course}
        data.append(record1)
        
    return data
    
@app.route("/about", methods=['GET','POST'])
def about():
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)