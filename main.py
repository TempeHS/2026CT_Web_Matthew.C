from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/index.html')
@app.route('/')
def index():
    card_data = (
        ("Moon Knight","How To Play Moon Knight For Beginners","How To Play","static/images/thumb/thumb1.png"),
        ("The Punisher","How To Play The Punisher For Beginners","How To Play","static/images/thumb/thumb2.png"),
        ("Jeff The Landshark","How To Play Jeff The Landshark For Beginners","How To Play","static/images/thumb/thumb3.png"),
        ("Rocket Raccoon","How To Play Rocket Raccoon For Beginners","How To Play","static/images/thumb/thumb4.png"),
        ("Groot","How To Play Groot For Beginners","How To Play","static/images/thumb/thumb5.png"),
        ("Magneto","How To Play Magneto For Beginners","How To Play","static/images/thumb/thumb6.png"),
    )
    return render_template("index.html", cards=card_data), 200

if __name__ == '__main__':
    app.run(debug=True)