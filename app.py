from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from models import User, db  # Import User model and db from models.py


basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)




@app.route('/')
def index():
    return render_template('index.html')



@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'username': user.username, 'email': user.email} for user in users])

@app.route('/users/create')
def create_user():
    username = request.args.get('username')
    email = request.args.get('email')
    print(f"received {username}")
    print(f"received {email}")
    if username and email:
        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    else:
        return jsonify({'error': 'Missing username or email in URL parameters'}), 400

# http://localhost:5000/users/create?username=john2&email=john2@example.com




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
