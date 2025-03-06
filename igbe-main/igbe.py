from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import mysql.connector
import bcrypt

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# MySQL Configuration
db_config = {
    "host": "centerbeam.proxy.rlwy.net",
    "user": "root",
    "password": "pvLTyCYCgBbJoQdskITQclfRZZEYGhw",
    "database": "railway",
    "port": 10996
}

# Connect to MySQL
def connect_db():
    return mysql.connector.connect(**db_config)

@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')  # Store password directly

        if not username or not password:
            return '', 204  # No response (empty)

        # Insert into database (without hashing)
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password_hash) VALUES (%s, %s)", (username, password))
        conn.commit()
        cursor.close()
        conn.close()

        return '', 204  # Return empty response

    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Show error only if something goes wrong


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)