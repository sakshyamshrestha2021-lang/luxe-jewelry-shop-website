from flask import Flask, render_template,request

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
PRODUCTS = {"Gold Ring": 120, "Silver Necklace": 80}
@app.route("/checkout", methods=["POST"])
def checkout():
    item = request.form.get("item_name")
    price = PRODUCTS.get(item)
    if price is None:
        return "Unknown item", 400
    print(f"product : {item}")
    print(f"product : {price}")
    return render_template("checkout.html", item=item, price=price)

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=80)
