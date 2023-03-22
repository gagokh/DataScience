from flask import Flask,render_template, request, redirect, url_for, flash
import psycopg2
import psycopg2.extras 

app=Flask(__name__,template_folder='template')

DB_HOST = "localhost"
DB_NAME = "imdb"
DB_USER = "postgres"
DB_PASS = "Admin"
 
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)


@app.route("/")
def home():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    s = "SELECT * FROM actors LIMIT 100"
    cur.execute(s) # Execute the SQL
    list_users = cur.fetchall()
    return render_template('home.html', list_users = list_users)

@app.route("/about/")
def layout():
    return render_template('about.html')

if __name__=="__main__":
    app.run(debug=True)
