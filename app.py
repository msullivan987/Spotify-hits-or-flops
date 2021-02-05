from flask import Flask, render_template, jsonify
import pandas as pandas
import csv 
import psycopg2 as psycopg2

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/spotify_data")
def read_spotify_hits_sql():
    conn = psycopg.connect(dbname="spotify_data", user="postgres", password="postgres", host="127.0.0.1", port="5432")
    dataframe = pd.read_sql("SELECT * FROM spotify_data", conn)
    json_data = dataframe.to_json(orient="records")
    return json_data

if __name__ == "main":
    app.run(debug=True)