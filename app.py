from flask import Flask, render_template, request, url_for, redirect


app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Do something
        form_data = request.form
        print(form_data)
        return render_template('index.html',form_data=form_data)
    else:
        return render_template('index.html',form_data=None)
        


if __name__ == "__main__":
    try:
        app.run(debug=True)
    except Exception as e:
        print(e)