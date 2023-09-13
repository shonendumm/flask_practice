from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api', methods=['POST'])
def process_json():
    try:
        data = request.json

        # Process the JSON data 
        result = process_data(data)

        # Create a response JSON
        response = {'message': 'JSON data processed successfully', 'result': result}
        return jsonify(response), 200
    
    except Exception as e:
        error_message = str(e)
        return jsonify({'error': error_message}), 400

def process_data(data):
    # Process the JSON data
    print('name', data.get('name'))
    print('age', data.get('age'))
    print('city', data.get('city'))

    return data

if __name__ == '__main__':
    app.run(debug=True)
