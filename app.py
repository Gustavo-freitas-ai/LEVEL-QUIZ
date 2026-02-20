from flask import Flask, render_template, request, redirect

app = Flask(__name__)

erros = 0

@app.route("/")
def home():
    global erros
    erros = 0
    return render_template("index.html")


@app.route("/level1", methods=["GET", "POST"])
def level1():
    global erros

    resultado = ""

    if request.method == "POST":
        resposta = request.form["resposta"]

        if resposta == "4":
            erros = 0
            return redirect("/level2")

        else:
            erros += 1
            resultado = f"Err! 😢 ({erros}/3)"

        if erros == 3:
            erros = 0
            return redirect("/")

    return render_template("level1.html", resultado=resultado)


@app.route("/level2", methods=["GET", "POST"])
def level2():
    global erros

    resultado = ""

    if request.method == "POST":
        resposta = request.form["resposta"]

        if resposta == "2": 
            resultado = "You Win! 🥳"
        else:
            erros += 1
            resultado = f"Err! 😢 ({erros}/3)"

        if erros == 3:
            erros = 0
            return redirect("/")

    return render_template("level2.html", resultado=resultado)


if __name__ == "__main__":
    app.run(debug=True)