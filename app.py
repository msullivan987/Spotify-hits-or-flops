from flask import Flask, render_template, jsonify
# import pandas as pandas
# import csv 
# import psycopg2 as psycopg2

app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/spotify_data")
# def read_spotify_hits_sql():
#     conn = psycopg.connect(dbname="spotify_data", user="postgres", password="BUChoy123!!!", host="127.0.0.1", port="5432")
#     dataframe = pd.read_sql("SELECT * FROM spotify_data", conn)
#     json_data = dataframe.to_json(orient="records")
#     return json_data

# if __name__ == "main":
#     app.run(debug=True)

@app.route('/')
def home():
    return render_template("home.html")


@app.route("/hitwords")
def hitwords():
    return render_template("hitwords.html")


@app.route('/contributors')
def contributors():
    return render_template('contributors.html')


@app.route('/barcharts')
def bar_2():
    return render_template('bars.html')

@app.route('/barcharts2')
def bar_3():
    return render_template('bars2.html')

@app.route('/billboard')
def billboard():
    return render_template('billboard.html')

@app.route('/newmusic')
def newmusic():
    return render_template('newmusicplaylist.html')



# @app.route("/spotify_data")
# def read_spotify_hits_sql():
#     conn = psycopg.connect(dbname="spotify_data", user="postgres", password="BUChoy123!!!", host="127.0.0.1", port="5432")
#     dataframe = pd.read_sql("SELECT * FROM spotify_data", conn)
#     json_data = dataframe.to_json(orient="records")
#     return json_data


if __name__ == '__main__':
    app.run(debug=True)
