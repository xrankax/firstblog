from flask import Flask, render_template, request, url_for
import os

app = Flask(__name__)

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

@app.route("/", methods=["GET", "POST"])
def main():
    title="Top Page"
    return render_template("index.html", title=title)

@app.route("/profile", methods=["GET", "POST"])
def profile():
    title="AboutMe"
    return render_template("profile.html", title=title)

@app.route("/vocabulary", methods=["GET", "POST"])
def vocab():
    title="vocabulary"
    return render_template("vocab.html", title=title)

@app.route("/calculator/", methods=["GET", "POST"])
def calculator():
    title="Accounting Analysis"
    if request.method == "GET":
        return render_template("calculator.html", title = title)
    else:
        # numbers_name = request.form.getlist("numbers_name")
        numbers_name=["売上高","売上総利益","営業利益","経常利益","当期純利益"]
        numbers= request.form.getlist("num")
        return render_template("calculator_result.html", title = title, numbers_name = numbers_name, numbers = numbers)




# @app.route("/hello/")
# def hello():
#     hello = "<h1>こんにちは</h1>"
#     return hello

# @app.route('/hello/<string:str1>/<string:str2>')
# def show_str(str1, str2):
#     return "<h1>こんにちは{0}さん{1}さん</h1>".format(str1, str2)

# @app.route('/add/<int:num1>/<int:num2>')
# def show_add(num1, num2):
#     return "num1 + num2={}".format(num1+num2)

# @app.route('/div/<float:num1>/<float:num2>')
# def show_div(num1, num2):
#     return "num1 / num2={}".format(math.floor(num1/num2))

# if __name__ == "__main__":
#     app.run(debug=True)