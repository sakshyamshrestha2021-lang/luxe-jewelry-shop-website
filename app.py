from flask import Flask, render_template,request
import time as t
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")
@app.route("/ring")
def ring():
    return render_template("ring.html")
@app.route("/necklace")
def necklace():
    return render_template("necklace.html")
@app.route("/checkout",methods=["POST"])
def checkout():
    items = request.form.get("item_name")
    price = request.form.get("price", "0")
    print(f"product : {items}")
    print(f"price : {price}")
    return render_template("checkout.html")
          

app.run(host="0.0.0.0", port=80,debug=True)
