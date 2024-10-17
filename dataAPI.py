from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# Configure MySQL connection
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'tesco_data'
}

# Connect to MySQL
def connect_db():
    return mysql.connector.connect(**db_config)

@app.route('/', methods=['GET'])
def get_products():
    conn = connect_db()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return jsonify(products)



if __name__ == '__main__':
    app.run()