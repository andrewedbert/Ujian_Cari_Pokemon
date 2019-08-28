from flask import Flask, render_template, request, redirect, jsonify
import requests

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template('pokehome.html')

@app.route('/hasil', methods=['POST'])
def hasil():
    body = request.form
    pokemon = str(body['nama'])
    pokelow = pokemon.lower()
    url = f'https://pokeapi.co/api/v2/pokemon/{pokelow}'

    data = requests.get(url)

    if data.status_code == 200:
        statistik = data.json()
        return render_template('responsefound.html', data1=str(statistik['name']).capitalize(), data2=statistik['id'], data3=statistik['sprites']['front_default'], data4=statistik['height'],data5=statistik['weight'])
    elif str(data) == """<Response [404]>""":
        return render_template('responsenotfound.html')


if __name__ == '__main__':
    app.run(debug=True)