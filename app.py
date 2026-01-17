from flask import Flask, render_template, request

from alerts import detect_attack

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def login():
    alert = None
    payload = None

    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")

        payload = f"{username} {password}"
        attack = detect_attack(payload)

        if attack:
            alert = attack
            print(r"""
//      ___  _ _           _     _ _ _ 
//     / _ \| | |         | |   | | | |
//    / /_\ \ | | ___ _ __| |_  | | | |
//    |  _  | | |/ _ \ '__| __| | | | |
//    | | | | | |  __/ |  | |_  |_|_|_|
//    \_| |_/_|_|\___|_|   \__| (_|_|_)
//                                   
//                                   """)
            print(f"[ALERT] Detected: {attack}")
            print(f"[PAYLOAD] {payload}")
        else:
            alert = "No attack detected"
            print(f"[INFO] Clean input: {payload}")

    return render_template("login.html", alert=alert, payload=payload)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
