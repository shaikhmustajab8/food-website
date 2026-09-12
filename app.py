from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/order", methods=["POST"])
def order():
    name = request.form["name"]
    food = request.form["food"]
    quantity = request.form["quantity"]

    return f"""
    <h1>Order Confirmed!</h1>
    <p>Thank you, {name}.</p>
    <p>Your order: {food}</p>
    <p>Quantity: {quantity}</p>
    <p>Your food will be prepared soon.</p>
    <a href="/">Go Back</a>
    """

if __name__ == "__main__":
    app.run(debug=True)