from flask import Flask, jsonify

app =Flask(__name__)

@app.route("/")
def home():
    name = "usama"
    id = 23
    resignation = "AI Engineer"
    data  = {"name":name,"id":id,"resignation":resignation}
    return jsonify(data)

app.run(debug=True)