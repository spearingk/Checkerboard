from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", row=8, col=8, color_one='red', color_two='black')

@app.route('/<int:x>')
def row(x):
    return render_template("index.html", row=x, col=8, color_one='red', color_two='black')

@app.route('/<int:x>/<int:y>')
def row_col(x,y):
    return render_template("index.html", row=x, col=y, color_one='red', color_two='black')

@app.route('/<int:x>/<int:y>/<string:colorone>')
def row_col_colorone(x,y,colorone):
    return render_template("index.html", row=x, col=y, color_one=colorone, color_two='black')

@app.route('/<int:x>/<int:y>/<string:colorone>/<string:colortwo>')
def row_col_colortwo(x,y,colorone,colortwo):
    return render_template("index.html", row=x, col=y, color_one=colorone, color_two=colortwo)


if __name__=="__main__":
    app.run(debug=True)