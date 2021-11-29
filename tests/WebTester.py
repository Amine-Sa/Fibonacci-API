from flask import Flask
from flask import request, render_template
from flask_wtf import FlaskForm
from wtforms import SubmitField, RadioField, IntegerField
from wtforms.validators import DataRequired, NumberRange
import requests

app = Flask(__name__)
app.config["SECRET_KEY"] = "9ee24808950fd24f818ba6ee3763d29c"


class input_form(FlaskForm):
    my_number = IntegerField(
        "Number",
        validators=[DataRequired(message="Please Fill This Field"), NumberRange(min=0)],
    )
    choice = RadioField(
        "Method",
        choices=["Basic", "Functools", "Advanced", "Inverse"],
        validators=[DataRequired(message="Please Fill This Field")],
    )
    submit = SubmitField("Calculate")


@app.route("/", methods=["GET", "POST"])
def Home():
    response = False
    form = input_form()
    if request.method == "POST":
        if form.choice.data == "Basic":
            response = requests.get(
                f"http://127.0.0.1:5000/v1/fibonacci/basic/{form.my_number.data}"
            )
            return render_template("home.html", form=form, response=response)
        if form.choice.data == "Functools":
            response = requests.get(
                f"http://127.0.0.1:5000/v1/fibonacci/functools/{form.my_number.data}"
            )
            return render_template("home.html", form=form, response=response)
        if form.choice.data == "Advanced":
            response = requests.get(
                f"http://127.0.0.1:5000/v1/fibonacci/advanced/{form.my_number.data}"
            )
            return render_template("home.html", form=form, response=response)
        if form.choice.data == "Inverse":
            response = requests.get(
                f"http://127.0.0.1:5000/v1/reverse-fibonacci/{form.my_number.data}"
            )
            return render_template("home.html", form=form, response=response)
    elif request.method == "GET":
        return render_template("home.html", form=form)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080", debug=True)
