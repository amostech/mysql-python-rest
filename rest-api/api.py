from flask import Flask, jsonify
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'admin'
app.config['MYSQL_DATABASE_DB'] = 'airlinedatadb'
app.config['MYSQL_DATABASE_HOST'] = '54.201.46.255'

mysql.init_app(app)

@app.route('/')
def get():
    cur = mysql.connect().cursor()
    cur.execute('''select * from airlinedatadb.flights''')
    r = [dict((cur.description[i][0], value)
              for i, value in enumerate(row)) for row in cur.fetchall()]
    return jsonify({'carrier_delays' : r})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)