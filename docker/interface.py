from flask import Flask, request, jsonify
import pymysql

app = Flask(__name__)

def query_database(sqlstring):
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='123456',
                                 database='test',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            cursor.execute(sqlstring)
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

@app.route('/api/sql-execute', methods=['POST'])
def handle_select():
    data = request.get_json()
    sqlstring = data.get('sql')
    print(sqlstring)
    if not sqlstring:
        return "No SQL string provided.", 400

    try:
        data = query_database(sqlstring)
        print(data)
        if "error" in data:
            return jsonify(data), 500
        return jsonify(data)
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)