from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>CryptoX Demo Platform</h1>
    <p>Welcome to CryptoX Trading Platform</p>
    <p>Deposit Approval System Enabled (Demo Mode)</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
