from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/index.html')
@app.route('/')
def index():
    card_data = (
        ("Moon Knight","How To Play Moon Knight For Beginners","How To Play","static/images/thumb/thumb1.png","/moonknight.html"),
        ("The Punisher","How To Play The Punisher For Beginners","How To Play","static/images/thumb/thumb2.png","/punisher.html"),
        ("Jeff The Landshark","How To Play Jeff The Landshark For Beginners","How To Play","static/images/thumb/thumb3.png","/jeff.html"),
        ("Rocket Raccoon","How To Play Rocket Raccoon For Beginners","How To Play","static/images/thumb/thumb4.png","/rocket.html"),
        ("Groot","How To Play Groot For Beginners","How To Play","static/images/thumb/thumb5.png","/groot.html"),
        ("Magneto","How To Play Magneto For Beginners","How To Play","static/images/thumb/thumb6.png","/magneto.html"),
    )
    return render_template("index.html", cards=card_data), 200

@app.route('/contact.html')
def contact():
    return render_template("contact.html"), 200

@app.route('/duelist.html')
def duelist():
    card_data = (
        ("Moon Knight","How To Play Moon Knight For Beginners","How To Play","static/images/thumb/thumb1.png","/moonknight.html"),
        ("The Punisher","How To Play The Punisher For Beginners","How To Play","static/images/thumb/thumb2.png","/punisher.html"),
        )
    return render_template("duelist.html", cards=card_data), 200

@app.route('/strategist.html')
def strategist():
    card_data = (
       ("Jeff The Landshark","How To Play Jeff The Landshark For Beginners","How To Play","static/images/thumb/thumb3.png","/jeff.html"),
        ("Rocket Raccoon","How To Play Rocket Raccoon For Beginners","How To Play","static/images/thumb/thumb4.png","/rocket.html"),
        )
    return render_template("strategist.html", cards=card_data), 200

@app.route('/vanguard.html')
def vanguard():
    card_data = (
        ("Groot","How To Play Groot For Beginners","How To Play","static/images/thumb/thumb5.png","/groot.html"),
        ("Magneto","How To Play Magneto For Beginners","How To Play","static/images/thumb/thumb6.png","/magneto.html"),
        )
    return render_template("vanguard.html", cards=card_data), 200

if __name__ == '__main__':
    app.run(debug=True)