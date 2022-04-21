from flask import Flask, render_template, request, redirect, url_for, flash
from flaskext.mysql import MySQL

app = Flask(__name__)

#mysql connection
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Rose1957'
app.config['MYSQL_DATABASE_DB'] = 'socialdb'
mysql = MySQL()
mysql.init_app(app)

#settings
app.secret_key = 'mySecretKey'

#routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    try:
        email = request.form['email']
        age = request.form['age']
        sex = request.form['sex']
        favorite = request.form['favorite']
        facebook = request.form['facebook']
        whatsapp = request.form['whatsapp']
        twitter = request.form['twitter']
        instagram = request.form['instagram']
        tiktok = request.form['tiktok']
        cursor = mysql.get_db().cursor()
        query = """INSERT INTO participant
        (email, age, sex, favorite, facebook, whatsapp, twitter, instagram, tiktok)
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s);"""
        values = (email, age, sex, favorite, facebook, whatsapp, twitter, instagram, tiktok)
        cursor.execute(query, values)
        mysql.get_db().commit()
        flash('La encuesta ha sido guardada')
        return redirect(url_for('index'))
    except:
        flash('algo salio mal, no puedes dejar campos vacios, el email debe ser unico')
        return redirect(url_for('index'))

@app.route('/stats')
def stats():
    # import pdb; pdb.set_trace()
    try:
        cursor = mysql.get_db().cursor()
        query1 = 'SELECT COUNT(0) FROM participant;'
        cursor.execute(query1)
        length = cursor.fetchall()
        length = length[0][0]
        query2 = """SELECT AVG(facebook) AS facebook_time, AVG(whatsapp) AS whatsapp_time,
        AVG(twitter) AS twitter_time, AVG(instagram) AS instagram_time,
        AVG(tiktok) AS tiktok_time FROM participant;"""
        cursor.execute(query2)
        avg = cursor.fetchall()[0]
        avg = {'facebook': avg[0], 'whatsapp': avg[1], 'twitter': avg[2],'instagram': avg[3], 'tiktok': avg[4]}
        query3 = 'SELECT favorite, COUNT(0) AS count_favorites FROM participant GROUP BY favorite ORDER BY count_favorites DESC LIMIT 1'
        cursor.execute(query3)
        favorite = cursor.fetchall()
        query4 = 'SELECT favorite, COUNT(0) AS count_favorites FROM participant GROUP BY favorite ORDER BY count_favorites ASC LIMIT 1'
        cursor.execute(query4)
        unlike = cursor.fetchall()
        return render_template('stats.html', LENGTH = length, AVG = avg, FAVORITE = favorite, UNLIKE = unlike)
    except:
        flash('algo salio mal o no hay datos que mostrar')
        return redirect(url_for('index'))

#init server
if __name__ == '__main__':
    app.run(port = 3000, debug = True)
