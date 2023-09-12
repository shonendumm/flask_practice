from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_json', methods=['POST'])
def process_json():
    try:
        # Get JSON data from the client
        data = request.get_json()
        print(data)
        # Process the JSON data (e.g., perform some calculations)
        result = process_data(data)

        # Create a response JSON
        response = {'message': 'JSON data processed successfully', 'result': result}

        return jsonify(response), 200
    except Exception as e:
        error_message = str(e)
        return jsonify({'error': error_message}), 400

def process_data(data):
    # Replace this with your own data processing logic
    # For demonstration, we'll simply return the input data as is
    return data

if __name__ == '__main__':
    app.run(debug=True)
