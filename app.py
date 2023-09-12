from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Do something
        form_data = request.form
        print(form_data)
        return render_template('index.html', form_data=form_data)
    else:
        form_data=None
        return render_template('index.html', form_data=form_data)

if __name__ == "__main__":
    try:
        app.run(debug=True)
    except Exception as e:
        print(e)