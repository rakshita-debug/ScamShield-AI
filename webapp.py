from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

suspicious_words = [
    "urgent",
    "verify your account",
    "password",
    "win prize",
    "click here",
    "bank details",
    "otp",
    "claim your reward"
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json(silent=True) or {}
    message = str(data.get("message", "")).strip()
    message_lower = message.lower()

    if not message:
        return jsonify({
            "error": "Please enter a message or suspicious link."
        }), 400

    detected_words = [
        word for word in suspicious_words
        if word in message_lower
    ]

    if detected_words:
        result = "Suspicious"
        explanation = "Potential scam indicators were found."
    else:
        result = "No suspicious keywords detected"
        explanation = (
            "This does not guarantee the message is safe."
        )

    return jsonify({
        "result": result,
        "detected_words": detected_words,
        "explanation": explanation
    })

if __name__ == "__main__":
    app.run(debug=True)