from flask import*

app = Flask(__name__)

@app.route("/")
def base():
    return render_template("base.html")

@app.route("/clothes/")
def clothes():
    clothers = [
        {
            "id": 1,
            "size": 44,
            "color": "red"
        },
        {
            "id": 2,
            "size": 46,
            "color": "blue"
        }
    ]
    context = {"clothes": clothers}
    return render_template("clothes.html", **context)

@app.route("/jackets/")
def jackets():
    jackets = [
        {
            "id": 1,
            "size": 48,
            "color": "grey"
        },
        {
            "id": 2,
            "size": 50,
            "color": "black"
        }
    ]
    context = {"jackets": jackets}
    return render_template("jackets.html", **context)

@app.route("/shoes/")
def shoes():
    shoes = [
        {
            "id": 1,
            "size": 41,
            "color": "grey"
        },
        {
            "id": 2,
            "size": 40,
            "color": "black"
        }
    ]
    context = {"shoes": shoes}
    return render_template("shoes.html", **context)

if __name__ == "__main__":
    app.run()