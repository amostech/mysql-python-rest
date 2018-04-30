from flask import Flask, jsonify
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'admin'
app.config['MYSQL_DATABASE_DB'] = 'airlinedatadb'
app.config['MYSQL_DATABASE_HOST'] = 'ec2-18-236-97-154.us-west-2.compute.amazonaws.com'

mysql.init_app(app)

@app.route('/')
def get():
    cur = mysql.connect().cursor()
    cur.execute('''select UNIQUE_CARRIER, count(*) from airlinedatadb.flights where ARR_DELAY > 30 group by UNIQUE_CARRIER order by count(*) desc;''')
    r = [dict((cur.description[i][0], value)
              for i, value in enumerate(row)) for row in cur.fetchall()]
    return jsonify({'carrier_delays' : r})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)